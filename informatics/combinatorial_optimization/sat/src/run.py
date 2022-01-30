import time
from logging import info

from serializer import parse_mwcnf, write_results
from solver import tabu
from traverser import iterate_problem_quadruples

for problem_name, problem_file, results_file, times_file in iterate_problem_quadruples():
    weights, variables, negations = parse_mwcnf(problem_file.readlines())
    time_start = time.process_time()
    value, value_vector = tabu(weights, variables, negations)
    time_elapsed_cpu = time.process_time() - time_start
    write_results(results_file, problem_name, value, value_vector, times_file, time_elapsed_cpu)
    info(f'{problem_name}, {time_elapsed_cpu}')
