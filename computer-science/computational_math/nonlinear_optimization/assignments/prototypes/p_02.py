#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:       Linear System Solver Prototype
Author:     Jaroslav Langer (langeja5@fit.cvut.cz)
Date:       2020, Dec. 15th
Version:    0.2
    Description:
The final python prototype solution to the first assignment
from nonlinear optimization course.
The code will be rewritten to the c/c++, so the code will not be pythonic,
because it should not be.
C version of this code should be the optimal solution to this problem.
"""

import sys
from math import sqrt

EPSILON = 0.00001

def read_matrix(matrix, m_file):
    """Read 1+n lines from given file, n is read from the first line.
    Write n rows of n floats to the matrix."""

    n = 0
    with open(m_file, "r") as f:
        first_line = f.readline()
        n = int(first_line);
        for i in range(n):
            line = f.readline()
            matrix.append([float(x) for x in line.split()])
    return n

def read_vector(vector, n, v_file):
    """Read vector of a length n from given file."""

    with open(v_file, "r") as f:
        for i, line in enumerate(f.readlines()):
            if (i == n): break
            vector.append(float(line))
    return None

def next_r_norm_alpha_Ar(r, A):
    rTr  =  0
    Ar   = [0 for x in r]
    rTAr =  0
    for i in range(len(A)):                     # iterate over rows
        for j in range(len(A[0])):              # iterate over columns
            Ar[i] += A[i][j] * r[j]
        rTr  += r[i]  * r[i]
        rTAr += Ar[i] * r[i]
    return (sqrt(rTr), (rTr / rTAr), Ar)        # (r_norm, alpha, Ar)

def next_x(x, alpha, r):
    x_1 = [0 for i in x]
    for i in range(len(x_1)):
        x_1[i] = x[i] + (alpha * r[i])
    return x_1

def next_r(r, alpha, Ar):
    r_1 = [0 for i in r]
    for i in range(len(r_1)):
        r_1[i] = r[i] - (alpha * Ar[i])
    return r_1

def gradient_descent(A, b, x, verbose):
    k = 0
    r = [x for x in b]
    while (True):
        # r_norm:  || r_k || = sqrt( r_k^T * r_k )
        # alpha:   alpha_k = (A * r_k) / (r_k^T * A * r_k)
        # Ar:      A * r_k
        r_norm, alpha, Ar = next_r_norm_alpha_Ar(r, A)

        if (r_norm < EPSILON): print(r_norm); break # || r_k || < epsilon

        x = next_x(x, alpha, r)  # x_{k+1} = x_k + (alpha_k * r_k)
        r = next_r(r, alpha, Ar) # r_{k+1} = r_k - (alpha_k * A * r_k)

        if verbose: print(f'step: {k: <8} | residuum: {r_norm:.5}'); k += 1
    return x


if __name__ == "__main__":
    verbose = False

    method = "gd"       # gradient descent method
    saving = "full"     # saved as 2D array
    n = None            # number of entries
    A = matrix = None   # Matrix A initialization
    b = vector = []     # Vector b initialization
    x = []

    if len(sys.argv) < 4:
        print(f"Error: Three input parameters are required, {len(sys.argv)-1} were given.")
        sys.exit(1)                             # return 1
    f_matrix = sys.argv[1]
    f_vector = sys.argv[2]
    f_output = sys.argv[3]
    if len(sys.argv) > 4: method = sys.argv[4]  # set method
    if len(sys.argv) > 5: saving = sys.argv[5]  # set matrix saving method
    if len(sys.argv) > 6: verbose = sys.argv[6] # show task, steps and solution

    if saving == "full":
        A = []
        n = read_matrix(A, sys.argv[1])
        read_vector(b, n, sys.argv[2])

    if verbose: print(A, b, sep='\n\n', end='\n\n')

    if method == "gd":
        for i in range(n): x.append(0)  # Initialize vector x
        x = gradient_descent(A, b, x, verbose)

    if verbose: print('\nsolution:', x)
    with open(f_output, mode="w") as f_out:
        f_out.write('\n'.join([str(xx) for xx in x]))
        f_out.write('\n')

    sys.exit(0) # return 0

