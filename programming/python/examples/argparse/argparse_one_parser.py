#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Argparse Example

Author:     Jaroslav Langer
Modified:   2021 Jan 31
"""

if __name__ == '__main__':
    import sys
    import argparse
    import math

    # Create parser
    parser = argparse.ArgumentParser(description=__doc__)

    # Add arguments

    # True-False Argument
    parser.add_argument("-d", "--debug", action='store_true',
            help="run in debug mode")

    # Value argument
    parser.add_argument("-m", "--max_iter", type=int, nargs='+', default=(500,),
            help="maximum number of iterations")
    parser.add_argument("-t", "--tabu_tenure", default=math.sqrt,
            help="length of tabu tenure")
    parser.add_argument("--type", choices=["DNA", "AA"],
            help="reformat nucleic acid or amino acid sequence")

    # Named file argument
    parser.add_argument("-s", "--metadata", type=argparse.FileType('w'),
            help="metadata for statistical purposes")

    # Input/Outupt positional arguments
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
            help='input file, if not given, stdin is used')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
            help='output file, if not given, stdout is used')

    args = parser.parse_args()

    print(args, end='\n\n')
    print(args.debug, args.max_iter, args.tabu_tenure, args.metadata,
        args.input, args.output, sep='\n')

