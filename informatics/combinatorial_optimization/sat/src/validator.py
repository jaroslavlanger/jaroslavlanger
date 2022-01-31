#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validates SAT formula with weights.
(x1 + ¬x3 + x4).(¬x1 + x2 + ¬x3).(x3 + x4).(x1 + x2 + ¬x3 + ¬x4).(¬x2 + x3).(¬x2' + ¬x4')
"""
import numpy as np
from logging import basicConfig, debug, info, INFO

WEIGHTS = np.array([2, 4, 1, 6])

VARIABLES = np.array([
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
],
                     dtype=bool)

NEGATIONS = np.array([
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
],
                     dtype=bool)

VALUE_VECTORS = [
    np.array([0, 0, 0, 0], dtype=bool),
    np.array([0, 0, 0, 1], dtype=bool),
    np.array([1, 0, 0, 1], dtype=bool),
    np.array([1, 1, 1, 0], dtype=bool),
]

def compute_satisfied_x_variables_x_weights(value_vector,
                                            weight_vector,
                                            variable_matrix,
                                            negation_matrix):
    # debug(f'{value_vector=}')

    assigned_matrix = variable_matrix * value_vector
    # debug(f'{assigned_matrix=}')

    negated_matrix = np.logical_xor(assigned_matrix, negation_matrix)
    # debug(f'{negated_matrix=}')

    columns_or_vector = np.logical_or.reduce(negated_matrix, 1)
    # debug(f'{columns_or_vector=}')

    satisfied = np.logical_and.reduce(columns_or_vector)
    # debug(f'{satisfied=}')

    weight_sum = weight_vector.dot(value_vector)
    # debug(f'{weight_sum=}')

    result = satisfied * weight_sum
    # if result != 0:
    #     debug(f'{result} {value_vector.astype(int)}')

    return result, columns_or_vector.sum()

if __name__ == '__main__':
    basicConfig(level=INFO)
    for value_vector in VALUE_VECTORS:
        res = compute_satisfied_x_variables_x_weights(value_vector=value_vector,
                                                      weight_vector=WEIGHTS,
                                                      variable_matrix=VARIABLES,
                                                      negation_matrix=NEGATIONS)
        info(res)
