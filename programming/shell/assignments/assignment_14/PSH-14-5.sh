# !/bin/bash
: '
Author:   Jaroslav Langer
Date:     25/05/2019
Desc.:    Skript, který přiřadí argument do jedné ze tří možných kategorií:
    slovo | číslo | ostatní.
'

var=$1

res=${var//[[:alpha:]]/}
if [ -s $res ]; then echo $1 = slovo; exit; fi

res=${var//[[:digit:]]/}
if [ -s $res ]; then echo $1 = cislo; exit; fi

echo $1 = ostatni
