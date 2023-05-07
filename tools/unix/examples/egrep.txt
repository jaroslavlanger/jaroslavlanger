#!/bin/sh
# Jaroslav Langer 
# 09/04/2019

# 1. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny IPv4 adresy. Předpokládejte následující formát a rozsah IP adres. Formát IPv4 adresy je x.x.x.x kde x je v rozsahu 0 až 255, v libovolné kombinaci na jednotlivých pozicích (např. 147.251.124.113 nebo 192.168.0.1 atd.). (1 bod)
egrep '[[:digit:]]{1,2}|[1-2][0-4][0-9]|25[0-5]' regexp.txt 

# 2. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechna desetinná čísla. Předpokládejte následující formát desetinných čísel. Číslo může, ale nemusí, začínat znaménkem plus nebo mínus. Následuje libovolný počet číslic, oddělovač desetinných míst (čárka nebo tečka) a končí maximálně dvěmi číslicemi. (1 bod)
# 
# 3. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny HTML tagy pro nadpis (header) včetně jejich případného obsahu a koncového tagu. To znamená tagy <h1>x</h1>, <h2>x</h2>, <h3>x</h3>, <h4>x</h4>, <h5>x</h5>, <h6>x</h6>, kde x je libovolný text. Uvažujte také variantu s velkými písmeny v názvu tagu, tedy <H1>x</H1> atp. (1 bod)
# 
# 4. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny časy zapsané v následujícím formátu. Formát je hh:mm:ss kde hh je hodina v rozsahu 00 až 23, mm je minuta v rozsahu 00 až 59 a ss je sekunda v rozsahu 00 až 59. Oddělovačem hodnot je dvojtečka a uvažujte pouze dvojciferné varianty čísel. (1 bod)
# 
# 5. Pro příkaz 'egrep' napište regulární výraz, který ve vstupu najde všechny emailové adresy. Uvažujte následující formát emailové adresy. Před zavináčem je text v rozsahu 4 až 15 znaků a obsahuje pouze alfanumerické znaky. Následuje zavináč, alfanumerický text v rozsahu 3 až 10 znaků, tečka a dvou- nebo třípísmenný kód domény. (1 bod)
