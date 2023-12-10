#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
print(' Input matrix '.center(79, '-'), '\n', sep='')

mat = '''15 0 -4 3 -2 1 0 0 0 0 -4 0
0 23 3 -6 -1 4 0 0 0 0 0 -19
-4 3 15 0 -4 0 -2 -1 -4 -3 -2 1
3 -6 0 23 0 -19 1 4 -3 -6 -1 4
-2 -1 -4 0 15 0 -4 3 -2 1 -4 -3
1 4 0 -19 0 23 3 -6 -1 4 -3 -6
0 0 -2 1 -4 3 7 -3 -2 -1 0 0
0 0 -1 4 3 -6 -3 11 1 -9 0 0
0 0 -4 -3 -2 -1 -2 1 7 3 0 0
0 0 -3 -6 1 4 -1 -9 3 11 0 0
-4 0 -2 -1 -4 -3 0 0 0 0 15 0
0 -19 1 4 -3 -6 0 0 0 0 0 23'''

print(*mat.split('\n'), sep='\n')

#------------------------------------------------------------------------------
print('\n', ' Compressed row matrix (one line one value) '.center(79, '-'),
    '\n', sep='')

a = []
ci = []
adr = []

a_len = 0
n = 0       # Number of rows (columns)

for i, line in enumerate(mat.split('\n')):
    adr.append(a_len)
    n += 1
    for j, num in enumerate(line.split()):
        number = float(num)
        #number = int(num)
        if (number != 0):
            a.append(number)
            ci.append(j)
            a_len += 1

row = 0
next_row_idx = adr[row + 1]

print(n, a_len)

for idx in range(a_len):
    if(idx == next_row_idx):
        row += 1
        next_row_idx = adr[row + 1] if (row + 1 < n) else 0
    # print(f"row {row} col {ci[idx]} val {a[idx]}")
    print(f"\t{row}\t{ci[idx]}\t{a[idx]}")

#------------------------------------------------------------------------------
print('\n', ' Compressed row matrix '.center(79, '-'), '\n', sep='')

# row_idx = 0
# next_col_idx = row_idx + 1

# print('{', end='')                                     # wolfram alpha format
for i in range(n):
    row_idx = adr[i]                # index of the first column at the i-th row

    next_col_idx = row_idx
    next_col = ci[next_col_idx]     # next column index at the i-th row
    # print('{', end='')                                 # wolfram alpha format
    for j in range(n):
        if (j == next_col):
            print(a[next_col_idx], end=' ')
            # if (j + 1 < n):                            # wolfram alpha format
            #     print(a[next_col_idx], end=', ')       # wolfram alpha format
            # else:                                      # wolfram alpha format
            #     print(a[next_col_idx], end='')         # wolfram alpha format
            next_col_idx += 1
            next_col = ci[next_col_idx] if (next_col_idx < a_len) else 0
        else:
            print('X', end=' ')
            # if (j + 1 < n):                            # wolfram alpha format
            #     print('0', end=', ')                   # wolfram alpha format
            # else:                                      # wolfram alpha format
            #     print('0', end='')                     # wolfram alpha format
    print()
    # print('},') if (i + 1 < n) else print('}', end='') # wolfram alpha format
# print('}')                                             # wolfram alpha format

#------------------------------------------------------------------------------
print('\n', ' Vector '.center(79, '-'), '\n', sep='')

vector = '''
3
0
2
1
-4
-6
-3
11
-2
-9
0
0'''

v = [float(f) for f in vector.split()]
#v = [int(f) for f in vector.split()]
print(*v, sep='\n')

# print('{', end='')                                      # wolfram alpha format
# for j in range(len(v)):
#     print('{', end='')                                  # wolfram alpha format
#     print(v[j], end='')                                # wolfram alpha format
#     print('},') if (j + 1 < n) else print('}', end='')  # wolfram alpha format
# print('}')                                              # wolfram alpha format

#------------------------------------------------------------------------------
print('\n', ' Multiply matrix with vector '.center(79, '-'), '\n', sep='')

Av = [0 for f in v]

row = 0
next_row_idx = adr[row + 1]

for idx in range(a_len):
    if(idx == next_row_idx):
        row += 1
        next_row_idx = adr[row + 1] if (row + 1 < n) else 0
    Av[row] += a[idx] * v[ci[idx]]

print(Av)

#------------------------------------------------------------------------------
print('\n', ' Solution '.center(79, '-'), '\n', sep='')

print('''
42
-20
64
247
-34
-263
-46
235
-21
-241
17
54'''.split())

