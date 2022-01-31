from pathlib import Path
from logging import info

ROOT = Path('.')
DATA_PATH = ROOT / Path('data')
RESULTS_PATH = ROOT / Path('results')
EXTENSION = '.dat'
OPTIMA_SUFFIX = '-opt'

def yield_groups():
    for file in DATA_PATH.glob(f'*{OPTIMA_SUFFIX}*'):
        yield str(Path(file).stem.removesuffix(OPTIMA_SUFFIX))

def yield_group_problems(group):
    suffix = '1'
    for file in DATA_PATH.glob(f'*{group}{suffix}/*'):
        yield str(file)

def get_optima_path(group):
    files = list(DATA_PATH.glob(f'{group}{OPTIMA_SUFFIX}{EXTENSION}'))
    assert len(files) == 1
    return files[0]

def generate_results_path(group):
    return str(RESULTS_PATH / f'{group}-res{EXTENSION}')

def generate_times_path(group):
    return str(RESULTS_PATH / f'{group}-time{EXTENSION}')

def iterate_group_optima_results_times():
    for group in yield_groups():
        optima_path = get_optima_path(group)
        results_path = generate_results_path(group)
        times_path = generate_times_path(group)
        yield group, optima_path, results_path, times_path

def iterate_problem_quadruples(last_index=None):
    for group in sorted(yield_groups(), reverse=False):
        results = generate_results_path(group)
        times = generate_times_path(group)
        files = list(yield_group_problems(group))
        if last_index is None:
            last_index = len(files) - 1

        with open(get_optima_path(group)) as optima_file:
            problem_names = [line.split()[0] for line in optima_file.readlines()]

        with open(results, 'w') as results_file, open(times, 'w') as times_file:
            for file_index, problem_path in enumerate(sorted(files)):
                if file_index > last_index:
                    break

                problem_name = Path(problem_path).stem.removeprefix('w').removesuffix('-A')
                if problem_name not in problem_names:
                    continue

                with open(problem_path) as problem_file:
                    info(f'{group}\t{problem_name}\t({file_index+1}/{last_index+1})')
                    yield problem_name, problem_file, results_file, times_file


if __name__ == '__main__':
    for group in sorted(yield_groups()):
        print(group)

        optima = get_optima_path(group)
        print(f'  {optima}')

        results = generate_results_path(group)
        print(f'  {results}')

        times = generate_times_path(group)
        print(f'  {times}')

        for file in sorted(yield_group_problems(group)):
            print(f'    {file}')
            print(f'    {Path(file).stem}')
            break
