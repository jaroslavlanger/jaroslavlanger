#!/bin/sh
# Jaroslav Langer

# 1. Napište příkaz, který pomocí jediného spuštění vytvoří v aktuálním adresáři adresář 'dir2', v adresáři 'dir2' vytvoří adresář 'dir3' a v nadřazeném adresáři aktuálního adresáře vytvoří adresář 'dir1'. (1 bod)
mkdir dir2 dir2/dir3 ../dir1

# 2. Napište příkaz, který vypíše posledních 15 řádků ze souboru '/etc/passwd'. (1 bod)
tail -15 /etc/passwd

# 3. Napište dva způsoby vytvoření symbolického linku jménem 'ABC' pro soubor 'abc'. (1 bod) 
ln -s abc ABC
cp -s abc ABC

# 4. Napište wildcard vzor pro soubory, které jsou dlouhé 4 znaky, začínají velkým písmenem, druhým znakem je alfanumerický znak a končí libovolnými dvěma znaky. (1 bod)
[[:upper:]][[:alnum:]]??

# 5. Napište příklad jména souboru, který zachytí následující wildcard vzor: (1 bod)
# ?[[:alpha:]][3-4][xyz[:digit:]]
?O42
