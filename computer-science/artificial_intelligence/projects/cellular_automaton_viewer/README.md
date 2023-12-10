# Cellular Automaton

`2021 Feb 12, Jaroslav Langer`

## Sample Usage

```sh
# By default creates ca rule 110, for 255 steps
./cellular_automaton.py

# More options
./cellular_automaton.py -r 73 -i random -s 511 -o ca_73_rand.png

# See all options
./cellular_automaton.py --help
```

## Contents

<!-- TOC GFM -->

* [Introduction](#introduction)
* [Cellular Automata Classification](#cellular-automata-classification)
    * [Class 1](#class-1)
    * [Class 2](#class-2)
    * [Class 3](#class-3)
    * [Class 4](#class-4)

<!-- /TOC -->

## Introduction

Cellular automata is a model of computation. It consists of of rigid structure of cells (It can be one or multidimensional). There is set of states a cell can be in. There is also defined neighborhood of a cell. And lastly there is a transition function (rule) that based on a cell's state and state of it's neighbors define the next cell's state.

One-dimensional cellular automata have the advantage that the time progress can be visualized to the second dimension.

## Cellular Automata Classification

There is a classification proposed by Stephen Wolfram that divides the automata into four classes.

### Class 1

Automata belonging to the first class create an uniform stable patterns. Perhaps rule 0 or rule 4 belongs to this class. 

### Class 2

Second class automata create also stable patterns. This time, the cells are not constant, but they changes itself periodically. Few representatives from the beginning are rules 1, 5 and 7.

### Class 3

Cellular automata of the third class are the ones that appears random, those where no repetition or a structure can be found. First such an example is rule 30.

### Class 4

Fourth class is the class of a complex cellular automata. Results of these automata are patterns with a structured subpatterns interacting with each other in seemingly random manner. One such an example and probably the most famous one is the rule 110. 

