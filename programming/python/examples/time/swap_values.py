#!/usr/bin/env python3
"""
CPU Time Measurements
"""
import sys
import time

iterator = range(int(1e8))

start = time.process_time()

if len(sys.argv) == 1:
    # No swapping to see the iteration impact alone
    for i in iterator:
        b = i % 2

elif sys.argv[1] == 't':
    # Swap values using ternary conditional
    for i in iterator:
        b = i % 2
    
        b = 0 if (i == 1) else 1

elif sys.argv[1] == 'm':
    # Swap values using modular arithmetic
    for i in iterator:
        b = i % 2
    
        b = (b + 1) % 2

else:
    print('ERROR')

print(time.process_time() - start)
