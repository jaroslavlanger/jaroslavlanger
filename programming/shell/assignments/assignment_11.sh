#!/bin/bash
#Jaroslav Langer
#09/05/2019

# 1. S využitím konstrukce 'if' napište skript s názvem 'cislo.sh', který otestuje vstup zadaný uživatelem. Skript nepřijímá žádné argumenty. Po spuštění skript vyzve uživatele k zadání vstupu. Pokud vstup není číslo, ukončí se s hláškou, že se nejedná o číselnou hodnotu (1 bod). Pokud je vstup číslo, skript vypíše, jestli je celé nebo desetinné (jako oddělovač desetinných míst předpokládejte tečku nebo čárku) (1 bod). Pokud je číslo desetinné, dále se nic netestuje a skript se ukončí. Pokud se jedná o celé číslo, skript dále vypíše, jestli je kladné nebo záporné (1 bod), dále jestli je sudé nebo liché (1 bod), a kolik má číslic (1 bod).
# 
# (TIP: počet znaků řetězce lze získat například pomocí stringové operace v rámci expanse parametru: a=-159; echo ${#a};)
# 
# Ukázka použití skriptu:
# cislo.sh
# 
# Výzva shellu:
# Zadejte hodnotu: -159
# 
# Ukázka výstupu:
# Vstup je cele cislo.
# Cislo je zaporne.
# Cislo je liche.
# Pocet cislic: 3

read -p "Zadejte hodnotu: "

if [[ $REPLY =~ ^(\+|-)?[[:digit:]]*$ ]]; then
        echo 'Vstup je cele cislo.'

        if (( REPLY > 0 )); then
                echo 'Cislo je kladne.'
        else
                echo 'Cislo je zaporne.'
        fi

        if (( REPLY%2 == 0 )); then
                echo 'Cislo je sude.'
        else
                echo 'Cislo je liche.'
        fi

        n=0
        while (( REPLY != 0 )); do
                REPLY=$(( REPLY/=10 ))
                n=$(( n+1 ))
        done
        echo "Pocet cislic: $n" 
        exit 0

elif [[ $REPLY =~ ^(\+|-)?[[:digit:]]+(\.|,)[[:digit:]]*$ ]]; then
        echo 'Vstup je desetinne cislo.'
        exit 0
fi

echo 'Nejedna se o ciselnou hodnotu'
exit 1
