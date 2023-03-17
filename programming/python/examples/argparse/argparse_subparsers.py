#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subparsers Example

Bunch of lines i have probably used/tested in the past.
I did not have the time to go through them and clean this up.

Author:     Jaroslav Langer
Modified:   2021 Jan 31
"""

if __name__ == '__main__':
    import sys
    import argparse

    # create the top-level parser
    parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument('action', type=str, help="Name of desired action",
    #     choices=['reformat', 'reverse_complement', 'statistic', 'get_region', 'translate'])
    # parser = argparse.ArgumentParser(prog='PROG')
    # parser.add_argument('--foo', action='store_true', help='foo help')
    
    # Create sub parsers
    subparsers = parser.add_subparsers(help='')
    subparsers_list = []
    
    parser_reformat = subparsers.add_parser('reformat', aliases=['refo'], 
        help='Reads sequences and formates it as correct fasta.')
    subparsers_list.append(parser_reformat)
    
    parser_reverse_complement = subparsers.add_parser('reverse_complement', aliases=['rc'],
        help='Reverse given sequence and interchange every nucleotide for its complementary one')
    subparsers_list.append(parser_reverse_complement)

    parser_get_region = subparsers.add_parser('get_region', aliases=['gr'],
        help='For every sequence returns desired region')
    subparsers_list.append(parser_get_region)

    parser_translate = subparsers.add_parser('translate', aliases=['tran'],
        help='Translate given sequence into amino acid sequence')
    subparsers_list.append(parser_translate)


    # Add common optional arguments # subparsers.choices.items() does not work, dunno why
    for subparser in subparsers_list:
        subparser.add_argument('-l', '--line_length', metavar='N', type=int, default=LINE_LENGTH,
            help='Length of sequence line (newline characters does not count, for width 80 use length 79)')

    parser_statistic = subparsers.add_parser('statistic', aliases=['stat'],
        help='Gives basic statistics about read sequences such as lengths, residue composition etc.')
    subparsers_list.append(parser_statistic)

    for subparser in subparsers_list:
        subparser.add_argument("-f", "--filter", type=str.lower, help="Optional filtering, slower, safer",
            choices=['y', 'yes', 't', 'true', 'on', '1', 'n', 'no', 'f', 'false', 'off', '0'], default='false')
        subparser.add_argument("-s", "--seq_start", metavar='str', type=str, default=SEQ_NAME_START,
            help=f"Beginning of name of sequence, default: {SEQ_NAME_START}")

    # Specific arguments for command reformat
    parser_reformat.add_argument("seq_type", type=str.upper, choices=[DNA, RNA, AA],
        help="Reformat nucleic acid or amino acid sequence")
    parser_reformat.set_defaults(command=reformat, filter='true')
    # parser_reformat.set_defaults(filter=True)

    # Specific arguments for command reverse_complement
    parser_reverse_complement.add_argument("seq_type", type=str.upper, choices=[DNA, RNA],
        help="Type of sequence to be reversed and complementary interchanged")
    parser_reverse_complement.set_defaults(command=reverse_complement)

    # # Specific arguments for command translate
    parser_translate.add_argument("-t", "--seq_type", type=str.upper, choices=[DNA, RNA],
        help="Type of sequence to be translated, required only when filter is set true", default=None)
    parser_translate.set_defaults(command=translate)

    # Specific arguments for command statistic
    parser_statistic.add_argument("seq_type", type=str.upper, choices=[DNA, RNA, AA],
        help="Type of sequence for desired statistic")
    parser_statistic.set_defaults(command=statistic)

    # Specific arguments for command get_region
    parser_get_region.add_argument("-t", "--seq_type", type=str.upper, choices=[DNA, RNA, AA],
    help="Type of sequence, required if filter option is set true", default=None)
    parser_get_region.add_argument('first', type=int, 
        help='First index of desired string range. String is indexed from 1 to n.')
    parser_get_region.add_argument('last', type=int, 
        help='Last index of desired string range. String is indexed from 1 to n.')
    parser_get_region.set_defaults(command=get_region)

    # Define common positional arguments
    for subparser in subparsers_list:
        subparser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
            help='Optional input, if not given, stdin is used')
        subparser.add_argument('output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
            help='Optional output, if not given, stdout is used')

    # Parse arguments, additional handle
    args_dict = vars(parser.parse_args())
    if ('filter' in args_dict):
        args_dict = handleFilterOption(args_dict) 

    
    # Exctract command and call it
    function = args_dict.pop('command')
    
    function(**args_dict) if (function is not None) else parser.print_help()
    # print(f"args_dict: {args_dict}")
    # args.func(**vars(args))

