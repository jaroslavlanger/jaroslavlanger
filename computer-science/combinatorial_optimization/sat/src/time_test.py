import numpy as np
import itertools
import time

permutations = (np.array(c) for c in itertools.product([0, 1], repeat=20))

start = time.process_time() # Measure CPU time

for count, value_vector in enumerate(permutations):
    if count % 100000 == 0:
        print(count)
elapsed_cpu_time = time.process_time() - start

print(elapsed_cpu_time)
