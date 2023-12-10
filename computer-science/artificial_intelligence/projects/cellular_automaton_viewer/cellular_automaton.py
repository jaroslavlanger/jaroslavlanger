#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cellular Automata Recorder

2021 Feb 11, Jaroslav Langer
"""

import sys
import numpy as np
from matplotlib import pyplot as plt

class CellularAutomaton:


    @classmethod
    def make_step(cls, row, rules):
        next_row = np.empty(shape=row.shape, dtype='u1')
        for idx in range(row.shape[0]):
            if (idx == 0):
                next_row[idx] = rules[tuple([[row[-1]], [row[0]], [row[1]]])]
            elif (idx == row.shape[0] - 1):
                next_row[idx] = rules[tuple([[row[-2]], [row[-1]], [row[0]]])]
            else:
                next_row[idx] = rules[tuple([int(i)] for i in row[idx-1:idx+2])]
        return next_row


    @classmethod
    def compute(cls, rule, init, steps):
        rules = np.reshape(
                [int(binary) for binary in f'{rule:08b}'[::-1]],
                newshape=(2,2,2),
        )

        shape = (steps - 1, steps * 2 - 1)
        if (init  == 'dot'):
            history = np.zeros(shape, dtype='u1')
            history[0][history.shape[1]//2] = 1
        else:
            history = np.reshape(
                    np.random.binomial(1, 0.5, size=(shape[0] * shape[1])),
                    newshape=shape,
            )

        for next_idx, row in enumerate(history[ : - 1], start=1):
            history[next_idx] = cls.make_step(row, rules)
        return history


    @classmethod
    def save(cls, matrix, file_template, rule='', steps=''):
        image = np.array(
                [[255 * (not item)] * 3 for row in matrix for item in row],
                dtype='u1')
        image = image.reshape((*matrix.shape, 3))

        file_name = file_template.format(rule=rule, steps=steps, extension='png')
        plt.imsave(file_name, image)


if __name__ == '__main__':
    import argparse
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode'
    )
    parser.add_argument('-r', '--rule', type=int, default=110,
            help='automaton rule, default rule is 110',
    )
    parser.add_argument('-i', '--init', default='dot',
            choices=['dot','random'], help=('first row initialization method, '
            'default is a dot in the middle')
    )
    parser.add_argument('-s', '--steps', type=int, default=255,
            help='number of steps (pixel height - 1)',
    )
    parser.add_argument('-o', '--output', type=str,
            default='cellular_automaton_{rule}_{steps}.{extension}',
            help='file name for image of automaton history'
    )
    args = parser.parse_args()

    if args.debug:
        import pdb; pdb.set_trace()

    history = CellularAutomaton.compute(
            rule=args.rule, init=args.init, steps=args.steps
    )

    CellularAutomaton.save(
            matrix=history, file_template=args.output, rule=args.rule,
            steps=args.steps,
    )

