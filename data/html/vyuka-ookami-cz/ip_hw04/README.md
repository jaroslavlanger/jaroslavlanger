# HW 04 - Použití Canvas API

## Zadání

Vyrobte HTML-stránku, která bude na pohyby myši, resp. pohyby prstu či stajlusu, nad kanvasem vykreslovat čáru ve vybrané barvě. 

Přitom:

Pohyb myši zachycuje událost mousemove.

Výběr barev zajistěte buď nějakým klikátkem (odkazy, tlačítka…) nebo třebas kontextovým menu.

PS: Událost mousemove bude pravděpodobně velmi náročná a cesta myši/prstu se nebude stíhat vykreslovat úplně celá. Lepší řešení je místo malých čtverečků na každou tuto zpracovanou událost nakreslit spojnici s posledním vykresleným místem. Ze stejného důvodu bude sice čára lomená, protože prohlížeč nestihne zpracovat kompletní pohyb myši/prstu, ale výsledek bude vypadat lépe.

PPS: Při přenosu kódu na mobily/tablety bude vhodné nahradit události myši událostmi dotyku (tedy rodinou událostí touch…).

Stránka by měla běžet v telefonu a kreslení fungovat prstem.

PS: Přepínání barev je bonus. Vhodné události pro kreslení jedním prstem jsou nejspíše pointer, touch je vhodný spíše až pro víceprsté.

[source](http://vyuka.ookami.cz/priklady/html/drawing.xml)