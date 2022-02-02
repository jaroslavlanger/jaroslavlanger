from itertools import product
from logging import basicConfig, INFO

import cProfile, pstats, io
from pstats import SortKey

from serializer import parse_mwcnf, write_results
from solver import tabu
from traverser import yield_name_lines_file

basicConfig(format='%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=INFO)

pr = cProfile.Profile()
pr.enable()

# breakpoint()
max_iterations = ['n', 'nlogn', 'nn', 'nnn']
for problem_name, lines, results_path in yield_name_lines_file(max_instances=34):
    weights, variables, negations = parse_mwcnf(lines)
    for neighbors, tenure, reinits in product(['all', 'logn', 'logn_weighted'],
                                              ['n', 'nlogn', 'nn', 'infinity'],
                                              ['0', '1', 'n']):
        measurements = tabu(weights, variables, negations,
                            max_iterations=max_iterations, neighbors=neighbors,
                            tenure=tenure, reinits=reinits)
        write_results(results_path, problem_name, measurements, max_iterations,
                      neighbors, tenure, reinits)

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
