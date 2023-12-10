#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sudoku Solver Using Constraint Satisfaction Problem Approach

2021 Feb 11, Jaroslav Langer
"""

import sys
import math
import numpy as np
import time
import copy

class Sudoku():
    """Reads sudoku file into matrix, writes sudoku matrix into file"""

    states_visited = 0

    def __repr__(self):
        return (f"<class 'Sudoku':\n{self.matrix}\n>")


    @classmethod
    def read_instance(cls, input_iter, shape=(9,9)):
        """
        Return Sudoku instance, read iterable input into 2D array

        Format description:
        * Lines starting with hash and newlines are ignored
        * Odd columns are ignored (first column is even)
        * Numbers are extracted from the even columns
        * Zeros can be denoted with 0 or with space character ' '
        """

        sudoku = Sudoku()

        matrix_list = [int(n) if n != ' ' else 0
                for row, line in enumerate(input_iter)
                        if (line[0] not in ['#', '\r', '\n'])
                                for i, n in enumerate(list(line))
                                        if ((i % 2 == 0)
                                                and (i <= (shape[0] - 1) * 2))]
        matrix = np.reshape(matrix_list, shape)
        return matrix


    @classmethod
    def write_matrix(cls, matrix, file_out):
        """
        Writes matrix to given file_out.

        The format was copied to match http://lipas.uwasa.fi/~timan/sudoku/
        so the results would be possible to diff easily.
        """

        for row, line in enumerate(matrix):
            for col, elem in enumerate(line):
                print(f'{elem} ', file=file_out, end='')
                if (col in [2, 5]):
                    print('| ', file=file_out, end='')
                if (col == 8):
                    print(' = 0,45', file=file_out, end='')

            print(file=file_out, end='\r\n')
            if (row in [2, 5]):
                print('---------------------', file=file_out, end='\r\n')
            if (row == 8):
                print(file=file_out, end='\r\n')
                print('0 0 0 0 0 0 0 0 0 ', file=file_out, end='\r\n')
                print('45 45 45 45 45 45 45 45 45 ', file=file_out, end='\r\n')
                print('\r\n', file=file_out, end='\r\n')


    @classmethod
    def is_consistent(cls, idx, matrix):
        """Check whether the var's row, column and box have only unique values"""

        unique_row = np.unique(matrix[idx[0], : ], return_counts=True)
        duplicated_row = any(unique_row[1][int(0 in unique_row[0]): ] > 1)

        unique_col = np.unique(matrix[ :, idx[1]], return_counts=True)
        duplicated_col = any(unique_col[1][int(0 in unique_col[0]): ] > 1)

        box_x_start, box_y_start = (3 * (idx[0] // 3)), (3 * (idx[1] // 3))
        unique_box = np.unique(
                matrix[
                         box_x_start : box_x_start + 3,
                         box_y_start : box_y_start + 3
                ], return_counts=True
        )
        duplicated_box = any(unique_box[1][int(0 in unique_box[0]): ] > 1)

        return (not (duplicated_row or duplicated_col or duplicated_box))


    @classmethod
    def backtracking_rec(cls, unassigned, matrix):
        """Solve sudoku matrix using backtracking"""

        if (len(unassigned) == 0):              # If all variables are assigned
            return matrix                       # return full matrix

        var, work_domain = unassigned.popitem() # Choose some unassigned variable
        for value in work_domain:               # iterate over it's work domain
            cls.states_visited += 1
            matrix[var] = value                 # Assign the value to the variable

            if cls.is_consistent(var, matrix):  # Check if the matrix is consistent
                result = cls.backtracking_rec(
                        unassigned=copy.deepcopy(unassigned), matrix=matrix
                )
                if (result is not None):        # Return result if it is not None,
                    return result               # None means, the solution was not found
        matrix[var] = 0                     # unassign the variable and continue
        return None

    @classmethod
    def maintain_arc_consistency(cls, unassigned, matrix):
        return unassigned

    @classmethod
    def filter_work_domain(cls, var, work_domain, matrix):
        for value in copy.copy(work_domain):
            matrix[var] = value
            if (not cls.is_consistent(var, matrix)):
                work_domain.remove(value)
            matrix[var] = 0


    @classmethod
    def filter_work_domains(cls, unassigned, matrix):
        for var, work_domain in unassigned.items():
            cls.filter_work_domain(var, work_domain, matrix)
            if (len(work_domain) == 0):
                return False
        return True
        # return unassigned


    @classmethod
    def get_affected_indices(cls, idx, variables, matrix):
        row_indices = {(idx[0], y) for y in range(matrix.shape[1])}
        col_indices = {(x, idx[1]) for x in range(matrix.shape[0])}

        box_x, box_y = (3 * (idx[0] // 3)), (3 * (idx[1] // 3))
        box_indices = {
                (x, y) for x in range(box_x, box_x + 3)
                        for y in range(box_y, box_y + 3)
        }

        indices = {*row_indices, *col_indices, *box_indices}
        indices.remove(idx)
        return {idx for idx in indices if idx in variables}
        #return {idx: variables[idx] for idx in variables if idx in indices}

    @classmethod
    def inference(cls, indices, value, variables, matrix):
        """
        Remove value from work domains of indices
        If some work domain become empty, return False, solution not possible
        If there is only one value in the domain, propagate it and do inference
        """
        for idx in indices:
            if (idx not in variables):
                continue
            variables[idx].discard(value)   # Remove value form work_domain
            if (len(variables[idx]) == 0):  # Terminate if there is no value left
                return False
            if (len(variables[idx]) == 1):  # Propagate the only possible value
                work_domain = variables.pop(idx)    # Pop work domain form vars
                matrix[idx] = work_domain.pop()     # Pop the only item from it
                if (not cls.is_consistent(idx, matrix)):  # is matrix inconsistent
                    return False
                indices_next = cls.get_affected_indices(idx, variables, matrix)
                if (not cls.inference(indices_next, matrix[idx], variables, matrix)):
                    return False
        return True

    @classmethod
    def backtracking_with_inference_rec(cls, unassigned, matrix):
        if (len(unassigned) == 0):              # If all variables are assigned
            return matrix                       # return full matrix

        idx, work_domain = unassigned.popitem() # Choose some unassigned variable
        for value in work_domain:               # iterate over it's work domain
            cls.states_visited += 1
            matrix_copy = matrix.copy()
            matrix_copy[idx] = value                 # Assign the value to the variable

            if cls.is_consistent(idx, matrix_copy):  # Check if the matrix is consistent
                unassigned_copy = copy.deepcopy(unassigned)
                indices = cls.get_affected_indices(idx, unassigned_copy, matrix_copy)

                if (cls.inference(indices, value, unassigned_copy, matrix_copy)):
                    result = cls.backtracking_with_inference_rec(
                            unassigned=unassigned_copy, matrix=matrix_copy,
                    )
                    if (result is not None):    # Return result if it is not None,
                        return result           # None means, the solution was not found
        return None

    @classmethod
    def maintaining_arc_consistency_rec(cls, unassigned, matrix):
                    # unassigned_copy.update(affected)
                    # consistent = cls.maintain_arc_consistency(
                    #         unassigned_copy, matrix,
                    # )
                    # if (consistent is not None):
        pass

    @classmethod
    def solve(cls, matrix, method, file_meta):
        """Solve sudoku matrix with specified method"""
        start = time.process_time() # Measure CPU time

        unassigned = {
                (i,j): set(range(1, matrix.shape[0] + 1))
                        for i,j in np.argwhere(matrix == 0)
        }

        solution = None
        if (method == 'bt'):
            solution =  cls.backtracking_rec(unassigned, matrix)
        elif (method == 'bti'):
            if (cls.filter_work_domains(unassigned, matrix)):
                solution =  cls.backtracking_with_inference_rec(unassigned, matrix)
        elif (method == 'mac'):
            if (cls.filter_work_domains(unassigned, matrix)):
                solution =  cls.maintaining_arc_consistency_rec(unassigned, matrix)
        else:
            raise NotImplementedError

        elapsed_cpu_time = time.process_time() - start
        if (file_meta is not None):
            print(f'# {cls.states_visited} {elapsed_cpu_time}', file=file_meta)
        return solution


if __name__ == '__main__':
    import argparse
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode')
    parser.add_argument('-m', '--method', default='bti',
            choices=['bt','bti', 'mac', 'bt', 'dbt', 'ddbt'],
            help=('solver method'))
    parser.add_argument('-l', '--logging', nargs='?', const=sys.stdout,
            default=None, type=argparse.FileType('w'),
            help='metadata logging, default option is logging off')
    # Input/Outupt positional arguments
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin,
            help='input file, if not given, stdin is used')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'),
            default=sys.stdout,
            help='output file, if not given, stdout is used')
    args = parser.parse_args()

    if args.debug:
        input_iter = args.input.readlines()
        sys.stdin = open('/dev/tty')
        import pdb; pdb.set_trace()
    else:
        input_iter = args.input

    instance = Sudoku.read_instance(input_iter)

    solution = Sudoku.solve(
            matrix=instance, method=args.method, file_meta=args.logging
    )

    if (solution is not None):
        Sudoku.write_matrix(matrix=solution, file_out=args.output)
