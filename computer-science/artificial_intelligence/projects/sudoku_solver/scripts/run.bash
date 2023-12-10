#!/bin/bash

for file in data/instances/*; do
    file_name=${file##*/}
    echo ${file_name}
    cat ${file} |
        ./sudoku_solver.py -l |
        diff data/solutions/${file_name%%.txt}_s.txt - |
        cat -t
    echo
done
