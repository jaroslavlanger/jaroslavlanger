# Nelineární optimalizace a numerické metody

- [Main page](http://mech.fsv.cvut.cz/~jk/minon2021.html)
- [Homework material](http://mech.fsv.cvut.cz/~jk/MINON/)
  - mat_cct_7650.txt, mat_cct_120600
  - mat_ps_8200.txt, pat_ps_128800.txt

- [Mathematical Methods for Engineers II (ocw.mit)](https://ocw.mit.edu/courses/mathematics/18-086-mathematical-methods-for-engineers-ii-spring-2006/video-lectures/)

- [Skyline Storage for symmetric and non-symmetric matrices (netlib.org jackDongarra)](http://www.netlib.org/utk/people/JackDongarra/etemplates/node378.html)


## Obsah

- [Přednáška 1](#přednáška-1)
  - [Funkce](#funkce)
  - [Derivace funkce](#derivace-funkce)
  - [Extrémy funkcí](#extrémy-funkcí)
  - [Kvadratické funkce n proměnných](#kvadratické-funkce-n-proměnných)
  - [metoda největšího spádu](#metoda-největšího-spádu)
- [Přednáška 2](#přednáška-2)
  - [metoda sdružených gradientů](#metoda-sdružených-gradientů)
- [Přednáška 3](#přednáška-3)
  - [obyčejné diferenciální rovnice](#obyčejné-diferenciální-rovnice)
  - [metoda konečných diferencí](#metoda-konečných-diferencí)
  - [funkcionály](#funkcionály)
  - [Eulerova nutná podmínka pro extrém](#eulerova-nutná-podmínka-pro-extrém)
  - [metoda konečných prvků](#metoda-konečných-prvků)
- [Přednáška 4](#přednáška-4)
  - [ukládání matic v počítači](#ukládání-matic-v-počítači)
  - [metoda konstantního pásu](#metoda-konstantního-pásu)
  - [metoda proměnné pásu - skyline](#metoda-proměnné-pásu---skyline)
  - [kompresované řádky](#kompresované-řádky)
  - [symetrické kompresované řádky](#symetrické-kompresované-řádky)
- [Přednáška 5](#přednáška-5)
  - [parciální diferenciální rovnice](#parciální-diferenciální-rovnice)
  - [klasifikace rovnic](#klasifikace-rovnic)
  - [metoda konečných diferencí](#metoda-konečných-diferencí-1)
  - [trojúhelníkový prvek pro Poissonovu rovnici](#trojúhelníkový-prvek-pro-poissonovu-rovnici)
- [Přednáška 6](#přednáška-6)
  - [integrace v čase](#integrace-v-čase)
  - [zobecněné lichoběžníkové pravidlo](#zobecněné-lichoběžníkové-pravidlo)
  - [Newmarkova metoda pro rovnice 2. řádu](#newmarkova-metoda-pro-rovnice-2-řádu)
  - [příklad](#příklad)
- [Přednáška 7](#přednáška-7)
  - [paralelní počítače](#paralelní-počítače)
  - [metody rozložení oblasti na podoblasti](#metody-rozložení-oblasti-na-podoblasti)
- [Přednáška 8](#přednáška-8)
  - [soustavy nelineárních algebraických rovnic](#soustavy-nelineárních-algebraických-rovnic)
- [TODO](#todo)

## Přednáška 1

### Funkce

### Derivace funkce

**Definice**: Nechť je funkce f(x), limita

$$
\frac{d f(x)}{d x} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
$$

se nazývá derivace funkce f(x) v bodě x, někdy značeno $f'(x)$.

#### Derivace některých funkcí

| $f(x)$        | $f'(x)$               |
| ---           | ---                   |
| $x^n$         | $nx^{(n-1)}$          |
| $\sin x$      | $\cos x$              |
| $\cos x$      | $- \sin x$            |
| $n^x$         | $n^x \cdot \ln n$     |
| $\log_{n} x$  | $\frac{1}{x \ln n}$   |

**Definice**: Bod $x \in D$ se nazývá stacionárním právě když $f'(x) = 0$.

### Extrémy funkcí

#### Konvexní a konkávní funkce

**Definice**: Funkce $f(x)$ se nazývá konvexní na množině $M \subset D$, když $\forall x_{1},x_{2} \in D, \alpha \in (0,1)$ platí

$$
f(\alpha x_{1} + (1-\alpha)x_{2}) \le \alpha f(x_{1}) + (1-\alpha)f(x_{2})
$$

**Věta**: jeli $f'(x) > 0$ funkce je v bodě x rostoucí.

**Věta**: jeli $f'(x) < 0$ funkce je v bodě x klesající.

**Věta**: jeli $f''(x) > 0$ funkce je v bodě k ryze konvexní.

**Věta**: jeli $f''(x) < 0$ funkce je v bodě k ryze konkávní.

**Věta**: jeli $f'(x) = 0 \wedge f''(x) > 0$ funkce má v bodě x lokální minimum.

**Věta**: jeli $f'(x) = 0 \wedge f''(x) < 0$ funkce má v bodě x lokální maximum.

### Kvadratické funkce n proměnných

$$
    f(x) = \frac{1}{2} a_{1,1}x_{1}^{2} + \frac{1}{2} a_{1,2}x_{1}x_{2} + \dots + \frac{1}{2} a_{1,n}x_{1}x_{n} \\
    + \frac{1}{2} a_{2,1}x_{2}x_{1} + \frac{1}{2} a_{2,2}x_{2}^{2} + \dots + \frac{1}{2} a_{2,n}x_{2}x_{n} \\
    \dots \\
    + \frac{1}{2} a_{n,1}x_{n}x_{1} + \frac{1}{2} a_{n,2}x_{n}x_{2} + \dots + \frac{1}{2} a_{n,n}x_{n}^{2} \\
    + b_{1}x_{1} + b_{2}x_{2} + \dots + b_{n}x_{n} + c
$$

potom se dají proměnné $x_{1}, x_{2}, \dots x_{n} \textrm{napsat jako vektor} \quad \textbf{v}$

a kvadratická rovnice n proměnných se dá maticově napsat jako

$$
    f(x) = x^{T}Ax + x^{T}b + c
$$

$c$ nemění vlastnosti extrému, pouze jeho absolutní hodnotu, proto se dále předpokládá, že $c = 0$.

**Definice**: Matice $A^{n,n}$ je pozitivně definitní, právě tehdy když pro libovolný nenulový vektor $x$ 
$$
    x \in R^{n}, x^TAx > 0
$$

**Poznámka**: Velmi mnoho inženýrských úloh se dá zkonstruovat tak, 
že se hledá minimum kvadratické rovnice o n neznámýchjako s pozitivně definitní maticí.

**Věta**: Matice $A^{n,n}$ je pozitivně definitní právě tehdy když jsou všechna její vlastní čísla kladná.

**def**: Matice $A$ je symetrická právě tehdy když $A = A^T$

### metoda největšího spádu

- inverzní matice se nikdy nepočítá, byla by plná, moc veklá (ostatní matice jsou řídké)

- determinant a kubická rovnice -> vlastní čísla
- tři rovnice -> valstní tři vektory

## Přednáška 2

### metoda sdružených gradientů

## Přednáška 3

### obyčejné diferenciální rovnice

### metoda konečných diferencí

### funkcionály

### Eulerova nutná podmínka pro extrém

### metoda konečných prvků

## Přednáška 4

### ukládání matic v počítači

### metoda konstantního pásu

### metoda proměnné pásu - skyline

### kompresované řádky

### symetrické kompresované řádky

## Přednáška 5

### parciální diferenciální rovnice

### klasifikace rovnic

### metoda konečných diferencí

### trojúhelníkový prvek pro Poissonovu rovnici

## Přednáška 6

### integrace v čase

### zobecněné lichoběžníkové pravidlo

### Newmarkova metoda pro rovnice 2. řádu

### příklad

## Přednáška 7

### paralelní počítače

### metody rozložení oblasti na podoblasti

## Přednáška 8

### soustavy nelineárních algebraických rovnic

## TODO

- vlatní číslo 
- vlastní vektor
- fundamentální matice
