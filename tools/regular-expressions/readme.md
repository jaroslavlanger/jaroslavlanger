# Regular Expressions

## TODO

* https://en.wikipedia.org/wiki/Regular_expression
* https://en.wikipedia.org/wiki/Raku_rules

## Introduction

I found [Regular-Expressions.info](https://www.regular-expressions.info/) very useful to me, from now on I go there if I am not sure how exactly the thing works.

You don't need to reinvent the wheel every time. There are "community patterns" on [regexr.com](https://regexr.com/), that solves your problem, or at least usually give you a nice baseline.

## Optional item '?'

Makes the preceding token in optional. `regexp?` will match `regex` and `regexp`. In order to make optional more tokens use grouping, e.g. `Reg(ular)? ?Ex(p?ressions)?`.

* [Optional Items (regular-expressions.info)](https://www.regular-expressions.info/optional.html)

## Character Classes or Character Sets '[]'

* [Character Classes or Character Sets (regular-expressions.info)](https://www.regular-expressions.info/charclass.html)

## Regex Alternation '|'

Alternation has the lowest precedence of all regex operators. So the regex math either everything to the left from this sign `|` or everything to the right. In case the alternation should be applied only as a part of the pattern, then it needs to be closed with braces to create a group.

```
/first_pattern|second_pattern/
```
It is equivalent to
```
/(first_pattern|second_pattern)/
```
and not equivalent to
```
/first_patter(n|s)econd_pattern/
```

* [Alternation (regular-expressions info)](https://www.regular-expressions.info/alternation.html)

## Metacharacter

| Sym. | Matches                                                                    |
| ---- |                                                                            |
| `\b` | "Word boundary" i.e. between ^-word, nonword-word, word-nonword, word-end. |

* [Word Boundaries (regular-expressions.info)](https://www.regular-expressions.info/wordboundaries.html)

## Integer

**anywhere on the line**
```
$pattern = '/[[:digit:]]+/';
```
**Tousand dot every third position from end**
```
$integer = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*/';
```
**Tousand - dot every third position from end, ,-**
```
$pattern = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*(\ )*,-/';
```

## Float

**Tousand dot every third position from end with comma**
```
$float = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';
```

**Tousand dot every third position from end with comma and Kč**
```
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*Kč/';
```

**Tousand dot every third position from end with comma and CZK**
```
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK/';
```

**CZK and tousand dot every third position from end with comma**
```
$pattern = '/CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';
```

**CZK at start or end and tousand dot every third position from end with comma**
```
$pattern = '/(([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK|CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?)/';
```

