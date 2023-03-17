#!/bin/sh
#Jaroslav Langer 27.3.2019

# 1. Napište tvar příkazu 'echo', který vypíše skryté soubory z aktuálního adresáře, přičemž vynechá výpis symbolů pro aktuální (.) a nadřazený (..) adresář. (1 bod)
echo "$(ls .[!.]*)"
# 2. Napište příkaz, který v aktuálním adresáři vytvoří adresáře s následujícími názvy. (1 bod)
# x1yZ x1yY x1yX x2yZ x2yY x2yX x3yZ x3yY x3yX
mkdir x{1,2,3}y{X,Y,Z}
# 3. Napište tvar příkazu 'echo', který vypíše níže uvedenou větu. Jméno uživatele je dáno aktuálně přihlášeným uživatelem a jednoduché uvozovky jsou součástí vypsaného textu. (1 bod)
# Stav účtu uživatele 'pepa' je $1.5
echo "Stav účtu uživatele '$USER' je \$1.5"
# 4. Napište tvar příkazu 'echo', který s využitím aritmetické expanse vypočítá následující příklad. (1 bod)
# 82 - 6 * 3^2 + 8 (slovy: osmdesát dva mínus šest krát tři na druhou plus osm)
echo $((82 -6 *3**2 +8))
# 5. S využitím expanse příkazu vypište rozšířené informace o souboru programu 'mv'. (1 bod)
ls -l `which mv`
