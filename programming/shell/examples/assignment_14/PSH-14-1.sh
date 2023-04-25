# !/bin/bash
: '
Author:   Jaroslav Langer
Date:     25/05/2019
Desc.:    Skript, který nakreslí pravoúhlý trojúhelník pro zadané odvěsny.
'

read -p "Zadejte delku odvesny: "

start=\*
mid=$start
end=$mid

echo "$start"

for ((i=0; i<$REPLY-2; i++)); do
        mid=$start
        end=$end$start
        for ((j=0; j<i; j++)); do
                #POZOR - tady musí být před newlinou jedna mezera!
                mid=$mid\ 
        done
        mid=$mid$start
        echo "$mid"
done
end=$end$start
echo "$end"
