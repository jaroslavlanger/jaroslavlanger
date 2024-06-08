#!/bin/bash
#Jaroslav Langer
#01/05/2019

# Napište skript s názvem 'struktura', který přijímá dva argumenty (viz Ukázka použití skriptu). Prvním argumentem je jméno souboru, který obsahuje data o strukturách DNA. Na každém řádku souboru jsou dvojtečkou oddělena metadata pro unikátní strukturu podle níže uvedeného vzoru a formátu. Druhým argumentem je kód DNA struktury, kterým začíná záznam metadat na řádku. Po spuštění skript vyzve uživatele k zadání desetinného čísla (jako oddělovač desetinných míst předpokládejte tečku). Skript v datovém vstupním souboru vyhledá a zpracuje příslušný řádek metadat podle zadaného kódu struktury a na výstup vypíše metadata přesně podle níže uvedeného formátu (viz Ukázka výstupu). Odevzdejte přímo soubor se skriptem.
# (1 bod za každý řádek výstupu)
# 
# Ukázka vstupního souboru 'vstup.txt':
# ... (záznamům může předcházet libovolný počet řádků)
# 1ZFF:GCT duplex B-DNA:0.9:F. Hays, A. Teegarden, Z. Jones, M. Harms:2005-05-10
# 1BNA:Structure of a B-DNA dodecamer:1.9:T. Takano, C. Broka, S. Tanaka, K. Itakura:1981-05-21
# 3WBO:Crystal structure analysis of the Z-DNA hexamer:0.8:T. Chatake:2014-05-14
# 4HIG:Ultrahigh-resolution crystal structure of Z-DNA in complex:1.2:P. Drozdzal, M. Gilski, R. Kierzek, L. Lomozik:2013-06-05
# ...
# 
# Ukázka použití skriptu:
# struktura vstup.txt 1BNA
# 
# Výzva shellu:
# Zadejte desetinne cislo: 1.3
# 
# Ukázka výstupu:
# struktura = 1BNA                                        # kód struktury beze změny
# nazev = Structure of a B-DNA dodecamer                  # název beze změny
# rozliseni = 1.9 + 1.3 = 3.2                             # původní hodnota a hodnota zvětšená o uživatelem vložené číslo
# autori = T. TAKANO, C. BROKA, S. TANAKA, K. ITAKURA     # jména autorů převedena na velká písmena
# rok = 1981                                              # z celého datumu vypíše pouze rok

read -p "Zadejte desetinne cislo: "
echo ''
line=$(egrep $2 $1)

echo "struktura = $2"
# kod struktury beze změny

nazev=$(echo $line | cut -d ':' -f 2)
echo "nazev = $nazev"
# název beze změny

roz=$(echo $line | cut -d ':' -f 3)
echo $REPLY | awk -v var="$roz" '{print "rozliseni = ",var,"+",$1,"=",var+$1}'
 # původní hodnota a hodnota zvětšená o uživatelem vložené číslo

autori=$(echo $line | cut -d ':' -f 4)
echo $autori | awk '{print "autori =",toupper($0)}'
# jména autorů velkými písmeny

rok=$(echo $line | cut -d ':' -f 5)
echo $rok | sed 's/\([[:alnum:]]\{4\}\).*/rok = \1/'
# z celého datumu pouze rok
