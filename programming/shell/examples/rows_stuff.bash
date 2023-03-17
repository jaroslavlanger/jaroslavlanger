#!/bin/bash

file_in=dirs/zkc4_inst_5.dat
file_sol=dirs/zkc4_sol.dat

# CREATE SAMPLES
shuf -n 5 ${file_inst} | sort > ${file_in}

# cut -d ' ' -f 1 dirs/nk4_inst_5.dat

# cut -d ' ' -f 1 dirs/nk4_inst_5.dat | tr '\n' '|'

# id_rows=$(cut -d ' ' -f 1 dirs/nk4_inst_5.dat)

# id_rows=$(cut -d ' ' -f 1 dirs/nk4_inst_5.dat)
# echo $id_rows | tr ' ' '|'


# egrep ${id_patt:0:-1} dirs/nk4_inst.dat

# egrep "^(${id_patt:0:-1})" dirs/nk4_inst.dat

# echo ${a:0:-1}

id_patt=$(cut -d ' ' -f 1 dirs/nk4_inst_5.dat | tr '\n' '|')
egrep "^(${id_patt:0:-1}) " dirs/nk4_sol.dat | cut -d ' ' -f 3

