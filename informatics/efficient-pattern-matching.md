# Efficient pattern matching

## Lectures

- [L01 - Basic notions, border array](#l01---basic-notions,-border-array)
- [L02 - Text full index: Suffix array, Suffix Sorting](#l02---text-full-index:-suffix-array,-suffix-sorting)
- [L03 - Text full index: Suffix tree, LCP construction](#l03---text-full-index:-suffix-tree,-lcp-construction)
- [](#)

## L01 - Basic notions, border array

## Alphabet

### Types of alphabet

- index with symbols
- ordered alphabet
- unordered alphabet
- partially ordered alphabet

## 

Σ* = Σ+ ∪ {0}
Σ* = 
Σ+ = non empty

## Orientation

- string (linear) - left to right
- necklace (circular) - can be oriented to left or right
- infinite string -
- infinite necklace

## Substring (factor)

- string - symbols between i and j index of original string
- proper substring - smaller than original
- factor - all substring including the string
- prefix - eferything before i
- sufix - any 

## prefix sufix types 

- non-proper prefix
- non-empty prefix
- proper suffix
- non-empty proper suffix

## Ordering standard

## Normal form

## L02 - Text full index: Suffix array, Suffix Sorting

### Searching in list of strings

Membership problem

Interval problem

### DEF LCP - Longest common prefix
```
Let u, v ∈ Σ∗. The longest common prefix lcp(u, v) is the longest prefix
common to u and v.
```

### Algoritm: Simple-search-MP
```
Algorithm Simple-Search-MP
Input: L, n, x, m
Output: index i, Li = x, or indices d and f.
1: d ← −1
2: f ← n
3: while d + 1 < f do
4:      i ← ⌊(d + f)/2⌋
5:      ℓ ← |lcp(x , Li)|
6:      if ℓ = m and ℓ = |Li| then return i
7:      else if (ℓ = |Li|) or (ℓ 6= m and Li[ℓ] < x[ℓ]) then
8:          d ← i
9:      else
10:         f ← i
11:     end if
12: end while
13: return (d, f)
``` 

## L03 - Text full index: Suffix tree, LCP construction

## Symbols

𝜖 ∞ ∀ ≡ ≠ | |„ ∪  ∩ ✓