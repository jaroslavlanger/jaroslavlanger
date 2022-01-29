#!/usr/bin/env python3

import sys
import random

n = 5
seed = 42

# Read inputs
if len(sys.argv) > 1:
    n = int(sys.argv[1])
if len(sys.argv) > 2:
    seed = (sys.argv[2])

# Seed randomness
random.seed(seed)

# Read stdin
lines = sys.stdin.readlines()

# Write stdin sample
print(*random.sample(lines, n), sep='', end='')

