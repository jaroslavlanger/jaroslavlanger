# !/bin/bash
: '
Author:   Jaroslav Langer
Date:     25/05/2019
Desc.:    Skript, který pro číslo n vypíše řadu čísel od jedné do n,
    vynechá čísla, dělitelná 3 nebo 7.
'


read -p "Zadejte cislo: "

line=1
for ((i=2; i<$REPLY+1; i++)); do
        if (( i %3 != 0 && i%7 != 0 )); then
                line=$line\ $i
        fi
done
echo "$line"
