#!/bin/bash

source ~/Projects/learning/informatics/combinatorial_optimization/assignments/4_local_search/config.bash

OLDIFS=$IFS
IFS=','
for tup in n,cbrt n,sqrt n,div3 n,div2 n,n; do
    set -- $tup
    m=$1 # n # n^2 # 
    t=$2 # cbrt # sqrt # n_by_3 # n_by_2 # n # n^2 # 

    tabu_m_t=${outs}/tabu_${m}_${t}
    mkdir -p ${tabu_m_t}

    echo Output folder - ${tabu_m_t}
    echo "$(date +%T.%N) - Computation started."
    for dataset in ${base_path}/data/*; do
        for inst in ${dataset}/*inst*; do #*_{0,1,2,3}*inst*

            name=${inst##*/}
            ds_n=${name%%_inst*}
            n=$((${ds_n##*_}+0))

            if [ $n -gt 30 ]; then
                soln=${tabu_m_t}/${ds_n}_soln.csv
                meta=${tabu_m_t}/${ds_n}_meta.csv
                ${solver} -m ${m} -t ${t} -w ${meta} < ${inst} > ${soln}
                echo "$(date +%T.%N) - File ${name} done."
            fi
        done;
        echo
    done
done;
IFS=$OLDIFS

