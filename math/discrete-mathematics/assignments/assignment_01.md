# Domácí zábava č. 1

`23. 2. 2021, Jaroslav Langer`

## 1.

Dokončete důkaz z přednášky odvozením finálního vzorce pro Fibonacciho čísla pomocí rozkladu zlomku $\frac{x}{(1−x−x^2)}$ na parciální zlomky.

$$
x_1 = \frac{-1 - \sqrt{5}}{2},\quad x_2 = \frac{-1 +\sqrt{5}}{2}
$$

$$
(1 - x - x^2)
= -(x - x_1)(x - x_2)
= -\left(x + \frac{1 + \sqrt{5}}{2}\right)\left(x + \frac{1 - \sqrt{5}}{2}\right)
$$

$$
\frac{x}{1 - x - x^2}
= \frac{x}{-(x - x_1)(x - x_2)}
= \frac{-x}{\left(x + \frac{1 + \sqrt{5}}{2}\right)\left(x + \frac{1 - \sqrt{5}}{2}\right)}
$$

$$
A = \frac{-5 -\sqrt{5}}{10},\quad B = \frac{-5 + \sqrt{5}}{10}
$$

$$
\frac{A}{x -x_1} + \frac{B}{x -x_2}
= \frac{\frac{-5 -\sqrt{5}}{10}}{x + \frac{1 + \sqrt{5}}{2}}
+ \frac{\frac{-5 +\sqrt{5}}{10}}{x + \frac{1 - \sqrt{5}}{2}}
$$

$$
\frac{x}{1 -x -x^2}
= \frac{A}{x -x_1} \cdot \frac{-x_1}{-x_1} + \frac{B}{x -x_2} \cdot \frac{-x_2}{-x_2}
= \frac{a}{1 - \lambda_1x} + \frac{b}{1 - \lambda_2x}
$$

$$
\lambda_1 = \frac{1}{x_1} = \frac{2}{-1 - \sqrt{5}}
$$

$$
\lambda_2 = \frac{1}{x_2} = \frac{2}{-1 +\sqrt{5}}
$$

<!--
A = \frac{-5 -\sqrt{5}}{10},\quad B = \frac{-5 + \sqrt{5}}{10}
x_1 = \frac{-1 - \sqrt{5}}{2},\quad x_2 = \frac{-1 +\sqrt{5}}{2}
-->

$$
a = - \frac{A}{x_1} = - \frac{\frac{-5 -\sqrt{5}}{10}}{\frac{-1 - \sqrt{5}}{2}} = - \frac{\sqrt{5}}{5}
$$

$$
b = - \frac{B}{x_2} = - \frac{\frac{-5 + \sqrt{5}}{10}}{\frac{-1 +\sqrt{5}}{2}} = \frac{\sqrt{5}}{5}
$$

$$
\frac{x}{1 -x -x^2}
= \frac{a}{1 - \lambda_1x} + \frac{b}{1 - \lambda_2x}
= \frac{- \frac{\sqrt{5}}{5}}{1 - \left(\frac{2}{-1 - \sqrt{5}}\right)x}
+ \frac{\frac{\sqrt{5}}{5}}{1 - \left(\frac{2}{-1 +\sqrt{5}}\right)x}
$$

## 3

combination(2,0)*combination(2,2) + (combination(2,1)*combination(2,1)*-1) + (combination(2,2)*combination(2,2))

