# Diskrétní matematika

* [Invitation to Discrete Mathematics by Jiří Matoušek and Jaroslav Nešetřil](https://global.oup.com/academic/product/invitation-to-discrete-mathematics-9780198570431)

## Obsah
- [Dělitelnost, gcd a lcm a jejich vlastnosti, (rozšířený) Euklidův algoritmus, prvočísla a faktorizace, kongruence modulo m](#dělitelnost,-gcd-a-lcm-a-jejich-vlastnosti,-(rozšířený)-Euklidův-algoritmus,-prvočísla-a-faktorizace,-kongruence-modulo-m)
- [Inverze v modulární aritmetice, vlastnosti prvočísel, Malá Fermatova a Eulerova věta a jejich použití, výpočet velkých mocnin modulo m, úvod k lineárním diofantickým rovnicím](#inverze-v-modulární-aritmetice,-vlastnosti-prvočísel,-Malá-Fermatova-a-Eulerova-věta-a-jejich-použití,-výpočet-velkých-mocnin-modulo-m,-úvod-k-lineárním-diofantickým-rovnicím)
- [](#)

### Konečné tělěso

### Relace dělitelnosti

## Dělitelnost, gcd a lcm a jejich vlastnosti, (rozšířený) Euklidův algoritmus, prvočísla a faktorizace, kongruence modulo m

### LCM Nejmenší společný násobek

- pokud
$$\ a \div n \wedge b \div n \Rightarrow lcm(a, b) \div n$$

### GCD Největší společný dělitel

 
- $$gcd \left( \frac{a}{gcd(a,b)}, \frac{b}{gcd(a,b)}\right) = 1$$

- $$gcd(a,b)$$
  +  je nejmenší kladné řešení m*a + n*b$$

**Bezoutova rovnost**
- $$gcd(a,b) = m \cdot a + n \cdot b; \quad a,b \in \mathbb{Z}$$

- $$a \div (b \cdot c) ^ {gcd(a,b)} = 1 => a/c$$

### EA - Euklidův algoritmus

```
a > b > 0
r0 = a
r1 = b
rn = rn-2 mod rn-1
```

### EEA - rozšířený euklidův algoritmus (REA)

|    r     | α = 254| β = 158| q |
|----------|--------|--------|---|
| r0 = 254 |    1   |    0   |   |
| r1 = 158 |    0   |    1   | 1 |
| r2 =  96 |    1   |   -1   | 1 |
| r3 =  62 |   -1   |    2   | 1 |
| r4 =  34 |    2   |   -3   | 1 |
| r5 =  28 |   -3   |    5   | 1 |
| r6 =   6 |    5   |   -8   | 4 |
| r7 =   4 |  -23   |   37   | 1 |
| r8 =   2 |   28   |   45   | 2 |
| r8 =   0


### Základní věta aritmetiky

- faktorizace, kanonický rozklad
- každé složené číslo se dá napsat jako rostoucí posloupnost prvočísel 

### Kongruence mod m

- $$a \sim b \mod m \equiv m/a-b$$

## Inverze v modulární aritmetice, vlastnosti prvočísel, Malá Fermatova a Eulerova věta a jejich použití, výpočet velkých mocnin modulo m, úvod k lineárním diofantickým rovnicím

### Malá fermatova věta

- prvočíselné (p) a něco nesoudělného (a) gcd(a,p)=1
    + $$a^p = 1 \mod p$$
- $$5^{203} \mod 101 = 5^{100^2}+{5^3} \mod 101 = 125 \mod 101 = 24$$

### Eulerova věta

Φ(m) - eulerova funkce
    - počet čísel z množiny {1,2,..  m} s m nesoudělných
    - p prvočíslo, Φ(p) = p - 1
- $$a^Φ(m) \equiv 1 \mod m$$
