# IPython

Toolkit to help with using Python interactively.

```
Author: Jaroslav Langer
Date:   2021 Jan 05
```

## Contents

## Introduction

## Magic commands

- [Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

### Cell Magic Functions

- Cell magic functions starts with `%%`, gets the rest of the cell as an argument.

```ipynb
%%time
# Measure cell time
```

### Line Magic Functions

#### Measure execution time

```ipynb
%time function()
# Average run time of multiple executions
%timeit function()
```

#### Debugger

```ipynb
%pdb on
```

