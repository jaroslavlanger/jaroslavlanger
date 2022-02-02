import itertools
from functools import partial
from math import log2, ceil
import time
from typing import NamedTuple
from logging import DEBUG, INFO, info, basicConfig

import numpy as np

from validator import compute_satisfied_x_variables_x_weights, WEIGHTS, VARIABLES, NEGATIONS

INFINITY = float('inf')
RANDOM_GENERATOR = np.random.default_rng(42)

class Measurement(NamedTuple):
    time: float
    best_value: int
    best_assignment: list[bool]

def tabu_core(initial_value, initial_assignment, tabu_tenure, yield_neighbor,
              value_function, times_of_yeild, times_of_reinitialization,
              reinitialize):
    best_value = next_value = initial_value
    best_assignment = next_assignment = initial_assignment
    tabu = {}

    time_start = time.process_time()
    t = 0
    while True:
        for neighbor_assignment in yield_neighbor(np.array(next_assignment)):
            t += 1
            # time_since_available = tabu.get(tuple(neighbor_assignment), 0)
            try:
                time_since_available = tabu[tuple(neighbor_assignment)]
            except:
                time_since_available = 0

            if t in times_of_reinitialization:
                next_assignment = reinitialize()
                next_value = value_function(next_assignment)
            elif t >= time_since_available:
                neighbor_value = value_function(neighbor_assignment)
                if neighbor_value >= next_value:
                    next_value, next_assignment = (neighbor_value,
                                                   np.array(neighbor_assignment))
            if t in times_of_yeild:
                if next_value > best_value:
                    best_value, best_assignment = (next_value, next_assignment)
                seconds_elapsed = time.process_time() - time_start
                yield Measurement(seconds_elapsed, best_value, best_assignment)

                if t == times_of_yeild[-1]:
                    return
            if t in times_of_reinitialization:
                break

        tabu[tuple(next_assignment)] = t + tabu_tenure
        if next_value > best_value:
            best_value, best_assignment = (next_value, next_assignment)
        next_value = initial_value

def yield_neighbor_one_flip(assignment_vector, indices):
    for index in indices:
        before_swap = assignment_vector[index]
        assignment_vector[index] = not before_swap
        yield assignment_vector
        assignment_vector[index] = before_swap

def yield_neighbor_sampled(assignment_vector, length, tries, probabilities):
    indices = RANDOM_GENERATOR.choice(length, tries, p=probabilities)
    yield from yield_neighbor_one_flip(assignment_vector, indices)

def create_yield_neighbor(weights, truncator=None, weighted=False):
    variable_count = len(weights) 
    if truncator is not None:
        tries = ceil(truncator(variable_count))
        probabilities = weights / weights.sum() if weighted else None
        return partial(yield_neighbor_sampled, length=len(weights), tries=tries,
                       probabilities=probabilities)
    else:
        return partial(yield_neighbor_one_flip, indices=range(variable_count))

NEIGHBOR_GENERATOR_FACTORY = {
    'all': create_yield_neighbor,
    'logn': partial(create_yield_neighbor, truncator=log2),
    'logn_weighted': partial(create_yield_neighbor, truncator=log2,
                             weighted=True)
}
NAMED_FUNCTIONS = {
    '0': lambda n: 0,
    '1': lambda n: 1,
    'n': lambda n: n,
    'nlogn': lambda n: n*log2(n),
    'nn': lambda n: n*n,
    'nnn': lambda n: n*n*n,
    'infinity': lambda x: INFINITY,
}

def tabu(weight_vector, variable_matrix, negation_matrix,
         *, max_iterations=('nn',), neighbors='all', tenure='infinity', reinits='0'):
    variable_count = len(weight_vector)
    # reinitialize = partial(np.zeros, variable_count, dtype=bool)
    reinitialize = partial(RANDOM_GENERATOR.choice, [False,True], size=variable_count)
    initial_value = (-INFINITY, -INFINITY)
    initial_assignment = reinitialize()
    tabu_tenure = NAMED_FUNCTIONS[tenure](variable_count)
    yield_neighbor = NEIGHBOR_GENERATOR_FACTORY[neighbors](weight_vector)
    value_function = partial(compute_satisfied_x_variables_x_weights,
                             weight_vector=weight_vector,
                             variable_matrix=variable_matrix,
                             negation_matrix=negation_matrix)
    times_of_yeild = [ceil(NAMED_FUNCTIONS[n](variable_count))
                      for n in max_iterations]
    last_iteration = times_of_yeild[-1]
    ratio = int(last_iteration / (NAMED_FUNCTIONS[reinits](variable_count) + 1))
    times_of_reinitialization = list(range(ratio, last_iteration, ratio))

    return list(tabu_core(initial_value=initial_value,
                          initial_assignment=initial_assignment,
                          tabu_tenure=tabu_tenure,
                          yield_neighbor=yield_neighbor,
                          value_function=value_function,
                          times_of_yeild=times_of_yeild,
                          times_of_reinitialization=times_of_reinitialization,
                          reinitialize=reinitialize))


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
