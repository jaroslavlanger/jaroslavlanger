# Assignments

```
Assignments from shell programming course (PSH) at UCT, Prague.

Assignee:   Jaroslav Langer
```

## Contents <!-- omit in toc -->
- [Assignment 01](#assignment-01)
- [Assignment 02](#assignment-02)
- [Assignment 03](#assignment-03)
- [Assignment 04](#assignment-04)
- [Assignment 05](#assignment-05)
- [Assignment 06](#assignment-06)
- [Assignment 07](#assignment-07)
- [Assignment 08](#assignment-08)
- [Assignment 09](#assignment-09)
- [Assignment 10](#assignment-10)
- [Assignment 11](#assignment-11)
- [Assignment 12](#assignment-12)
- [Assignment 13](#assignment-13)
- [Assignment 14](#assignment-14)

## Assignment 01

Vyberte si libovolný příkaz shellu (1 bod). Pomocí informací z nápovědy k příkazu zjistěte a napište (česky), k čemu příkaz slouží (1 bod). Využijte voleb (tzv. options) vybraného příkazu a uveďte tři různé příklady jeho použití, a popište, co zvolená volba konkrétně provádí (3 body).

## Assignment 02

1. Napište příkaz, který pomocí jediného spuštění vytvoří v aktuálním adresáři adresář 'dir2', v adresáři 'dir2' vytvoří adresář 'dir3' a v nadřazeném adresáři aktuálního adresáře vytvoří adresář 'dir1'. (1 bod)

2. Napište příkaz, který vypíše posledních 15 řádků ze souboru '/etc/passwd'. (1 bod)

3. Napište dva způsoby vytvoření symbolického linku jménem 'ABC' pro soubor 'abc'. (1 bod) 

4. Napište wildcard vzor pro soubory, které jsou dlouhé 4 znaky, začínají velkým písmenem, druhým znakem je alfanumerický znak a končí libovolnými dvěma znaky. (1 bod)

5. Napište příklad jména souboru, který zachytí následující wildcard vzor: (1 bod)

?[[:alpha:]][3-4][xyz[:digit:]]

## Assignment 03

1. Napište příkaz, který najde pouze v aktuálním adresáři všechny skryté prázdné soubory. (1 bod)

2. Napište příkaz, který spočítá všechny linky s příponou '.txt' v aktuálním adresáři a všech jeho podadresářích. (1 bod)

3. Napište příkaz, který najde soubory větší než 1 kilobyte a u každého z nich vypíše o jaký typ souboru se jedná. (1 bod)

4. Napište příkaz, který vypíše 3 nejstarší soubory z aktuálního adresáře. (1 bod)

5. Napište příkaz, který seřadí pozpátku jména uvedená v souboru 'names.txt' a uloží je do souboru 'names_sorted.txt'. (1 bod)

## Assignment 04

## Assignment 05

1. Napište tvar příkazu 'echo', který vypíše skryté soubory z aktuálního adresáře, přičemž vynechá výpis symbolů pro aktuální (.) a nadřazený (..) adresář. (1 bod)

2. Napište příkaz, který v aktuálním adresáři vytvoří adresáře s následujícími názvy. (1 bod)
x1yZ x1yY x1yX x2yZ x2yY x2yX x3yZ x3yY x3yX

3. Napište tvar příkazu 'echo', který vypíše níže uvedenou větu. Jméno uživatele je dáno aktuálně přihlášeným uživatelem a jednoduché uvozovky jsou součástí vypsaného textu. (1 bod)
Stav účtu uživatele 'pepa' je $1.5

4. Napište tvar příkazu 'echo', který s využitím aritmetické expanse vypočítá následující příklad. (1 bod)
82 - 6 * 3^2 + 8 (slovy: osmdesát dva mínus šest krát tři na druhou plus osm)

5. S využitím expanse příkazu vypište rozšířené informace o souboru programu 'mv'. (1 bod)

## Assignment 06

1. Pro níže uvedené symbolické reprezentace oprávnění napište jejich ekvivalent v oktalové reprezentaci. (1 bod)
rw-rw-r--, rwxrwxr-x, r--------

2. Pro níže uvedené oktalové reprezentace oprávnění napište jejich ekvivalent v symbolické reprezentaci. (1 bod)
421, 600, 357

3. Napište dva způsoby nastavení oprávnění pro adresář '/home/novak/download' (předpodkládejte, že jste vlastník uvedeného adresáře). Vlastník může vypsat obsah adresáře, může do něj vstoupit a mazat v něm soubory/adresáře. Členové skupiny vlastníka mohou vypsat obsah adresáře, vstoupit do něj, ale nemají v něm právo soubory/adresáře mazat. Všichni ostatní uživatelé nemají žádná oprávnění. (1 bod)

4. Zapište posloupnost příkazů, které provedou následující akce a nastavení (předpokládejte, že jste uživatel 'root'). V adresáři '/data' vytvořte adresář 'testy', jehož vlastníkem bude uživatel 'root' a skupina 'ucitel'. Vlastníkovi a skupině u uvedeného adresáře nastavte všechna oprávnění, ostatním odepřete všechna práva. (1 bod)

5. Napište formát příkazu 'find', který najde v aktuálním adresáři a všech jeho podadresářích všechny soubory uživatele 'pepa', které mají pro ostatní uživatele (others) nastaveno právo spuštění. Na nastavení oprávnění vlastníka a skupiny nehleďte. (1 bod)
tip: příkaz 'find' disponuje testy -user a -perm

## Assignment 07

1. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny IPv4 adresy. Předpokládejte následující formát a rozsah IP adres. Formát IPv4 adresy je x.x.x.x kde x je v rozsahu 0 až 255, v libovolné kombinaci na jednotlivých pozicích (např. 147.251.124.113 nebo 192.168.0.1 atd.). (1 bod)

2. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechna desetinná čísla. Předpokládejte následující formát desetinných čísel. Číslo může, ale nemusí, začínat znaménkem plus nebo mínus. Následuje libovolný počet číslic, oddělovač desetinných míst (čárka nebo tečka) a končí maximálně dvěmi číslicemi. (1 bod)

3. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny HTML tagy pro nadpis (header) včetně jejich případného obsahu a koncového tagu. To znamená tagy <h1>x</h1>, <h2>x</h2>, <h3>x</h3>, <h4>x</h4>, <h5>x</h5>, <h6>x</h6>, kde x je libovolný text. Uvažujte také variantu s velkými písmeny v názvu tagu, tedy <H1>x</H1> atp. (1 bod)

4. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny časy zapsané v následujícím formátu. Formát je hh:mm:ss kde hh je hodina v rozsahu 00 až 23, mm je minuta v rozsahu 00 až 59 a ss je sekunda v rozsahu 00 až 59. Oddělovačem hodnot je dvojtečka a uvažujte pouze dvojciferné varianty čísel. (1 bod)

5. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny emailové adresy. Uvažujte následující formát emailové adresy. Před zavináčem je text v rozsahu 4 až 15 znaků a obsahuje pouze alfanumerické znaky. Následuje zavináč, alfanumerický text v rozsahu 3 až 10 znaků, tečka a dvou- nebo třípísmenný kód domény. (1 bod)

## Assignment 08

1. Napište tvar příkazu 'cut', který ze souboru '/etc/passwd' vybere z každé řádky pouze jméno uživatele a jeho UID číslo. Jako nový oddělovač pro vybrané hodnoty použije lomítko a výsledek uloží do souboru 'uzivatele' (formát viz níže). (1 bod)

Ukázka vstupního souboru '/etc/passwd':
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
... atd.

Ukázka výstupního souboru 'uzivatele':
root/0
daemon/1
bin/2
... atd.

2. V souboru 'mesta' jsou uloženy názvy měst a jejich vzdáleností od Atén (formát viz níže). Napište tvar příkazu 'sed', který uvedený vstup přetransformuje do níže uvedeného formátu výstupu. (1 bod)

Ukázka vstupního souboru 'mesta':
Rim 2702
Pariz 3172
Praha 2194
... atd.

Ukázka výstupu:
Vzdalenost Ateny - Rim je 2702 km.
Vzdalenost Ateny - Pariz je 3172 km.
Vzdalenost Ateny - Praha je 2194 km.
... atd.

3. V souboru 'mesta' jsou uloženy názvy měst a jejich vzdáleností od Atén (formát viz níže). Napište tvar příkazu 'sort', který seřadí řádky v uvedeném vstupu podle vzdálenosti od nejdelší po nejkratší. (1 bod)

Ukázka vstupního souboru 'mesta':
Rim 2702
Pariz 3172
Praha 2194
... atd.

Ukázka výstupu:
Pariz 3172
Rim 2702
Praha 2194
... atd.

4. Napište tvar příkazu 'sed', který v souboru 'jmena.txt' vymaže všechny sudé řádky a změny v souboru uloží (tip: option -i). (1 bod)

5. Napište příkaz, který do souboru 'users-online' uloží abecedně seřazený seznam uživatelských jmen uživatelů aktuálně přihlášených do systému (tip: příkaz 'who' vrací informace o aktuálně přihlášených uživatelích). (1 bod)

## Assignment 09

1. Pomocí příkazu 'paste' spojte obsahy souborů 'jmena1' a 'jmena2', a výsledek zapište do souboru 'jmena'. Jako oddělovač jmen použijte dvojtečku. (1 bod)

Ukázka souboru 'jmena1':
Karel
Bohdan
Jaromir

Ukázka souboru 'jmena2':
Novotny
Vymetal
Nedusil

Ukázka souboru 'jmena':
Karel:Novotny
Bohdan:Vymetal
Jaromir:Nedusil

2. Ze vstupního souboru vytvořte pomocí příkazu 'sed' varianty odpovědí pro vědomostní test, tzn. každé řádce ze vstupního souboru bude předcházet nová řádka s textem buď "a)", nebo "b)", nebo "c)", a to opakovaně ve stejném pořadí. (1 bod)

Ukázka vstupního souboru:
prvni odpoved
druha odpoved
treti odpoved
prvni odpoved
druha odpoved
treti odpoved
... atd.

Ukázka výstupu:
a)
prvni odpoved
b)
druha odpoved
c)
treti odpoved
a)
prvni odpoved
b)
druha odpoved
c)
treti odpoved
... atd.

3. Pomocí příkazu 'sed' odstraňte ze vstupního html souboru všechnny html tagy. Ve výstupu zůstanou jen textové informace, pokud je některé HTML tagy obsahují. Zároveň odstraňte všechny prázdné řádky, pokud po předchozí úpravě nějaké vzniknou. (1 bod)

Ukázka vstupního souboru html:
<html>
    <head>
        <title>Nazev stranky</title>
    </head>
    <body>
        <h1>Nadpis</h1>
        <div>
            <p>Tohle je <b>1.</b> odstavec</p>
            <p>Tohle je <b>2.</b> odstavec</p>
        </div>
    </body>
</html>

Ukázka výstupu:
        Nazev stranky
        Nadpis
            Tohle je 1. odstavec
            Tohle je 2. odstavec

4. Najděte všechny skupiny uživatelů v systému, jejichž jméno začíná písmenem 's'. Vypište jejich GID (group id) a název oddělené mezerou (formát výstupu viz níže). Seznam všech skupin je uveden v souboru '/etc/group'. (1 bod)

Ukázka výstupu:
3 sys
27 sudo
108 ssh
... atd.

5. Uvažujte vstupní soubor, kde jsou na každém řádku dvě celá kladná čísla oddělená čárkou (viz ukázka vstupu). Pro každý řádek ze vstupního souboru proveďte rozdíl mezi uvedenými čísly a na výstup vypište výsledky ve formátu podle níže uvedeného vzoru. (1 bod)

Ukázka vstupního souboru:
23,35
69,3
357,17
... atd.

Ukázka výstupu:
Vyhodnoceni prikladu
23 - 35 = -12
69 - 3 = 66
357 - 17 = 340
... atd.

## Assignment 10

Napište skript s názvem 'struktura', který přijímá dva argumenty (viz Ukázka použití skriptu). Prvním argumentem je jméno souboru, který obsahuje data o strukturách DNA. Na každém řádku souboru jsou dvojtečkou oddělena metadata pro unikátní strukturu podle níže uvedeného vzoru a formátu. Druhým argumentem je kód DNA struktury, kterým začíná záznam metadat na řádku. Po spuštění skript vyzve uživatele k zadání desetinného čísla (jako oddělovač desetinných míst předpokládejte tečku). Skript v datovém vstupním souboru vyhledá a zpracuje příslušný řádek metadat podle zadaného kódu struktury a na výstup vypíše metadata přesně podle níže uvedeného formátu (viz Ukázka výstupu). Odevzdejte přímo soubor se skriptem.
(1 bod za každý řádek výstupu)

Ukázka vstupního souboru 'vstup.txt':
... (záznamům může předcházet libovolný počet řádků)
1ZFF:GCT duplex B-DNA:0.9:F. Hays, A. Teegarden, Z. Jones, M. Harms:2005-05-10
1BNA:Structure of a B-DNA dodecamer:1.9:T. Takano, C. Broka, S. Tanaka, K. Itakura:1981-05-21
3WBO:Crystal structure analysis of the Z-DNA hexamer:0.8:T. Chatake:2014-05-14
4HIG:Ultrahigh-resolution crystal structure of Z-DNA in complex:1.2:P. Drozdzal, M. Gilski, R. Kierzek, L. Lomozik:2013-06-05
...

Ukázka použití skriptu:
struktura vstup.txt 1BNA

Výzva shellu:
Zadejte desetinne cislo: 1.3

Ukázka výstupu:
struktura = 1BNA                                        # kód struktury beze změny
nazev = Structure of a B-DNA dodecamer                  # název beze změny
rozliseni = 1.9 + 1.3 = 3.2                             # původní hodnota a hodnota zvětšená o uživatelem vložené číslo
autori = T. TAKANO, C. BROKA, S. TANAKA, K. ITAKURA     # jména autorů převedena na velká písmena
rok = 1981                                              # z celého datumu vypíše pouze rok

## Assignment 11

1. S využitím konstrukce 'if' napište skript s názvem 'cislo.sh', který otestuje vstup zadaný uživatelem. Skript nepřijímá žádné argumenty. Po spuštění skript vyzve uživatele k zadání vstupu. Pokud vstup není číslo, ukončí se s hláškou, že se nejedná o číselnou hodnotu (1 bod). Pokud je vstup číslo, skript vypíše, jestli je celé nebo desetinné (jako oddělovač desetinných míst předpokládejte tečku nebo čárku) (1 bod). Pokud je číslo desetinné, dále se nic netestuje a skript se ukončí. Pokud se jedná o celé číslo, skript dále vypíše, jestli je kladné nebo záporné (1 bod), dále jestli je sudé nebo liché (1 bod), a kolik má číslic (1 bod).

(TIP: počet znaků řetězce lze získat například pomocí stringové operace v rámci expanse parametru: a=-159; echo ${#a};)

Ukázka použití skriptu:
cislo.sh

Výzva shellu:
Zadejte hodnotu: -159

Ukázka výstupu:
Vstup je cele cislo.
Cislo je zaporne.
Cislo je liche.
Pocet cislic: 3

## Assignment 12

## Assignment 13

## Assignment 14
