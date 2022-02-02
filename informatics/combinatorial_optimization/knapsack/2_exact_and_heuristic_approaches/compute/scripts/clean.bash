#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

if (($# < 1)); then
    for ds in ${dataset[@]}; do rm ${outs_path}/${ds}/*; done
    for ds in ${dataset[@]}; do rm ${ins_path}/${ds}/*; done
    for ds in ${dataset[@]}; do rm ${tmp_path}/${ds}/*; done
    for ds in ${dataset[@]}; do rm ${data_path}/computed/${ds}/*; done
else
    case $1 in
    outs)
        for ds in ${dataset[@]}; do rm ${outs_path}/${ds}/*; done
    ;;
    ins)
        for ds in ${dataset[@]}; do rm ${ins_path}/${ds}/*; done
    ;;
    tmp)
        for ds in ${dataset[@]}; do rm ${tmp_path}/${ds}/*; done
    ;;
    data)
        for ds in ${dataset[@]}; do rm ${data_path}/computed/${ds}/*; done
    ;;
    *)
        echo "Desired action \"$1\" was not found."
    ;;
    esac
fi
