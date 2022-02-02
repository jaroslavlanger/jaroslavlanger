#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knapsack 0/1 Tabu Search Prototype

Author:     Jaroslav Langer
Modified:   2021 Feb 02
"""

import sys
import math
import numpy as np
import time


class Instance():
    """Knapsack 0/1 instance class."""

    id =    None             # id of the problem
    n =     None             # number of items
    cpty =  None             # weight capacity
    items = None             # items matrix [[weights], [values]]

    def __init__(self, inst_id, n, cpty, items):
        self.id = inst_id
        self.n = n
        self.cpty = cpty
        self.items = items
        self.total_weight = self.items[0].sum()
        self.total_value = self.items[1].sum()

    def __repr__(self):
        return (f'<class Instance: '
                f'id={self.id}, n={self.n}, cpty={self.cpty},\n'
                f'items={self.items}>')

    @classmethod
    def read_instances(cls, lines):
        """Yield knapsack instances from standard input."""

        for line in lines:
            numbers = [int(x) for x in line.split()]
            inst_id = numbers[0]                            # instance id
            n = numbers[1]                                  # number of items
            cpty = numbers[2]                               # capacity
            items = np.array([
                    [numbers[i] for i in range(3, 3+2*n-1, 2)], # weights
                    [numbers[i] for i in range(4, 3+2*n, 2)]])  # values
            yield Instance(inst_id=inst_id, n=n, cpty=cpty, items=items)


class Solution():
    """
    Knapsack solution class.

    It should contain reference to the problem instance.
    Value represents the sum of item values.
    State vector represents what items are included into the solution.
    """

    inst = None
    state = None
    value = None
    total_eval = None

    def __init__(self, inst, state=None, value=None, total_eval=0):
        self.inst = inst
        self.state = state
        self.value = value
        self.total_eval = total_eval

    def __repr__(self):
        return (f'<class Solution: inst.id={self.inst.id},'
                f'value={self.value}, total_eval={self.total_eval}\n'
                f'state={self.state}>')

    @classmethod
    def get_random(cls, inst):
        """
        Get random solution, the number of items is proportional
        to the ratio of capacity to the sum of the items' weight.
        """

        one_prob = min((inst.cpty / inst.total_weight), 1)

        rand_gen = np.random.default_rng(42)
        # solution vector randomly initialized with an appropriate number of ones.
        state_rand = rand_gen.choice([0,1], size=inst.n, p=[1-one_prob, one_prob])
        soln_rand = Solution(inst=inst, state=state_rand)
        soln_rand.value = soln_rand.eval_state()

        return soln_rand

    def copy(self):
        """Return solution copy."""

        return Solution(inst=self.inst, value=self.value, state=self.state.copy())

    def assign(self, soln):
        """Assign value and state from a solution of the same instance."""

        if (self.inst is soln.inst):
            self.state = soln.state.copy()
            self.value = soln.value
        else:
            raise AttributeError('Assign called over different instances.')

    def eval_state(self, inst=None):
        """
        Evaluate knapsack state.

        Return total value.
        Return -1 if the total weight exceeds knapsack's capacity.
        """
        inst = inst if (inst is not None) else self.inst

        weight, value = list(np.dot(inst.items, self.state))
        self.total_eval += 1
        return value if (weight <= inst.cpty) else inst.cpty - weight

    def write_down(self, output):
        print(self.inst.id, self.inst.n, self.value, *self.state, end=' \n',
                file=output)


class Solver():
    """Knapsack 0/1 solver class."""

    @classmethod
    def tabu(cls, inst, max_iter, tabu_tenure, meta_file):
        """
        Solve knapsack instance using Tabu search.
        1) Randomly initialize first solution vector.
          - Number of ones is proportional to the average number of items that fits
        """

        tabu_dict = {}  # (swap_idx, item_value, value_prev, soln_tmp.value)
        max_iter = math.ceil(max_iter(inst.n))
        tabu_tenure = math.ceil(tabu_tenure(inst.n))
        log_metadata = True if (meta_file is not None) else False
        solutions_evaluated = 0     # Measure evaluate solutions
        start = time.process_time() # Measure CPU time

        step = 0
        soln_tmp = Solution.get_random(inst) # First solution is randomized
        key_tmp = None
        soln_next = Solution(inst=inst, value= - inst.total_weight - 1)
        key_next = None
        soln_best = Solution(inst=inst, value=0,
                state=np.zeros(inst.n, dtype='i4'))
        if log_metadata:
            print(inst.id, inst.n, soln_tmp.value, file=meta_file, end=' ')

        for step in range(1, max_iter + 1): # Iterate until max_iteration
            value_prev = soln_tmp.value     # Previous iteration value

            # Iterate over all items, find the best transition
            for swap_idx in range(inst.n):

                # Remember item's value, swap it and evaluate the swap
                item_prev = soln_tmp.state[swap_idx] # Remember previous value
                item_tmp = (item_prev + 1) % 2
                soln_tmp.state[swap_idx] = item_tmp  # Swap item's value
                soln_tmp.value = soln_tmp.eval_state()  # Evaluate solution

                key_tmp = (         # Create a key describing the transition
                        swap_idx,       # Index of the item swapped
                        item_prev,      # Previous item value
                        value_prev,     # Previous knapsack value
                        soln_tmp.value, # Next knapsack value
                )
                key_back = (swap_idx, item_tmp, soln_tmp.value, value_prev)

                # Check whether forward and backward transitions are not tabu
                if ((tabu_dict.get(key_tmp, step - 1) < step)
                        and (tabu_dict.get(key_back, step - 1) < step)):
                    if (soln_tmp.value > soln_next.value):
                        soln_next.assign(soln_tmp) # assign next solution
                        key_next = key_tmp         # assign next transition key
                    if (soln_tmp.value > soln_best.value):
                        soln_best.assign(soln_tmp) # assign best solution

                # Recover the temporary solution for other swap indices
                soln_tmp.state[swap_idx] = item_prev # Previous item value
                soln_tmp.value = value_prev          # Previous knapsack value

            # Assign next solution to temporary solution, add it to the tabu list
            soln_tmp.assign(soln_next)                  # Assign next solution
            soln_next.value = (- inst.total_weight) - 1 # Make any other better 

            tabu_dict[key_next] = step + tabu_tenure # Tabu forward transition

            if log_metadata:
                print(soln_tmp.value, file=meta_file, end=' ')

        if log_metadata:
            elapsed_cpu_time = time.process_time() - start
            print(soln_tmp.total_eval, len(tabu_dict), elapsed_cpu_time,
                    file=meta_file)

        return soln_best

def get_math_function(func_str, math_funcs):
    if ('div' in func_str):
        return lambda n: n / float(func_str.split('div')[-1])
    elif ('^' in func_str):
        return lambda n: n ** float(func_str.split('^')[-1])
    elif ('pwr' in func_str):
        return lambda n: n ** float(func_str.split('pwr')[-1])
    else:
        return math_funcs.get(func_str, lambda n: float(func_str))

if __name__ == '__main__':
    import argparse
    math_funcs = {
            'n':        lambda n: n,
            'sqrt':     math.sqrt,
            'cbrt':     lambda n: n ** (1 / 3),
            'log2':     math.log2,
            'log':      math.log,
            'log10':    math.log10,
    }
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode')
    parser.add_argument('-m', '--max_iter', default='n',
            help=('maximum number of iterations declared by number or function'
                    ', by default "n", other possible functions are: '
                    f'{list(math_funcs.keys())}'))
    parser.add_argument('-t', '--tabu_tenure', default='sqrt',
            help=('length of a tabu tenure declared by number or function, '
                    'by default "sqrt"'))
    parser.add_argument('-w', '--metadata', type=argparse.FileType('w'),
            help='file for metadata to be written')
    # Input/Outupt positional arguments
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin,
            help='input file, if not given, stdin is used')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'),
            default=sys.stdout,
            help='output file, if not given, stdout is used')
    args = parser.parse_args()

    if args.debug:
        input_iter = args.input.readlines()  # lines = sys.stdin.readlines()
        sys.stdin = open('/dev/tty')
        import pdb; pdb.set_trace()
    else:
        input_iter = args.input

    for inst in Instance.read_instances(input_iter):
        solution = Solver.tabu(inst=inst, meta_file=args.metadata,
                max_iter=get_math_function(args.max_iter, math_funcs),
                tabu_tenure=get_math_function(args.tabu_tenure, math_funcs))
        solution.write_down(args.output)

