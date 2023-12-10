#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:       Linear System Solver Prototype
Author:     Jaroslav Langer (langeja5@fit.cvut.cz)
Date:       2020, Dec. 14th
Version:    0.1
    Description:
Python prototype solution to the first assignment from nonlinear optimization.
The code will be rewritten to the c/c++, so the code will not be pythonic, because it should not be.
    Version description:
The gradient descent method is implemented with single function for every linear algebra operation.
Value `rTr` is calculated twice (once for next norm r `nr`, second the `a`).
"""

import sys
from math import sqrt

EPSILON = 0.0001

def read_matrix(matrix, m_file):
    """Read 1+n lines from given file, n is read from the first line.
    Write n rows of n floats to the matrix."""

    n = 0
    with open(m_file, "r") as f:
        first_line = f.readline()
        n = int(first_line); print(n)
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

def add_vector_vector(v_1, v_2):
    v = v_1.copy()
    for i in range(len(v_1)):
        v[i] = v_1[i] + v_2[i]
    return v

def subtract_vector_vector(v_1, v_2):
    v = v_1.copy()
    for i in range(len(v_1)):
        v[i] = v_1[i] - v_2[i]
    return v

def multiply_scalar_vector(s, v):
    x = v.copy()
    for i in range(len(v)):
        x[i] = s * v[i]
    return x

def multiply_vector_t_vector(x_1_t, x_2):
    x = 0
    for i in range(len(x_1_t)):
        x += x_1_t[i]*x_2[i]
    return x

def multiply_matrix_vector(m, v):
    x = [0 for row in m]            # shape (n,)
    for i in range(len(m)):         # iterate over rows
        for j in range(len(m[0])):  # iterate over columns
            x[i] += m[i][j] * v[j]
    return x

def norm(v):
    nn = 0
    for i in range(len(v)):
        nn += v[i]*v[i]
    return sqrt(nn)

def gradient_descent(A, b, x, verbose):
    i = 0 # step
    r = [x for x in b]
    while (True):
        Ar   = multiply_matrix_vector(A, r)    # Helper
        rTr  = multiply_vector_t_vector(r, r)  # Helper
        rTAr = multiply_vector_t_vector(r, Ar) # Helper

        a =  rTr / rTAr

        ar   = multiply_scalar_vector(a, r)    # Helper
        aAr  = multiply_scalar_vector(a, Ar)   # Helper

        x = add_vector_vector(x, ar)
        r = subtract_vector_vector(r, aAr)

        nr = norm(r);
        if verbose: print(f'step: {i: <8} | residuum: {nr:.5}'); i += 1
        if (nr < EPSILON): break
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

