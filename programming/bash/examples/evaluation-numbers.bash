# TODO
# * pass the information in different file descriptors than stdin, stdout
# eg. echo std >&3 && <&3 tr ' ' '\n' ...
#
# | xargs -I IT sh -c "ls -l IT && echo IT"
# | tr ' ' '\n' \
# | xargs -n 1 sh -c 'wget --no-verbose https://github.com/jaroslavlanger/nncmaes/raw/main/test/meta/$0.zip' 2>&1 | cut -d ' ' -f 6 \
# | xargs -I {} unzip -q {}.zip \
# | xargs -I {} unzip -z {}.zip | cut -c 11-
# && echo $(yes - | head -n 93 | tr -d '\n') \

get_evals () {
    pcre2grep --om-separator='
' -o1 -o2 ' ([0-9]+)-evals *([0-9]+)-cma-evals' $1 \
    | python3 -c '\
import sys
from statistics import mean
print(*map(lambda l_: f"{mean(l_):>5.1f}", ((l:= list(map(int, sys.stdin.readlines())))[::2], l[1::2])), end="")'
}

wget --no-verbose https://github.com/jaroslavlanger/nncmaes/raw/main/test/meta/test00{1,2}.zip 2>&1 | head -n -3 | cut -d ' ' -f 6 \
    | xargs -I ZIP unzip -q ZIP \
    && pr -mts'	' \
        <(for n in $(seq 24); do f="test001/mean/exp_mean_2d_${n}f_i.out"; printf "%-35s" $f; get_evals $f; echo; done) \
        <(for f in test002/mean/d02_f*_mean.out; do get_evals $f; echo "	$f"; done) \
    && rm -r test00{1,2}{,.zip}
