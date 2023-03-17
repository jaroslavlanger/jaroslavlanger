#!/bin/sh
# Jaroslav Langer 
# 17/04/2019

# 1. Napište tvar příkazu 'cut', který ze souboru '/etc/passwd' vybere z každé řádky pouze jméno uživatele a jeho UID číslo. Jako nový oddělovač pro vybrané hodnoty použije lomítko a výsledek uloží do souboru 'uzivatele' (formát viz níže). (1 bod)
# 
# Ukázka vstupního souboru '/etc/passwd':
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# ... atd.
# 
# Ukázka výstupního souboru 'uzivatele':
# root/0
# daemon/1
# bin/2
# ... atd.

cut -d ':' -f 1 /etc/passwd > name; cut -d ':' -f 3 /etc/passwd > uid; paste name uid -d '/' > uzivatele

# 2. V souboru 'mesta' jsou uloženy názvy měst a jejich vzdáleností od Atén (formát viz níže). Napište tvar příkazu 'sed', který uvedený vstup přetransformuje do níže uvedeného formátu výstupu. (1 bod)
# 
# Ukázka vstupního souboru 'mesta':
# Rim 2702
# Pariz 3172
# Praha 2194
# ... atd.
# 
# Ukázka výstupu:
# Vzdalenost Ateny - Rim je 2702 km.
# Vzdalenost Ateny - Pariz je 3172 km.
# Vzdalenost Ateny - Praha je 2194 km.
# ... atd.

sed 's/\([[:alpha:]]*\)\([[:digit:]]*\)$/Vzdalenost Ateny - \1je \2 km\./' mesta

# 3. V souboru 'mesta' jsou uloženy názvy měst a jejich vzdáleností od Atén (formát viz níže). Napište tvar příkazu 'sort', který seřadí řádky v uvedeném vstupu podle vzdálenosti od nejdelší po nejkratší. (1 bod)
# 
# Ukázka vstupního souboru 'mesta':
# Rim 2702
# Pariz 3172
# Praha 2194
# ... atd.
# 
# Ukázka výstupu:
# Pariz 3172
# Rim 2702
# Praha 2194
# ... atd.

sort -k 2 -r  mesta 

# 4. Napište tvar příkazu 'sed', který v souboru 'jmena.txt' vymaže všechny sudé řádky a změny v souboru uloží (tip: option -i). (1 bod)

sed -i '2~2d' jmena.txt

# 5. Napište příkaz, který do souboru 'users-online' uloží abecedně seřazený seznam uživatelských jmen uživatelů aktuálně přihlášených do systému (tip: příkaz 'who' vrací informace o aktuálně přihlášených uživatelích). (1 bod)

who | cut -d ' ' -f 1 | sort > users-online
