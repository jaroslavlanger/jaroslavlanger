#!/bin/bash

(( $# < 1 )) && echo "First argument is required, was not given." && exit 1
[[ $1 == gen ]] && (( $# < 2 )) && echo "Argument required by generator, was not given." && exit 1

source /home/langerjaros/Projects/learning/informatics/combinatorial_optimization/homeworks/hw03/scripts/config.bash

gen () {
    echo $1
    # kg2 -n inst-size -N inst-num -W num -C num [-a] [-I id] [-m rnum[,rnum]] [-w bal|light|heavy] [-c uni|corr|strong] [-k rnum][PRNG-control]
    ${gen_cmd} -n $n -N $N -W $W -C $C -m $m -w $w -c $c -k $k > $1
}

perm () {
    shuf -n $d $1 | ${perm_cmd} -d $d -N $N > $2
}

case $1 in
create) # Create data directories
    cd ${data_path};    mkdir -p    ns ms Ws ws Cs cs ks ps;  cd ${scripts_path}  ;;
gen)    # Generate samples
    case $2 in
    ns) for nn in ${ns[@]}; do n_tmp=${n}; n=${nn};
            gen ${data_path}/ns/n_${nn}_inst.csv;
        done; n=${n_tmp} ;;
    ms) for mm in ${ms[@]}; do m_tmp=${m}; m=${mm};
            gen ${data_path}/ms/m_${mm}_inst.csv;
        done; m=${m_tmp} ;;
    Ws) for WW in ${Ws[@]}; do W_tmp=${W}; W=${WW};
            gen ${data_path}/Ws/W_${WW}_inst.csv;
        done; W=${W_tmp} ;;
    ws) for ww in ${ws[@]}; do w_tmp=${w}; w=${ww};
            gen ${data_path}/ws/w_${ww}_inst.csv;
        done; w=${w_tmp} ;;
    Cs) for CC in ${Cs[@]}; do C_tmp=${C}; C=${CC};
            gen ${data_path}/Cs/C_${CC}_inst.csv;
        done; C=${C_tmp} ;;
    cs) for cc in ${cs[@]}; do c_tmp=${c}; c=${cc};
            gen ${data_path}/cs/c_${cc}_inst.csv;
        done; c=${c_tmp} ;;
    ks) for ww in light heavy; do w_tmp=${w}; w=${ww};
            for kk in ${ks[@]}; do k_tmp=${k}; k=${kk};
                gen ${data_path}/ks/k_${ww}_${kk}_inst.csv;
            done; k=${k_tmp};
        done; w=${w_tmp} ;;
    ps) for pp in ${ps[@]}; do p_tmp=${p}; p=${pp};
            perm ${data_path}/ns/n_${n}_inst.csv ${data_path}/ps/p_${pp}_inst.csv;
        done; p=${p_tmp} ;;
    *)  echo "Desired action \"$2\" was not found." ;;
    esac    ;;
compute)
    echo "$(date +%T.%N) - Computation started."
    for nm in ${methods[@]}; do
        for nn in ${ns[@]}; do  ${knap} ${nm%:*} < ${data_path}/ns/n_${nn}_inst.csv > ${data_path}/ns/n_${nm#*:}_${nn}_sol.csv; done;
        for mm in ${ms[@]}; do  ${knap} ${nm%:*} < ${data_path}/ms/m_${mm}_inst.csv > ${data_path}/ms/m_${nm#*:}_${mm}_sol.csv; done;
        for WW in ${Ws[@]}; do  ${knap} ${nm%:*} < ${data_path}/Ws/W_${WW}_inst.csv > ${data_path}/Ws/W_${nm#*:}_${WW}_sol.csv; done;
        for ww in ${ws[@]}; do  ${knap} ${nm%:*} < ${data_path}/ws/w_${ww}_inst.csv > ${data_path}/ws/w_${nm#*:}_${ww}_sol.csv; done;
        for CC in ${Cs[@]}; do  ${knap} ${nm%:*} < ${data_path}/Cs/C_${CC}_inst.csv > ${data_path}/Cs/C_${nm#*:}_${CC}_sol.csv; done;
        for cc in ${cs[@]}; do  ${knap} ${nm%:*} < ${data_path}/cs/c_${cc}_inst.csv > ${data_path}/cs/c_${nm#*:}_${cc}_sol.csv; done;
        for ww in light heavy; do
            for kk in ${ks[@]}; do  ${knap} ${nm%:*} < ${data_path}/ks/k_${ww}_${kk}_inst.csv > ${data_path}/ks/k_${nm#*:}_${ww}_${kk}_sol.csv; done;
        done;
        for pp in ${ps[@]}; do  ${knap} ${nm%:*} < ${data_path}/ps/p_${pp}_inst.csv > ${data_path}/ps/p_${nm#*:}_${pp}_sol.csv; done;
        echo "$(date +%T.%N) - Method ${nm#*:} done."
    done    ;;
delete) # Delete data directories
    cd ${data_path};    rm -r   ns ms Ws ws Cs cs ks ps;    cd ${scripts_path}   ;;
*)
    echo "Desired action \"$1\" was not found." ;;
esac
