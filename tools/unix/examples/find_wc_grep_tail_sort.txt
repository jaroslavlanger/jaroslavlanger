#!/bin/sh
#Jaroslav Langer 13.3.2019

# 1. Napište příkaz, který najde pouze v aktuálním adresáři všechny skryté prázdné soubory. (1 bod)
find -maxdepth 1 -type f -empty -name ".*"
# 2. Napište příkaz, který spočítá všechny linky s příponou '.txt' v aktuálním adresáři a všech jeho podadresářích. (1 bod)
find -type l -name "*.txt" | wc
# 3. Napište příkaz, který najde soubory větší než 1 kilobyte a u každého z nich vypíše o jaký typ souboru se jedná. (1 bod)
find / -type f -size +1k -exec "file" {} \;
# 4. Napište příkaz, který vypíše 3 nejstarší soubory z aktuálního adresáře. (1 bod)
ls -tpl | grep -v "/" | grep -v "\->" | tail -3
# 5. Napište příkaz, který seřadí pozpátku jména uvedená v souboru 'names.txt' a uloží je do souboru 'names_sorted.txt'. (1 bod)
cat names.txt | sort -r >> names_sorted.txt
