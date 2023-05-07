# !/bin/bash
: '
Author:   Jaroslav Langer
Date:     25/05/2019
Desc.:    Skript, který pro zadanou řadu čísel zjistí, 
    zda-li se součin na lichých a sudých pozicích rovná.
'

fu (){
        num=$#
        odd=1
        even=1
        for ((i=1; i<$num+1; i++)); do
                (( i%2==0? (even *= $1) : (odd *= $1) ))
                shift 1
        done
        if (( odd == even )); then echo ANO; else echo NE; fi
        echo "soucin na lichych pozicich: $odd"
        echo "soucin na sudych pozicich: $even"
}

read -p "Zadejte ciselnou radu: "

fu $REPLY