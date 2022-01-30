"""
def iterate_problem_quadruples():
    problem_name = 'wuf20-02'
    problem_path = 'data/wuf20-78-M1/wuf20-02.mwcnf'
    results_path = 'results/wuf20-78-M-res.dat'
    times_path = 'results/wuf20-78-M-time.dat'
    with open(problem_path) as problem_file, open(results_path, 'w') as results_file, open(times_path, 'w') as times_file:
        yield problem_name, problem_file, results_file, times_file
"""
import os

def iterate_problem_quadruples():
    for root, dirs, files in os.walk('data'):
        names_to_leave_out = [name for name in dirs if ('20-' not in name and '50-' not in name)]
        for name in names_to_leave_out:
            dirs.remove(name)
        dirs.sort()

        if '/' not in root:
            continue
        # 'data/{}1'
        # problem_group = 'wuf20-78-M'
        data, group = root.split('/')
        problem_group = group[:-1] if group[-1] == '1' else group
        results_path = f'results/{problem_group}-res.dat'
        times_path = f'results/{problem_group}-time.dat'
        with open(results_path, 'w') as results_file, open(times_path, 'w') as times_file:
            for file_index, file_path in enumerate(sorted(files)):
                problem_path = os.path.join(root, file_path)
                print(file_index, problem_path)
                # problem_name = 'wuf20-02'
                problem_name, ext = file_path.split('.mwcnf')
                with open(problem_path) as problem_file:
                    yield problem_name, problem_file, results_file, times_file

                if file_index >= 99:
                    break

if __name__ == '__main__':
    for t in iterate_problem_quadruples():
        print(t)
