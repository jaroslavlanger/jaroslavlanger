#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative Linear System Solver

Author: Jaroslav Langer (langeja5@fit.cvut.cz)
Date:   2021 Jan 04

Implementation of the Jacobi and Gauss-Seidel method for linear system solving.
[Assignment link](https://courses.fit.cvut.cz/NI-MPI/media/grading/2020/ni-mpi-ukol-slr-v1.pdf)

Usage:
    ./langer_mpi.py <method> <gama>

- method:   ['j', 'jacobi'] for Jacobi method.
            ['g', 's', 'gs', 'gauss_seidel'] for Gauss-Seidel method.
- gama:     gama parameter from assignment paper.
"""

import numpy as np

def generate_mpi_matrix(gama, shape):
    """Generate matrix (20, 20) with gama values on the main diagonal.
    On all positions -1, +1 to the main diagonal are values -1. 0 is elsewhere.
    """
    matrix = np.zeros((shape), dtype="double")
    for row in range(matrix.shape[0]):
        gama_pos = row
        for col in range(matrix.shape[1]):
            if (gama_pos == col):
                matrix[row, col] = gama
            if ((col == gama_pos - 1) or (col == gama_pos + 1)):
                matrix[row, col] = -1
    return matrix

def generate_mpi_vector(gama, shape):
    """Generate vector with the first and last element equal to `gama - 1`.
    Other elements equal to `gama - 2`.
    """
    vector = np.ndarray(shape, dtype="double")
    for idx in range(vector.shape[0]):
        if ((idx == 0) or (idx == vector.shape[0] - 1)):
            vector[idx] = gama - 1
        else:
            vector[idx] = gama - 2
    return vector

def jacobi(A, b, epsilon=1e-6, max_iter=1000):
    """Solve linear system using Jacobi method"""

    D = np.diag(np.diag(A))     # Main diagonal values of matrix A, 0 elsewhere
    L = np.tril(A, -1)          # Values under the main diagonal of matrix A
    U = A - L - D               # Values above the main diagonal of matrix A

    inv_D = np.linalg.inv(D)            # Matrix D inverse (precomputed)

    # D inverse multiplied by negative values above and under the main diagonal
    matrix = np.dot(inv_D, (- L - U))
    inv_D_b = np.dot(inv_D, b)          # D inverse multiplied by vector b

    # Convergence check
    W = np.identity(A.shape[0]) - np.dot(inv_D, A)
    rho_W = np.linalg.eigvals(W).max()
    if (rho_W >= 1):
        raise ValueError("The convergence check did not pass:"
            f" rho(W)= {rho_W:.5}, please choose different solver.")
    print(f"rho(W)= {rho_W:.5}")

    norm_b = np.linalg.norm(b)              # Norm of b vector (precomputed)
    x = np.zeros(A.shape[0], dtype="double")# Initialization of x vector
    r = np.dot(A, x) - b                    # First residuum calculated

    norm_r_by_norm_b = np.linalg.norm(r)/norm_b
    print(f"Initial norm(r)/norm(b): {norm_r_by_norm_b}\n")

    step = 0
    while(norm_r_by_norm_b >= epsilon):
        step += 1;
        if step > max_iter:
            raise ValueError(f"Maximum iteration ({max_iter}) exceeded.")
        x = np.dot(matrix, x) + inv_D_b     # Calculate next x
        r = np.dot(A, x) - b                # Calculate next residuum
        norm_r_by_norm_b = np.linalg.norm(r)/norm_b
        print(f"Step: {step: <10} norm(r)/norm(b): {norm_r_by_norm_b}")
    return x

def gauss_seidel(A, b, epsilon=1e-6, max_iter=1000, omega=1):
    """Solve linear system using Gauss–Seidel method"""

    # Convergence check
    if (not (0 < omega < 2)):
        print("WARNING: The convergence check did not pass:"
            f" omega was not in range (0, 2), omega = {omega:.5}")
    if (not (np.allclose(A, A.T, rtol=1e-05, atol=1e-08))):
        print("WARNING: The convergence check did not pass:"
            f" matrix A is not symmetric.")
    if (not (np.all(np.linalg.eigvals(A) > 0))):
        print("WARNING: The convergence check did not pass:"
            f" matrix A is not positive definite.")

    D = np.diag(np.diag(A))     # Main diagonal values of matrix A, 0 elsewhere
    L = np.tril(A, -1)          # Values under the main diagonal of matrix A
    U = A - L - D               # Values above the main diagonal of matrix A

    # Q for `omega=1` equals to A values above the main with inverted sign
    Q = ((1/omega) * D) + L
    inv_Q = np.linalg.inv(Q)    # Matrix Q inverse (precomputed)
    matrix = np.dot(inv_Q, (((1/omega - 1) * D) - U))
    inv_Q_b = np.dot(inv_Q, b)  # Q inverse multiplied by vector b

    norm_b = np.linalg.norm(b)              # Norm of b vector (precomputed)
    x = np.zeros(A.shape[0], dtype="double")# Initialization of x vector
    r = np.dot(A, x) - b                    # First residuum calculated

    norm_r_by_norm_b = np.linalg.norm(r)/norm_b
    print(f"Initial norm(r)/norm(b): {norm_r_by_norm_b}\n")

    step = 0
    while(norm_r_by_norm_b >= epsilon):
        step += 1; 
        if step > max_iter:
            raise ValueError(f"Maximum iteration ({max_iter}) exceeded.")
        x = np.dot(matrix, x) + inv_Q_b     # Calculate next x
        r = np.dot(A, x) - b                # Calculate next residuum
        norm_r_by_norm_b = np.linalg.norm(r)/norm_b
        print(f"Step: {step: <10} norm(r)/norm(b): {norm_r_by_norm_b}")
    return x


if __name__ == "__main__":
    import sys

    methods = {}
    for name in ['j', 'jacobi']:                  methods[name] = jacobi
    for name in ['g', 's', 'gs', 'gauss_seidel']: methods[name] = gauss_seidel

    try:
        method = methods[sys.argv[1].lower()]
    except KeyError:
        raise ValueError(f'Method "{sys.argv[1]}" is not supported.')

    gama = int(sys.argv[2]) if (len(sys.argv) > 2) else 3
    shape = (20, 20)

    # Generate matrix and vector as was told in the assignment paper.
    matrix = generate_mpi_matrix(gama=gama, shape=shape)
    vector = generate_mpi_vector(gama=gama, shape=shape[:1])

    x = method(matrix, vector)
    print("", "Solution:", x, sep="\n") # Print solution vector.

