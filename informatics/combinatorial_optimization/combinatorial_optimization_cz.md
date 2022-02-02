# Kombinatorická optimalizace

## Obsah

- [Kombinatorické problémy a algoritmy](#kombinatorické-problémy-a-algoritmy)
  - [Terminologie kombinatorických problémů](#terminologie-kombinatorických-problémů)
  - [Charakterizace problému](#charakterizace-problému)
  - [Problém batohu](#problém-batohu)
  - [Typy problémů](#typy-problémů)
  - [Problém splnitelnosti (SAT - satisfiability)](#problém-splnitelnosti-sat---satisfiability)
- [Třídy P a NP](#třídy-p-a-np)
  - [Výpočetní modely](#výpočetní-modely)
  - [Třída P](#třída-p)
  - [Třída NP](#třída-np)
  - [co-NP](#co-np)
- [NP-úplné (NPC) a NP-těžké (NPH) problémy](#np-úplné-npc-a-np-těžké-nph-problémy)
  - [Karpova redukce](#karpova-redukce)
  - [Třída NP-úplný (NPC)](#třída-np-úplný-npc)
  - [Cookova věta](#cookova-věta)
  - [Třída NPO](#třída-npo)
  - [Třída PO](#třída-po)
  - [Turingova redukce](#turingova-redukce)
  - [Třída NP-těžký (NPH)](#třída-np-těžký-nph)
  - [Třída NPI](#třída-npi)
- [Pseudopolynomiální, aproximativní a randomizované algoritmy](#pseudopolynomiální-aproximativní-a-randomizované-algoritmy)
  - [Pseudopolynomiální algoritmy](#pseudopolynomiální-algoritmy)
  - [Aproximativní algoritmy, aproximativní problémy a jejich třídy](#aproximativní-algoritmy-aproximativní-problémy-a-jejich-třídy)
  - [Relativní kvalita relativní chyba](#relativní-kvalita-relativní-chyba)
  - [PTAS (Polynomial Time Approximation Scheme)](#ptas-polynomial-time-approximation-scheme)
  - [FPTAS (Fully Polynomial Time Approximation Scheme)](#fptas-fully-polynomial-time-approximation-scheme)
- [TODO](#todo)
  - [Paretooptimální](#paretooptimální)
  - [Multimodální optimalizace](#multimodální-optimalizace)

## Kombinatorické problémy a algoritmy

- Kombinatorická matematika

### Terminologie kombinatorických problémů

- PROBLÉM
- INSTANCE
- KONFIGURACE
- VSTUPNÍ, VÝSTUPNÍ PROMĚNNÉ
- KONFIGURAČNÍ PROMĚNNÉ
- OMEZUJÍCÍ PODMÍNKY
- OPTIMALIZAČNÍ KRITÉRIUM
- ŘEŠENÍ, OPTIMÁLNÍ A SUBOPTIMÁLNÍ ŘEŠENÍ

### Charakterizace problému 

- vstupní proměnné
- konfigurační proměnné (konfigurace)
- výstupní proměnné
- omezení
- optimalizační kritérium, pokud je třeba

[Moodle]([Moodle](https://moodle-vyuka.cvut.cz/course/view.php?id=3930))

### Problém batohu


### Typy problémů

- rozhodovací
- konstruktivní
- enumerativní

- optimalizační - pokud je zadáno optimalizační kriterium

### Problém splnitelnosti (SAT - satisfiability)

v boolovské konjuktivní normální formě

**svědek** - konfigurace příkladu

#### Optimalizační verze SAT

(maximálně n 1)

#### Max SAT

nejde o splnění sat, ale o maximální počet splněných klauzulí

#### Steinerův problém v pravoúhlé metrice

- mohou se objevit spojité podčásti problémů 

#### Diskrétní jádro problému

- 

## Třídy P a NP

### Výpočetní modely

### Třída P

- PSPACE
- EXPTIME

### Třída NP

Příklad
- Hamiltonova kružnice v grafu

### co-NP

## NP-úplné (NPC) a NP-těžké (NPH) problémy

### Karpova redukce

### Třída NP-úplný (NPC)

### Cookova věta

### Třída NPO

### Třída PO

### Turingova redukce

### Třída NP-těžký (NPH)

### Třída NPI

## Pseudopolynomiální, aproximativní a randomizované algoritmy

### Pseudopolynomiální algoritmy

### Aproximativní algoritmy, aproximativní problémy a jejich třídy

#### Algoritmu APR-KNAP

Polynomiální složitost
- Výsledné řešení má cenu
- $\geq 50 \%$ optimálního řešení

### Relativní kvalita relativní chyba

- `C(S)`   - hodnota opt. kritéria řešení S
- `APR(I)` - aprox. řešení instance I
- `OPT(I)` - optimální řešení instance I

#### Relativní kvalita R

Algoritmus APR má relativní kvalitu R, jestliže

$$
R \geq_{\forall I}\max\left\{ 
    \frac{C(APR(I))}{C(OPT(I))},
    \frac{C(OPT(I))}{C(APR(I))}
\right\}
$$

#### Relativní chyba $\varepsilon$

Algorimus APR má relativní chybu $\varepsilon$ jesliže

$$
\varepsilon \geq_{\forall I}\max\left\{ 
    \frac
        {|C(APR(I))-C(OPT(I))|}
        {\max\{C(OPT(I)),C(APR(I))\}}
\right\}
$$

#### Vztah R a $\varepsilon$

$$ \varepsilon = 1 - \frac{1}{R} $$

#### Algorithm A+

Problém uzlového pokrytí: dán graf G=(V,E);
sestrojit V’⊆V takovou, že
|V’| = min a ∀(u,v)∈E, u∈V’ nebo v∈V’.

```
1.  V’ = ∅
2.  dokud E != ∅
3.    zvol hranu (u,v) ∈ E
4.    V’ = V’∪{u,v}
5.    odstraň z E hrany incidentní s u nebo v
```

#### Algorithm A++

```
1.  V’ = ∅
2.  dokud E ≠ ∅
3.    zvol hranu (u,v) ∈ E tak, že deg(u) + deg(v) = max.
4.    V’ = V’∪{u,v}
5.    odstraň z E hrany incidentní s u nebo v
```

#### Algoritmus B+

```
1.  V’ = ∅
2.  dokud E ≠ ∅
3.    zvol uzel v ∈ V- V’, tak, že deg(v) = max.
4.    V’ = V’∪{v}
5.    odstraň z E hrany incidentní s v
```

### PTAS (Polynomial Time Approximation Scheme)

### FPTAS (Fully Polynomial Time Approximation Scheme)

## Tabu prohledávání

## TODO

### Paretooptimální 

### Multimodální optimalizace

- hamiltonova kružnice
- bi-ag2 projít slajdy
- bi-zum

