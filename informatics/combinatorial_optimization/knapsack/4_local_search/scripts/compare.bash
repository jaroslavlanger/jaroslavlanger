#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/assignments/4_local_search/config.bash

m=n^2 #n # 
t=n^2 # sqrt # 
tabu_m_t=${outs}/tabu_${m}_${t}

for dataset in ${base_path}/data/*; do
    for file in ${dataset}/*soln*; do # _{0,1}
        name=${file##*/}
        echo ${name} \
        $(diff -y --suppress-common-lines ${file} ${tabu_m_t}/${file##*/} |
        wc -l)
    done;
    echo
done

