#!/bin/sh
#Jaroslav Langer 
#2.4.2019

# 1. Pro níže uvedené symbolické reprezentace oprávnění napište jejich ekvivalent v oktalové reprezentaci. (1 bod)
# rw-rw-r--, rwxrwxr-x, r--------

echo rw-rw-r-- = 664
echo rwxrwxr-x = 775
echo r-------- = 400

# 2. Pro níže uvedené oktalové reprezentace oprávnění napište jejich ekvivalent v symbolické reprezentaci. (1 bod)
# 421, 600, 357

echo 755 = rwxr-xr-x
echo 600 = rw-------

# 3. Napište dva způsoby nastavení oprávnění pro adresář '/home/novak/download' (předpodkládejte, že jste vlastník uvedeného adresáře). Vlastník může vypsat obsah adresáře, může do něj vstoupit a mazat v něm soubory/adresáře. Členové skupiny vlastníka mohou vypsat obsah adresáře, vstoupit do něj, ale nemají v něm právo soubory/adresáře mazat. Všichni ostatní uživatelé nemají žádná oprávnění. (1 bod)
chmod 710 /home/novak/download
chmod u=rwx,g=x,o= /home/novak/download

# 4. Zapište posloupnost příkazů, které provedou následující akce a nastavení (předpokládejte, že jste uživatel 'root'). V adresáři '/data' vytvořte adresář 'testy', jehož vlastníkem bude uživatel 'root' a skupina 'ucitel'. Vlastníkovi a skupině u uvedeného adresáře nastavte všechna oprávnění, ostatním odepřete všechna práva. (1 bod)
mkdir /home/testy
chown :ucitel testy
chmod 2770 testy

# 5. Napište formát příkazu 'find', který najde v aktuálním adresáři a všech jeho podadresářích všechny soubory uživatele 'pepa', které mají pro ostatní uživatele (others) nastaveno právo spuštění. Na nastavení oprávnění vlastníka a skupiny nehleďte. (1 bod)
# tip: příkaz 'find' disponuje testy -user a -perm
find /home/pepa/ -type f -user pepa -perm -o=x -delete
find -maxdepth 1 -type f -name *.jpg -size +2M -exec chown :fotograf {} \;
