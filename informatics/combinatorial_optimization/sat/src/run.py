import time
from logging import basicConfig, INFO

import cProfile, pstats, io
from pstats import SortKey

from serializer import parse_mwcnf, write_results
from solver import tabu
from traverser import iterate_problem_quadruples


basicConfig(format='%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S',
            level=INFO)

pr = cProfile.Profile()
pr.enable()

for problem_name, problem_file, results_file, times_file in iterate_problem_quadruples():
    weights, variables, negations = parse_mwcnf(problem_file.readlines())
    time_start = time.process_time()
    values, assigned_values = tabu(weights, variables, negations)
    time_elapsed_cpu = time.process_time() - time_start
    write_results(results_file, problem_name, values, assigned_values, times_file, time_elapsed_cpu)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
