#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np
from logging import debug

def parse_variable_and_negation(shape, lines):
    variable_matrix = np.zeros(shape, dtype=bool)
    negation_matrix = np.zeros(shape, dtype=bool)
    clauses = [[int(c) for c in row.split()] for row in lines]

    debug(f'{len(clauses)=}, {shape[0]=}')
    assert len(clauses) == shape[0]
    assert all(clause[-1] == 0 for clause in clauses)
    assert all((0 < number <= shape[1] for number in clause) for clause in clauses)

    for clause_index, clause in enumerate(clauses):
        for variable_number in clause[:-1]:
            variable_index = abs(variable_number) - 1
            variable_matrix[clause_index][variable_index] = True
            if variable_number < 0:
                negation_matrix[clause_index][variable_index] = True
    return variable_matrix, negation_matrix

def output_check(variable_count, clause_count, weight_vector, variable_matrix, negation_matrix):
    assert len(weight_vector) == variable_count
    assert variable_matrix.shape == negation_matrix.shape == (clause_count, variable_count)

def parse_mwcnf(lines: list):
    for line_number, line in enumerate(lines):
        debug(line)
        segments = line.split()
        if (first := segments[0]) == 'c':
            continue
        elif first == 'p':
            variable_count = int(segments[2]) 
            clause_count = int(segments[3]) - 1
        elif first == 'w':
            assert segments[-1] == '0'
            weight_vector = np.array([int(i) for i in segments[1:-1]])
        else:
            variable_matrix, negation_matrix = (
                parse_variable_and_negation((clause_count, variable_count),
                                            lines[line_number:]))
            break
    output_check(variable_count, clause_count, weight_vector, variable_matrix, negation_matrix)
    debug('weight_vector=%s', weight_vector)
    debug('variable_matrix=%s', variable_matrix)
    debug('negation_matrix=%s', negation_matrix)
    return weight_vector, variable_matrix, negation_matrix


def write_results(results_path, problem_name, measurements, max_iterations, *args):
    lines = []
    for measurement, max_iteration in zip(measurements, max_iterations):
        variables = (str(i) if value else str(-i)
                     for i, value in enumerate(measurement.best_assignment, start=1))
        lines.append(' '.join([problem_name, max_iteration, *args,
                               str(measurement.time),
                               str(measurement.best_value[0]), *variables]))

    with open(results_path, 'a') as results_file:
        print(*lines, sep='\n', file=results_file)

if __name__ == '__main__':
    with open(sys.argv[1]) as problem_file:
        weights, variables, negations = parse_mwcnf(problem_file.readlines())
