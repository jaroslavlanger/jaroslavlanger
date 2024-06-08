#!/bin/bash

if (($# < 1)); then echo "First argument is required, was not given."; exit 1; fi

dir_data=../data
dataset=(NK ZKC ZKW)
ns=(4 10)

for ds in ${dataset[@]}; do
    for n in ${ns[@]}; do
        case $1 in
        show) echo ${dir_data}/${ds}/${ds^^}_${n};;
        samples) echo ALL GOOD;;
        *) echo "Desired action \"$1\" was not found.";;
        esac
    done
done

# for n in ${ns[@]}; do
#     # runtime=$(./pipeline --threads $t)
#     # allRuntimes+=( $runtime )
# done
