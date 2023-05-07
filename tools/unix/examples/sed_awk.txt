#!/bin/sh
# Jaroslav Langer 
# 24/04/2019

# 1. Pomocí příkazu 'paste' spojte obsahy souborů 'jmena1' a 'jmena2', a výsledek zapište do souboru 'jmena'. Jako oddělovač jmen použijte dvojtečku. (1 bod)
# 
# Ukázka souboru 'jmena1':
# Karel
# Bohdan
# Jaromir
# 
# Ukázka souboru 'jmena2':
# Novotny
# Vymetal
# Nedusil
# 
# Ukázka souboru 'jmena':
# Karel:Novotny
# Bohdan:Vymetal
# Jaromir:Nedusil

sed 'w jmena' jmena1 jmena2

# 2. Ze vstupního souboru vytvořte pomocí příkazu 'sed' varianty odpovědí pro vědomostní test, tzn. každé řádce ze vstupního souboru bude předcházet nová řádka s textem buď "a)", nebo "b)", nebo "c)", a to opakovaně ve stejném pořadí. (1 bod)
# 
# Ukázka vstupního souboru:
# prvni odpoved
# druha odpoved
# treti odpoved
# prvni odpoved
# druha odpoved
# treti odpoved
# ... atd.
# 
# Ukázka výstupu:
# a)
# prvni odpoved
# b)
# druha odpoved
# c)
# treti odpoved
# a)
# prvni odpoved
# b)
# druha odpoved
# c)
# treti odpoved
# ... atd.

sed '1~3i a)' input | sed '/a)/{N; s/\n/ /}' | sed '2~3i b)' | sed '/b)/{N; s/\n/ /}' | sed '3~3i c)' | sed '/c)/{N; s/\n/ /}'

# 3. Pomocí příkazu 'sed' odstraňte ze vstupního html souboru všechnny html tagy. Ve výstupu zůstanou jen textové informace, pokud je některé HTML tagy obsahují. Zároveň odstraňte všechny prázdné řádky, pokud po předchozí úpravě nějaké vzniknou. (1 bod)
# 
# Ukázka vstupního souboru html:
# <html>
#     <head>
#         <title>Nazev stranky</title>
#     </head>
#     <body>
#         <h1>Nadpis</h1>
#         <div>
#             <p>Tohle je <b>1.</b> odstavec</p>
#             <p>Tohle je <b>2.</b> odstavec</p>
#         </div>
#     </body>
# </html>
# 
# Ukázka výstupu:
#         Nazev stranky
#         Nadpis
#             Tohle je 1. odstavec
#             Tohle je 2. odstavec

sed -e '{s/<\/.*>//; s/<.*>//; /^[[:blank:]]*$/d}' /scratch/expressions/index.html

# 4. Najděte všechny skupiny uživatelů v systému, jejichž jméno začíná písmenem 's'. Vypište jejich GID (group id) a název oddělené mezerou (formát výstupu viz níže). Seznam všech skupin je uveden v souboru '/etc/group'. (1 bod)
# 
# Ukázka výstupu:
# 3 sys
# 27 sudo
# 108 ssh
# ... atd.

egrep '^s' /etc/group | awk -F : '{print $3, $1}'

# 5. Uvažujte vstupní soubor, kde jsou na každém řádku dvě celá kladná čísla oddělená čárkou (viz ukázka vstupu). Pro každý řádek ze vstupního souboru proveďte rozdíl mezi uvedenými čísly a na výstup vypište výsledky ve formátu podle níže uvedeného vzoru. (1 bod)
# 
# Ukázka vstupního souboru:
# 23,35
# 69,3
# 357,17
# ... atd.
# 
# Ukázka výstupu:
# Vyhodnoceni prikladu
# 23 - 35 = -12
# 69 - 3 = 66
# 357 - 17 = 340
# ... atd.

awk -F , '{print $1 " - " $2 " = " $1-$2 }' input
