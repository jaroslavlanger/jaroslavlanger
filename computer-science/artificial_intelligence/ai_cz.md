# Umělá inteligence

## Obsah <!-- omit in toc -->
- [Přednáška 1](#přednáška-1)
  - [Definice ai](#definice-ai)
  - [Historie](#historie)
  - [Typy artefaktů](#typy-artefaktů)
  - [Úrovně artefaktů](#úrovně-artefaktů)
  - [Řešení úloh - tvorba pasivních artefaktů](#řešení-úloh---tvorba-pasivních-artefaktů)
  - [Formulace úlohy](#formulace-úlohy)
  - [Neinformované prohledávání](#neinformované-prohledávání)
- [Přednáška 2](#přednáška-2)
  - [Constrains satisfaction problem (CSP)](#constrains-satisfaction-problem-csp)
  - [Chronologický backtracking](#chronologický-backtracking)
  - [Filtrace domén](#filtrace-domén)
  - [Arc consistency](#arc-consistency)
  - [Heuristiky](#heuristiky)
  - [Využítí struktury](#využítí-struktury)
  - [Složitost CSP](#složitost-csp)
  - [Optimalizace CSP](#optimalizace-csp)
  - [Spojité CSP](#spojité-csp)
  - [Programování s omezeními](#programování-s-omezeními)
  - [CSP, A*, Simulované žíhání](#csp-a-simulované-žíhání)
- [Přednáška 3](#přednáška-3)
  - [Back jumping](#back-jumping)
  - [Dynamický backjumping](#dynamický-backjumping)
  - [Závislosti (nogoody)](#závislosti-nogoody)
  - [Závislostmi řízený backtracking](#závislostmi-řízený-backtracking)
  - [Logika nogoodů](#logika-nogoodů)
  - [Zobecněná hranová konzistence (GAC)](#zobecněná-hranová-konzistence-gac)
  - [Globální podmínky](#globální-podmínky)
  - [Symetrie](#symetrie)
- [Přednáška 4](#přednáška-4)
  - [Paradigmata](#paradigmata)
  - [Výroková logika](#výroková-logika)
  - [Výrokové formule### Výrokové formule](#výrokové-formule-výrokové-formule)
  - [Ohodnocení proměnných](#ohodnocení-proměnných)
  - [Logické spojky](#logické-spojky)
  - [Pravdivost, Splnitelnost](#pravdivost-splnitelnost)
  - [Normální tvary](#normální-tvary)
  - [Cejtinova transformace](#cejtinova-transformace)
  - [Jednotkové klauzule](#jednotkové-klauzule)
  - [Unit propagation (UP)](#unit-propagation-up)
  - [Jednoduché splňování DPLL](#jednoduché-splňování-dpll)
  - [Učení a skoky zpět CDCL](#učení-a-skoky-zpět-cdcl)
  - [Trojice paradigmat](#trojice-paradigmat)
- [Přednáška 5](#přednáška-5)
  - [Podrobněji o CDCL](#podrobněji-o-cdcl)
  - [Analýza konfliktu](#analýza-konfliktu)
  - [Vynucující klauzule](#vynucující-klauzule)
  - [Unikátní implikační bod UIP](#unikátní-implikační-bod-uip)
  - [Volíme konfliktní klauzuli](#volíme-konfliktní-klauzuli)
- [Přednáška 6 - Plánování](#přednáška-6---plánování)
  - [Plánování](#plánování)
  - [Akce](#akce)
  - [Plánovací doména](#plánovací-doména)
  - [Dopředné plánování](#dopředné-plánování)
  - [Zpětné plánování](#zpětné-plánování)
  - [Liftování - s proměnnými](#liftování---s-proměnnými)
  - [Plánování v prostoru plánů](#plánování-v-prostoru-plánů)
  - [Složitost](#složitost)
- [Přednáška 7. - Plánovací algoritmy](#přednáška-7---plánovací-algoritmy)
  - [Strom dosažitelných stavů](#strom-dosažitelných-stavů)
  - [Plánovací graf](#plánovací-graf)
  - [Vzájemné vyloučení MUTEX](#vzájemné-vyloučení-mutex)
  - [Graphplan](#graphplan)
  - [Expanze plánovacího grafu](#expanze-plánovacího-grafu)
  - [Graphplan - kompletní](#graphplan---kompletní)
  - [Plánování jako SAT](#plánování-jako-sat)
  - [Satplan](#satplan)
  - [Plánování jako CSP](#plánování-jako-csp)
  - [Hierarchické plánování HTN](#hierarchické-plánování-htn)
- [Přednáška 8. - Automatické uvažování (v logice)](#přednáška-8---automatické-uvažování-v-logice)
  - [Nerozhodnutelnost](#nerozhodnutelnost)
  - [Logika prvního řádu (FOL)](#logika-prvního-řádu-fol)
  - [Formule prvního řádu](#formule-prvního-řádu)
- [TODO](#todo)

Nahrát na gitlab, přidat cvičícího jako pozorovatele.
(Můžu odevzdat klidně ještě vysavač)
[results](https://users.fit.cvut.cz/surynpav/teaching/restricted_2020-2021-ZS/results.php)

## Přednáška 1

### Definice ai

Pokus nejen o porozumění ale i o sestrojení umělé inteligence.

#### Rozdělení

Uvnitř: myslet jako člověk | myslet racionálně
Venku: jednat jako člověk | jednat racionálně

#### Nebude strojové učení

- nebudou neuronové sítě, SVM, rozhodovací stromy

### Historie

#### Předhistorie

- Filosofie
- Matematika
- Ekonomie
- Neurovědy
- Počítačové inženýrství
- Teorie řízení a kybernetika
- Lingvistika

#### Historie ai

- Formování (1943)
  - Turing, von Neuman
- Zrození (1956)
  - Logic theorist - Newell Simon
- Nadšení
- Vystřízlivění
- počítač 5. generace 
  - (JP) logické programování, Prolog
- Rozmach (1990-...)

#### Touringův test

###

- řešení úloh prohledáváním
- splňování omezujících podmínek
- splnitelnost
- automatické plánování
- modelování úloh
- zpracování přirozeného jazyka
- robotika

#### ai jako tvorba

Vytváření počítačových artefaktů

### Typy artefaktů

- pasivní - nevykazuje aktivitu (mapa)
    + skvěle se testují, vychází z lokálních vlastností
- aktivní - vykazuje aktivitu (hrací agent)
    + obtížné testovat správnost

### Úrovně artefaktů

0.  - aktivní - člověk hraje za stroj
    - pasivní - člověk si vytvoří sám
1.  - aktivní - člověk napíše program co hraje šachy
    - pasivní - člověk napíše program co něco spočítá
2.  - člověk vytvořil robota, ten vytváří kód
3.  - robot už vytvořil robota, který píše kód 

### Řešení úloh - tvorba pasivních artefaktů

- Formulace cíle
- formulace úlohy
- řešení úlohy
- provedení úlohy

### Formulace úlohy

- situace (agent je v Rumunsku, má si užít dovolenou)
- zjednodušení (jet do bukurešti)

#### Hračkové příklady

- vysavač
- 8 dam

#### Reálné příklady

- Amazon roboti

### Neinformované prohledávání

- prohledávání do hloubky
- prohledávání do šířky
- iterované prohledávání do hloubky
- prohledávání heuristicky (A*)
- RBFS

**Závěrečné poznámky**

- pozor na opakovatelné stavy
- prohledávání s využitím externí paměti
    + organizace těchto dat
- heuristika musí být monotóní a jednoznačná?
- obousměrné prohledávání

## Přednáška 2

### Constrains satisfaction problem (CSP)

Splňování omezení

Tvorba pasivních artefaktů.

(X, D, C)
- X - konečná množina proměnných - vlastnosti rozhodující o řešení
- D - konečná doména (možnosti)
- C - množina podmínek nad X 
    + relací - podmnožina kartézského součinu domény

Konjunkce všech podmínek

#### Definice

- Stav S' - částečné ohodnocení proměných
- Konzistentní stav - všchny podmínky splněny
- počáteční stav - prázdné ohodnocení proměných
- akce - 
- cílový stav - všechny proměnné ohodnoceny

### Chronologický backtracking

- DFS v kontextu CSP
    + dopředný chod - přiřazují se proměnné
    + zpětný chod - odpřiřadí se poslední proměnná a zkouší se znovu
- složitost velikost domény na počet proměnných

### Filtrace domén

#### Forward checking

- při akci zkontroluji pro všechny dotčené podmínky dotčené proměnné a vyškrtneme z pracovní domény proměné (nesplňující ohodnocení)
- kontrola podpory, kontrola jestli hodnota dotčené proměnné neztratila podporu

### Arc consistency

Hranová konzistence

- Kontrolujeme hranu z X1 do X2
(pro každou proměnou v pracovní doméně hledáme podporu, taková D2, že s D1 splňují podmínku)
- dvě proměné jsou 
- cíl celý problém má být hranově konzistentní
- všechny hrany musejí být oboustranně konzistentní (všchny hodnoty jedné proměnné mají podporu a opačně)
    + kontrola zasažených hran

#### algoritmus AC3 

- pro frontu hran, hledá podporu

### Heuristiky

#### Výběr nejvíce omezené proměnné v algoritmu 

- ohodnocujeme doménu, která má nejméně hodnot

#### Výběr klíčové proměnné

#### Hodnoty vybíráme tak, abychom co nejdříve narazili na řešení

### Využítí struktury

#### Výběrem proměnných rozložit na komponenty

### Složitost CSP

NP úplný problém

### Optimalizace CSP

branch and bound nad celou arc consistency, ...

### Spojité CSP

CSP s rozvrhováním - výrobní linky atd

### Programování s omezeními

### CSP, A*, Simulované žíhání

- Simulované žíhání - lokální, dobrý, na problémy co nejdou řešit systematicky
- A* - vymyslet heuristiku pro NP problém je problematické
- CSP - jak šité na barvení mapy

## Přednáška 3

#### CSP: SPLŇOVÁNÍ OMEZENÍ

#### TECHNIKA BACKJUMPINGU V LISTU

### Back jumping
- spočítám konfliktní množinu
- listové řešení 
- nelistové řešení

### Dynamický backjumping

### Závislosti (nogoody)

- Uvažujme částečné ohodnocení proměnných
$S’$. Nechť Conf $= \{y_1,y_2,..,y_k\}$ je množina konfliktních proměnných vzhledem k ohodnocení $S’$.
  - nogood podmínka zakazující vytvořit nerozšířitelné ohodnocení

### Závislostmi řízený backtracking

### Logika nogoodů

- příklad  $y1 ≠ S’(y1) ∨ y2 ≠ S’(y2) ∨ … ∨ yk ≠ S’(yk)$
- specifické nogoody lze skládat do obecnějších 
  - **rezoluční pravidlo**

### Zobecněná hranová konzistence (GAC)

### Globální podmínky

#### Propagace v All-different

### Symetrie

- rozbíjení symetrií

## Přednáška 4

### Paradigmata

- omezující podmínky
- inteeger programming
- splnitelnost

### Výroková logika

- Jazyk logiky
  + proměnné
  + spojky
  + pomocné spojky

### Výrokové formule### Výrokové formule

- formule
- pravidla lze chápat jako bezkontextovou gramatiku

### Ohodnocení proměnných

- interpretace
  + obor hodnot M a přiřazení
  + interpretace $\alpha$ výrokových proměnných (vyskytujícíh se ve formuli $\varphi$)

### Logické spojky

- používáme konvenci
  - False = 0, True = 1
- kolik může být různých binárních logických spojek?

### Pravdivost, Splnitelnost

- $\alpha$ ohodnocení formule $\varphi$
  - $\alpha \vDash \varphi$ znamená $\varphi$ je splněna pro ohodnocení $\alpha$
- $\varphi$ je splnitelná
- $\varphi$ je pravdivá
- $\varphi$ je sporná

#### Proč logika

- mnoho úloh z praxe je NP
- konkrétní úlohy
  - formální verifikace
  - bioinformatika / genetika
  - plánování

### Normální tvary

- CNF - konjunktivní normální tvar
  - podobá se CSP
    - CDCL - conflict-driven clause learning
  - literál
  - klauzule
  - term
- převod na ekvivalentní v CNF

### Cejtinova transformace

- převod na ekvivalentní CNF je nepraktický
  - stačí ekvivalentně splnitelná
- postupujeme podle derivačního stromu $\varphi$

#### Pomocné proměnné

- pro každý vnitřní uzel derivačního stromu $\varphi$ zavedeme pomocnou proměnnou $a_i$ 

### Jednotkové klauzule

- uvažujeme částečně ohodnocené proměnných

    $\alpha': V \to \{True, False\}$ a klauzuli $c$

### Unit propagation (UP)

Jednotková propagace

- chceme splňovat formuli ve tvaru CNF
$$
(\neg u \lor w) \land (u \lor v) \land (u) \land (\neg w \lor z)
$$

### Jednoduché splňování DPLL

- backtracking s jednoduchou propagací a propagací čistých proměnnch (BT + UP + PURE)
  - čistá proměnná vyskutuje se pouze jako pozitivní, nebo jako negativní (lze okamžitě ohodnotit {0,1})

#### Důvody konfliktu

- předchůdcovská klauzule (antecedent clause)
  - jetliže byl literál $l$ ohodnocen jednotkovou propagací kvůli klauzuli $c$, pak $c$ je předchůdcovská klauzule
- implikační graf pro $\alpha'$
  - hrany $(x_i, y)$ ukazují, že $y$ byla ohodnocena kvůli jednotkovou propagací, kvůli ohodnocením $x_1, x_2, ..., x_k$

#### Implikační graf

- konflikt K

#### Učení klauzulí

- hranový řez v implikačním grafu, který odděluje rozhodovací vrcholy a K, určuje konfliktní klauzuli
  - speciální případ nogoodů
  - konfliktní klauzuli c si můžeme zapamatovat, neopakovat chybu
- konfliktní klauzuli lze využít k spětnému skoku


### Učení a skoky zpět CDCL

conflict-driven clause learning

#### Splnitelnost s garancí

### Trojice paradigmat

- CSP
  - výhody
    - prohledávací algoritmy
  - nevýhody
    - heterogenní, obžížné vytvořit řešič
    - slabší učení
- SAT
  - výhody
    - obrovksá homogenita, 
    - dá se udělat propracovaný řešič, silné učení
  - nevýhody
    - absence aritmetiky
    - těžké integrovat vlastní heuristiku
- IP (integer programming) + OR (operation research)
  - výhody
    - vynikající aritmetika, homogenní, škálovatelnost
  - nevýhody
    - slabé učení

## Přednáška 5

### Podrobněji o CDCL

- DECIDE
  - ohodnotí další neohodnocenou proměnnou
- BCP (Boolean Constraint Propagation)
  - jednotková propagace
- BackTrack(level)
  - zruší všechna ohodnocení na úrovni `> level`

### Analýza konfliktu

- hranový řez oddělující K a všechny rozhodovací vrcholy R (jinak můžeme vést libovolně)
  - určuje nogood
- Obecné požadavky
  - krátké klauzule (aby se nám vešly do paměti)
    - podporuje jednotkovou propagaci

### Vynucující klauzule
(asserting conflict clause)
- obsahující jediný literál z aktuální rozhodovací úrovně

### Unikátní implikační bod UIP

- vzhledem k aktuální úrovni definujeme UIP 
  - vrchol různý od K
  - všechny cesty z rozhodovacího vrcholu d K vedou přes něj
- vlastnosti
  - existuje (přinejhorším sám rozhodovací vrchol)
  - může jich být víc
    - zajímá nás nejbližší ke K

### Volíme konfliktní klauzuli

## Přednáška 6 - Plánování

- [Přednáška video](https://web.microsoftstream.com/video/bf8065a9-29c4-4bca-b68f-f64f91fcac43)

### Plánování

### Akce

### Plánovací doména

### Dopředné plánování

### Zpětné plánování

### Liftování - s proměnnými

### Plánování v prostoru plánů

### Složitost

## Přednáška 7. - Plánovací algoritmy

- [Přednáška video](https://web.microsoftstream.com/video/490dbb58-706b-4c28-8349-c4507e481095?list=user&userId=2b6729ad-4995-49d0-b672-dc013e5e8485)

### Strom dosažitelných stavů

### Plánovací graf

### Vzájemné vyloučení MUTEX

### Graphplan

### Expanze plánovacího grafu

### Graphplan - kompletní

### Plánování jako SAT

### Satplan

### Plánování jako CSP

### Hierarchické plánování HTN

## Přednáška 8. - Automatické uvažování (v logice)

- ATP
- APC

### Nerozhodnutelnost

### Logika prvního řádu (FOL)

- Jazyk
  - Proměnné pro individua
    - x,y,z jsou prvky nosné množiny (univerza).
  - Spojky
    - unární, binární, ...
      - negace
      - konjunkce, disjunkce, implikace...
  - Kvantifikátory
    - Všeobecný, existenční
  - Pomocné symboly
    - Závorky, tečka.
- Signatura
  - Symboly pro funkce (transformace individuí)
    - f,g,h,+,*
  - Symboly pro predikáty (vlastnosti individuí)
    - R,S <,=

### Formule prvního řádu

- Termy
  - Proměnná je term
  - jestliže f je funkční symbol arity n a t1,t2,...,tn jsou termy, potom
    - pak f(t1, t2, ..., tn) je taky term.
- Atomy
  - jestliže p je predikátový symbol arity n a t1,t2,...,tn jsou termy, potom
    - p(t1, t2, ..., tn) je atomická formule (atom).
- Formule je slovo (konečná posloupnost symbolů).
  1) atomická formule je formule
  2) jestliže p a q jsou formule, potom
    - $\lnot p, (p \land q), (p \lor q), (p \Leftrightarrow q), (p \Rightarrow q)$
  3) jestliže p je formule a x je proměnná
    - $\forall x (p(x))$ a $\exist x (p(x))$ jsou formule.
  - všechny formule vzniknou konečným počtem aplikací pravidel 1-3.

## TODO

- bi-zum (a*)
- bi-ag2
- lineární programování

