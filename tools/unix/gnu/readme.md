# GNU

* [GNU Manuals Online](https://www.gnu.org/manual/)

## Software development

* [GNU Bash](https://www.gnu.org/software/bash/)
* [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)
  * [14.3 `stat`: Report file or file system status](https://www.gnu.org/software/coreutils/manual/coreutils.html#stat-invocation)
  * [21.1 `date`: Print or set system date and time](https://www.gnu.org/software/coreutils/manual/coreutils.html#date-invocation)
    * `diff -u $file /dev/null | head -n 1 | cut -f 2 | xargs -I {} date -d {} +%s`
  * [26.3 `seq`: Print numeric sequences](https://www.gnu.org/software/coreutils/manual/coreutils.html#seq-invocation)
* [GNU Findutils](https://www.gnu.org/software/findutils/manual/html_mono/find.html)
  * [8.4 Invoking `xargs`](https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs)
    * `find . | xargs ls -1d --color=always`
    * `{ for d in {2,10}; do for f in {1,3,6}; do echo $d $f; done; done } | xargs -n2 -P3 sh -c 'n="$1_$2_name"; python script.py -d $1 -f $2 2> ${n}.err > ${n}.out' _`
* [GCC, the GNU Compiler Collection](https://www.gnu.org/software/gcc/)

## System administration

* [GNU Parallel](https://www.gnu.org/software/parallel/)
* [GNU Time](https://www.gnu.org/software/time/)
  * `/bin/time -v -o time.out -a COMMAND...`
