# Sudoku

`2021 Feb 08, Jaroslav Langer`

## Sample usage

```sh
# Solve the sudoku from assignment
./sudoku_solver.py < data/tutorial_example.txt

# See all the options
./sudoku_solver.py --help

# Solve sudoku and compare it with prepared solution
./sudoku_solver.py < data/instances/s02a.txt | diff data/solutions/s02a_s.txt - | cat -t
```

## Contents

<!-- TOC GFM -->

* [Introduction and Problem Definition](#introduction-and-problem-definition)
    * [Sudoku Defined As a Constraint Satisfaction Problem](#sudoku-defined-as-a-constraint-satisfaction-problem)
    * [Sudoku Example](#sudoku-example)
* [Algorithms Description](#algorithms-description)
    * [Backtracking (BT)](#backtracking-bt)
    * [Maintaining Arc-Consistency (MAC-BT)](#maintaining-arc-consistency-mac-bt)
    * [Backjumping (BJ)](#backjumping-bj)
    * [Dynamic backtracking (DBT)](#dynamic-backtracking-dbt)
    * [Dependency Directed Backtracking (DDBT)](#dependency-directed-backtracking-ddbt)
* [Datasets](#datasets)

<!-- /TOC -->

## Introduction and Problem Definition

Sudoku is a number-placement puzzle. There are more versions of this game, here will be presented the most common one. You are given matrix $M$, $M \in \{0,1,2,3,4,5,6,7,8,9\}^{9,9}$ (the $0$ can be represented in various ways such as empty space, or any other symbol). The goal is to create matrix $M'$ where following conditions are satisfied: 

1) $\forall i,j \in \{1,2, \dots, 9\},\quad M_{i,j} \neq 0 \iff M_{i,j} = M'_{i,j}$
2) $\forall i \in \{1,2, \dots, 9\},\quad |\{m: m \in M_{i,:}\}| = 9$
3) $\forall j \in \{1,2, \dots, 9\},\quad |\{m: m \in M_{:,j}\}| = 9$
4) $\forall k,l \in \{1,2,3\},\quad |\{m: m \in M_{k+3n,l+3o},\quad \forall n,o \in \{0,1,2\} \}| = 9$

The mathematical definition will be handy for the algorithm. More human-friendly definition offers perhaps [Wikipedia's sudoku](https://en.wikipedia.org/wiki/Sudoku).

### Sudoku Defined As a Constraint Satisfaction Problem

Let's define sudoku as a Constraint Satisfaction Problem to be able to use classical CSP algorithms such as Backtracking or Backjumping.

Sudoku in terms of CSP is an tuple $(X, D, C)$, where

* $X = \{(a,b): \forall a,b \in \{1,2,3,4,5,6,7,8,9\}\}$, i.e. $X$ is a set of variables, in this case the variables are the indices of matrix $M$ defined above.
* $D = \{1,2,3,4,5,6,7,8,9\}$
* $C = \{allDifferent(S)\}$, where $S$ is a set of $27$ sets. $9$ sets are from all row variables, $9$ sets are from the column variables and $9$ sets are from variables of the $3 \times 3$ continuous non-overlapping boxes. Defined in the fourth condition above.

### Sudoku Example

Following is an example of a sudoku instance. Every number is followed with one senseless symbol (can be anything). Here are zeros represented with space character `' '`. Both lines starting with a hash symbol `#` and empty lines are ignored.

```txt
5 3  |  7  |     |
6    |1 9 5|     |
  9 8|     |  6  |
#----+-----+------
8    |  6  |    3|
4    |8   3|    1|
7    |  2  |    6|
#----+-----+------
  6  |     |2 8  |
     |4 1 9|    5|
     |  8  |  7 9|
```

## Algorithms Description

I believe the easiest way to explain an algorithm is to show the pseudocode first.

```py
# Python Sudoku Solver Pseudocode

def backtracking_rec(unassigned, matrix):
    if (len(unassigned) == 0):              # If all variables are assigned
        return matrix                       # return full matrix

    var, work_domain = unassigned.popitem() # Choose some unassigned variable
    for value in work_domain:               # iterate over it's work domain
        matrix[var] = value                 # assign the value to the variable

        if is_consistent(var, matrix):      # Check if the matrix is consistent
            result = backtracking_rec(deepcopy(unassigned), matrix=matrix)

            if (result is not None):        # Return result if it is not None,
                return result               # None means, the solution was not found
        matrix[var] = 0                     # unassign the variable and continue
    return None                 # None of later assignments lead to a solution

def backtracking(matrix):
    unassigned = indices_of_zero_values(matrix)
    solution =  backtracking_rec(unassigned, matrix)
```

### Backtracking (BT)

The backtracking algorithm tries to propagate every solution as long as it is possible. If happens that it is not possible to assign any variable, because all assignments are makes the solution be inconsistent (break some rule), than the lastly assigned variable is unassigned and the propagation continues.

### Maintaining Arc-Consistency (MAC-BT)

MAC-BT algorithm works the same way as the backtracking algorithm with one more feature. Before a solution is propagated, every variable of a every work domain is checked if it has an support over the other work domains of all the other variables. In other words if there is a value 3 in some work domain, it checks if it is possible to assign the value 3 to the variable that it does not make any other variable automatically inconsistent.

### Backjumping (BJ)

Backjumping is a different approach to the returns. While the backtracking goes always one level up (unassigns the lastly assigned variable) and at the level it tries all the variables, backjumping does this differently. Besides the partial solution it returns a conflict set, i.e. set of variables that down the road causes an inconsistency, if the variable of the return is not in the conflict set, it is useless to try all the different values, because the inconsistency will stay. In such a case the backjumping does not alternate the variable values and goes up until the variable is in the conflict set. Then it tries the other values.

### Dynamic backtracking (DBT)

### Dependency Directed Backtracking (DDBT)

## Datasets

For the algorithm functionality checks I download sudoku sets from [Sudoku research page (Timo Mantere & Janne Koljonen, University of Vaasa](http://lipas.uwasa.fi/~timan/sudoku/) there are instances and solutions in the data folder. I used their formatting so it is easily comparable. The files are from windows system, so the code returns files with `'\r\n'` newlines.

