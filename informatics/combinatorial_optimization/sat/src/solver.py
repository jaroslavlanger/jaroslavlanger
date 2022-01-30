import itertools
from functools import partial
from logging import DEBUG, INFO, info, basicConfig

import numpy as np

from validator import compute_satisfied_x_variables_x_weights, WEIGHTS, VARIABLES, NEGATIONS

def tabu(weight_vector, variable_matrix, negation_matrix):
    value_function = partial(compute_satisfied_x_variables_x_weights,
                             weight_vector=weight_vector,
                             variable_matrix=variable_matrix,
                             negation_matrix=negation_matrix)
    tabu = set()
    variable_count = len(weight_vector)
    generator = np.random.default_rng(42)
    # solution vector randomly initialized with an appropriate number of ones.
    assignment_next = generator.choice([0,1], size=variable_count)
    assignment_best = assignment_next.copy()
    value_next = value_best = value_function(assignment_next)
    for t in range(variable_count * 10):
        if value_next > value_best:
            value_best = value_next
            assignment_best = assignment_next.copy()
        assignment_vector = assignment_next
        tabu.add(tuple(assignment_vector))
        value_next = (float('-inf'), float('-inf'))
        assignment_next = assignment_vector.copy()
        for i in range(variable_count):
            before_swap = assignment_vector[i]
            assignment_vector[i] = not before_swap
            if tuple(assignment_vector) not in tabu:
                value_try = value_function(assignment_vector)
                if value_try >= value_next:
                    value_next = value_try
                    assignment_next = assignment_vector.copy()
            assignment_vector[i] = before_swap
    return value_best, assignment_best

def try_all_permutations(weight_vector, variable_matrix, negation_matrix):
    n = len(weight_vector)
    permutations = (np.array(c) for c in itertools.product([0, 1], repeat=n))

    value_function = partial(compute_satisfied_x_variables_x_weights,
                             weight_vector=weight_vector,
                             variable_matrix=variable_matrix,
                             negation_matrix=negation_matrix)
    values_max = max(permutations, key=value_function)
    return value_function(values_max), values_max

def try_n_options(weight_vector, variable_matrix, negation_matrix, n=2000):
    options = np.random.randint(0, 2, (n,len(weight_vector)))
    value_function = partial(compute_satisfied_x_variables_x_weights,
                             weight_vector=weight_vector,
                             variable_matrix=variable_matrix,
                             negation_matrix=negation_matrix)
    values_max = max(options, key=value_function)
    return value_function(values_max), values_max

if __name__ == '__main__':
    basicConfig(level=INFO)
    values_sum, value_vector = try_all_permutations(weight_vector=WEIGHTS,
                                                    variable_matrix=VARIABLES,
                                                    negation_matrix=NEGATIONS)
    info(f'{values_sum=}, {value_vector=}')
    values_sum, value_vector = try_n_options(weight_vector=WEIGHTS,
                                             variable_matrix=VARIABLES,
                                             negation_matrix=NEGATIONS)
