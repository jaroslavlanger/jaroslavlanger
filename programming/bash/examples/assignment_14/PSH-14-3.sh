# !/bin/bash
: '
Author:   Jaroslav Langer
Date:     25/05/2019
Desc.:    Skript, který pro zadané číslo n vypíše matici součinů.
'

read -p "Zadejte cislo: "

first=#
for ((a=1; a<$REPLY+1; a++)); do
        first=$first\ $a
done
echo $first

for ((i=1;i<$REPLY+1;i++)); do
        line=$i
        for ((j=1;j<$REPLY+1;j++)); do
                num=$(( j*i ))
                line=$line\ $num
        done
        echo $line
done