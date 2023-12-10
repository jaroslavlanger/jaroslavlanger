import pandas as pd
import seaborn as sns
from functools import partial
import matplotlib.pyplot as plt
from datetime import timedelta

from .traverser import (yield_groups,
                        get_optima_path,
                        generate_results_path,
                        generate_times_path)


ITERATION_COLUMNS = ['n', 'nlogn', 'nn', 'nnn']

read_csv = partial(pd.read_csv, sep=' ', header=None, index_col=0)

group = 'wuf20-91-A'
opt = get_optima_path(group)
times = generate_times_path(group)
results = generate_results_path(group)

read_csv(results).sample(5)

def load_main_frame():
    frames = []
    keys = []

    for group in sorted(yield_groups()):
        print(group)
        keys.append(group)

        frames.append(
        # display(
            pd.concat([
                read_csv(generate_times_path(group)).rename({1: 'time'}, axis=1),
                read_csv(get_optima_path(group)).rename({1: 'optimum'}, axis=1)['optimum'],
                read_csv(generate_results_path(group)).rename(
                    {1: 'n', 2: 'nlogn', 3: 'nn', 4: 'nnn'},
                    axis=1)[ITERATION_COLUMNS]
            ], axis=1)#.reset_index().rename({0: 'instance'}, axis=1)
        )

    frame = pd.concat(frames, keys=keys).reset_index().rename(
        {'level_0': 'group', 0: 'instance'}, axis=1)
    return frame

frame = load_main_frame()

def convert_values_to_errors(frame):
    for col in ITERATION_COLUMNS:
        frame[col] = (frame.optimum - frame[col]) / frame.optimum 
    return frame

frame = convert_values_to_errors(frame)

flattened = pd.melt(frame,
        id_vars=['group', 'instance', 'time'],
        value_vars=ITERATION_COLUMNS,
        var_name='max_iteration',
        value_name='relative_error'
       )
