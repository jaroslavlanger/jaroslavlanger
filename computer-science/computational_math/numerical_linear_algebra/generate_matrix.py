#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Matrix Generator for Assignment from NI-MPI course at FIT/CTU Prague.

Author: Jaroslav Langer (langeja5@fit.cvut.cz)
Date:   2021 Jan 04
"""

import numpy as np

def generate_mpi_matrix(gama, shape=(20, 20)):
    """Generate matrix (20, 20) with gama values on the main diagonal.
    On all positions -1, +1 to the main diagonal are values -1. 0 is elsewhere.
    """
    matrix = np.zeros((shape))
    for row in range(matrix.shape[0]):
        gama_pos = row
        for col in range(matrix.shape[1]):
            if (gama_pos == col):
                matrix[row, col] = gama
            if ((col == gama_pos - 1) or (col == gama_pos + 1)):
                matrix[row, col] = -1
    return matrix

def generate_mpi_vector(gama, shape=(20,)):
    vector = np.ndarray(shape)
    for idx in range(vector.shape[0]):
        if ((idx == 0) or (idx == vector.shape[0] - 1)):
            vector[idx] = gama - 1
        else:
            vector[idx] = gama - 2
    return vector

if __name__ == "__main__":
    matrix = generate_mpi_matrix(gama=3)
    # print(matrix)
    vector = generate_mpi_vector(gama=3)
    print(vector)

