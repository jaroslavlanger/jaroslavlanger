# Statistics

* https://www.probabilitycourse.com/

* probability: mathematical modelling of randomness
* statistics: estimating probability to observations
* measurable (Borel) space:  $(X, \sigma\text{-algebra of }X)$
* $\sigma\text{-algebra}$: set of $X$'s subsets, closed under complement, union and intersection

---

Probability space $\mathcal{E}$

$$ \mathcal{E}=(\Omega, \mathcal{F}, \mathrm{P}) $$

* $\Omega$: sample space
* $\mathcal{F}$: event space, $\sigma\text{-algebra}$ of $\Omega$
* $\mathrm{P}$: probability $P:{\mathcal {F}}\to [0,1]$
  * non-negativity: $P(f) \geq 0, \forall f \in \mathcal {F}$
  * normalization: $\sum_{\omega \in \Omega}P(\{\omega\}) = 1$
  * $\sigma$-aditivity: $P(\bigcup_{\omega \in \Omega} \{\omega\}) = \sum_{\omega \in \Omega}P(\{\omega\})$

Conditional probability
---

$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

* Normalize the probability to space B.

```
              P(INTER(a, b))
P(a, gvn=b) = --------------
              P(b)
```

$$P(A | B) \cdot P(B) = P(A \cap B) = P(B | A) \cdot P(A)$$

Law of Total Probability
---

Being $B_1, B_2, B_3$ a partitions of $\Omega$, then

$$
\begin{align}
P(A) &= P(A_1) &+ P(A_2) &+ \dots &+ P(A_n) \\
&= P(A_1 \cap \Omega) &+ P(A_2 \cap \Omega) &+ \dots &+ P(A_n \cap \Omega) \\
&= P(A_1 \cap B_1) &+ P(A_2 \cap B_2) &+ \dots &+ P(A_n \cap B_3) \\
&= P(A_1 | B_1) \cdot P(B_1) &+ P(A_2 | B_2) \cdot P(B_2) &+ \dots &+ P(A_3 | B_3) \cdot P(B_3) \\
\end{align}
$$

Bayes theorem
---

$$
P(val_i | obs)
= \frac{P(obs | val_i) \cdot P(val_i)}
{\sum_{j=1}^{|obs|} P(obs_j | val_i) \cdot P(val_i)}
$$

```
                           P(obs_1d, gvn=val_1d[i]) * P(val_1d[i])
P(val_1d[i], gvn=obs_1d) = ----------------------------------------------
                           SUM(j=1, obs_cnt)(
                             P(obs_1d[j], gvn=val_1d[i]) * P(val_1d[i]) )
```

Chain rule
---

```
P(INTER(a, b, c)) = P(a, gvn=INTER(b, c)) * P(b, gvn=c) * P(c)

P(INTER(a, b, ..., n)) = P(a) * P(b, gvn=a) * P(c, gvn=INTER(a, b))
                         * ... * P(n, gvn=INTER(a, b, ..., n-1))
```


Probability tree
---

```
                       / P(k | s) = 0.7   => P(INTER(k, s)) = 0.21            
        / P(s) = 0.3  *                                                       
                       \ P(!k | s) = 0.3  => P(INTER(!k, s)) = 0.09           
OMEGA *                                                                       
                       / P(k | !s) = 0.1  => P(INTER(k, !s)) = 0.07           
        \ P(!s) = 0.7 *                                                       
                       \ P(!k | !s) = 0.1 => P(INTER(!k, !s)) = 0.63          
```

Independent events
---

```
P(INTER(a, b)) = P(a) * P(b) <=> P(a, gvn=b) = P(a) <=> P(b, gvn=a) = P(b)
```

* Independent vs. disjoint events
* Conditional independence

## Random Variable

Random variable X on (OMEGA, F, P), is function that for every outcome omega in OMEGA returns REAL value X(omega).

$$\{X \leq x\} \in \mathcal{F}, \forall x \in \mathbb{R}$$

* $P(X \leq x) = P(\{X \leq x\}) = P(\{\omega| X(\omega) \leq x, \forall \omega \in \Omega\})$
* $P(X = x) = P(\{X = x\}) = P(\{\omega| X(\omega) = x, \forall \omega \in \Omega\})$

```
P(X <= x) = P({X <= x}) = P({o for o in OMEGA if X(o) <= x})
P(X = x) = P({X = x}) = P({o for o in OMEGA if X(o) = x})
```

Cumulative Distribution Function
---

$F_X(x) = P(X \leq x)$

Discrete Random Variable Examples
---

* Bernoulli, Be(p), e.g. probability of head in one toss of a coin
  * $P(X = 1) = p,\quad P(X = 0) = 1 - p$
* Binomial, Binom(n, p), e.g. probability of a head count in $n$ tosses
  * $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k},\quad k:= 0, 1, ..., n$
  * equal to a sum of $n$ i.i.d Be(p).
* Poisson, Poisson($\lambda$)
  * $P(X = k) = \frac{\lambda^k}{k!}e^{-\lambda}$
  * equal to a sum of $n$ independent and non-identical Be($p_i$)
* Geometric, Geom(p), e.g. probability of toss count before first head
  * $P(X = n) = (1 - p)^{n-1}p,\quad n := 1,2,...$


## Abbreviations

* e.g., exempli gratia, a Latin phrase that means "for example".
* i.i.d., independent and identically distributed.

## Notation

* functions, constants: written uppercase
  * SUM(\*), P(_, gvn=), INTER(\*), UNION(\*)
* operators: +, -, *, /, !, <=>, =>, :=, =, ...
* variables: all lowercase
* scalar: written as is -> scalar
* vector example: ending with _1d -> example_1d
* matrix example: ending with _2d -> example_2d
* tensor example: ending with _nd -> example_nd
* function example: named with verb -> normalize
* count of something: something_cnt
