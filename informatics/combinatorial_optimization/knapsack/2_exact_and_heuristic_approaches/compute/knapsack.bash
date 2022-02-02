#!/bin/bash

if (($# < 1)); then echo "First argument is required, was not given."; exit 1; fi

source ~/Projects/learning/informatics/combinatorial_optimization/homeworks/hw02/compute/scripts/config.bash

inst_path=${data_path} #${ins_path} #
sol_path=${data_path} #${outs_path} #
computed_path=${data_path}/computed #${tmp_path} #

for n in ${ns[@]}; do
    for ds in ${dataset[@]}; do
        for m in ${methods[@]}; do
            inst_file=${inst_path}/${ds}/${ds^^}${n}_inst.dat
            sol_file=${sol_path}/${ds}/${ds^^}${n}_sol.dat
            computed_file=${computed_path}/${ds}/${ds}_${m#*:}_${n}.csv
            case $1 in
            samples)
                data_inst_file=${data_path}/${ds}/${ds^^}${n}_inst.dat
                ins_inst_file=${ins_path}/${ds}/${ds^^}${n}_inst.dat
                data_sol_file=${data_path}/${ds}/${ds^^}${n}_sol.dat
                outs_sol_file=${outs_path}/${ds}/${ds^^}${n}_sol.dat

                shuf -n ${samples_num} ${data_inst_file} | sort -t ' ' -n > ${ins_inst_file}
                id_patt=$(cut -d ' ' -f 1 ${ins_inst_file} | tr '\n' '|')
                egrep "^(${id_patt:0:-1}) " ${data_sol_file} > ${outs_sol_file}
            ;;
            compute)
                $knapsack_cmd ${m%%:*} < ${inst_file} > ${computed_file}
                if (( ${m%%:*} == 6 )); then
                    for e in ${epsilons[@]}; do
                        fptas_file=${computed_path}/${ds}/${ds}_${m#*:}_${n}_$(echo $e | tr -d "." ).csv
                        $knapsack_cmd ${m%%:*} ${e} < ${inst_file} > ${fptas_file}
                    done
                fi
            ;;
            diff)
                case $2 in
                samples)
                    ins_inst_file=${ins_path}/${ds}/${ds^^}${n}_inst.dat
                    outs_sol_file=${outs_path}/${ds}/${ds^^}${n}_sol.dat
                    diff <(cut -d ' ' -f 1,2 ${ins_inst_file}) <(cut -d ' ' -f 1,2 ${outs_sol_file})
                ;;
                fptas)
                    (( ${m%%:*} == 6 )) && diff <(cut -d ' ' -f 1-$((3+$n)) ${sol_file}) <(cut -d ' ' -f 1-$((3+$n)) ${computed_file})
                ;;
                *) 
                    if (( ${m%%:*} == 1 || ${m%%:*} == 2 || ${m%%:*} == 3 || ${m%%:*} == 6)); then
                        diff <(cut -d ' ' -f 1-$((3+$n)) ${sol_file}) <(cut -d ' ' -f 1-$((3+$n)) ${computed_file})
                    fi
                ;;
                esac
            ;;
            rp)     $rp_cmd  ${m%%:*}                   < ${inst_file} > ${computed_file}   ;;
            bf)     (( ${m%%:*} == 1 )) && $bf_cmd    1 < ${inst_file} > ${computed_file}   ;;
            bab)    (( ${m%%:*} == 2 )) && $bab_cmd   2 < ${inst_file} > ${computed_file}   ;;
            dp)     (( ${m%%:*} == 3 )) && $dp_cmd    3 < ${inst_file} > ${computed_file}   ;;
            gh)     (( ${m%%:*} == 4 )) && $gh_cmd    4 < ${inst_file} > ${computed_file}   ;;
            fptas)  (( ${m%%:*} == 6 )) && $fptas_cmd 6 < ${inst_file} > ${computed_file}   ;;
            show)   echo ${dir_data}/${ds}/${ds^^}_${n}         ;;
            *)      echo "Desired action \"$1\" was not found." ;;
            esac
        done
    done
    echo "$(date +%T.%N) - Instances of size $n done."
done
