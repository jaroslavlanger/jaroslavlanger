# How to code

How to code without falling into deep depression.

`2020 Dec. 17, Jaroslav Langer`

## Content <!-- omit in toc -->

- [Recommendations](#recommendations)
  - [Use keyboard as much as possible](#use-keyboard-as-much-as-possible)
  - [Do not invent the wheel](#do-not-invent-the-wheel)
  - [Adding funtionality from elsewhere](#adding-funtionality-from-elsewhere)
  - [How to work on an assingment](#how-to-work-on-an-assingment)
- [Tools that saves time (and scripts)](#tools-that-saves-time-and-scripts)
- [Naming](#naming)
  - [Date and time formats](#date-and-time-formats)
- [Folders hierarchy](#folders-hierarchy)
- [My code routine](#my-code-routine)
- [Test driven development](#test-driven-development)
- [Debugging](#debugging)

## Recommendations

### Use keyboard as much as possible

### Do not invent the wheel

- It is so much more fun, to explore the world by try and fail approach.
- Also it is so less efficient. Don't do it often! Just google it, read it, then try it.
- Try in small pieces, not big features.
- Any time you want to try something big, elsewhere test every tiny piece.
- Testing on simple functionality, is annoying, useless and quick.
- On the other hand writing a piece and debug it at once is hard, challenging, and slow.
- Don't conquer the code, write it.

### Adding functionality from elsewhere

Always try it before adding to your code!
It will probably work if you don't but it will likely to work in other way than you've expected.

### How to work on an assignment

- Do not spend too much time with details right from the beginning.
  - i.e. do the most of the fluent work from the start,
  - the problems will be visible afterwards, and also it will be clear how much time is left.

## Tools that saves time (and scripts)

## Naming

### Date and time formats

| Date          | Simplified  | Ranking | Reasons                                                             |
| :---:         | ---         | :---:   | ---                                                                 |
| 2020, Apr. 25 | 2020_apr_25 | 1       | My favorite one. Descriptive, short, universal.                     |
| 2020-04-25    | 20200425    | 2       | Second favorite. The simplified version is sorted right by default. |
| 2020/04/25    | 20200425    | 2       | Second favorite. The simplified version is sorted right by default. |
| 25. 4. 2020   |             | 3       | Official date format in Czechia.                                    |
| Apr. 25, 2020 |             |         | American official date format.                                      |

- [American date format](https://iso.mit.edu/americanisms/date-format-in-the-united-states/#:~:text=The%20United%20States%20is%20one,yyyy%2Dmm%2Ddd).)

### Note to "universality" of the month abbreviation

As the names of months are in many languages derived from [latin](https://blogs.transparent.com/latin/months-of-the-year/) it is not the worst approach to use their abbreviations.

| Abbr. | English (1st) | Latin  | Spanish (4th) | German (12th) |
| :---: | ---       | ---        | ---           | ---           |
| Jan.  | January   | Ianuarius  | enero         | Januar        |
| Feb.  | February  | Februarius | febrero       | Februar       |
| Mar.  | March     | Martius    | marzo         | März          |
| Apr.  | April     | Aprilis    | abril         | April         |
| May   | May       | Maius      | mayo          | Mai           |
| Jun.  | June      | Iunius     | junio         | Juni          |
| Jul.  | July      | Iulius     | julio         | Juli          |
| Aug.  | August    | Augustus   | agosto        | August        |
| Sep.  | September | September  | septiembre    | September     |
| Oct.  | October   | October    | octubre       | Oktober       |
| Nov.  | November  | November   | noviembre     | November      |
| Dec.  | December  | December   | diciembre     | Dezember      |

- [Months abbreviations source](https://abbreviations.yourdictionary.com/articles/standard-month-and-days-of-the-week-abbreviations.html)
- [languages by total number of speakers](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers)
- [spanish months](https://spanish.kwiziq.com/revision/grammar/months-of-the-year-are-masculine)
- [german months](https://www.expatrio.com/living-germany/learn-german/german-months)

## Folders hierarchy

- Placeholder.

## My coding routine

1) Open terminal emulator

- Press `alt+t`.

2) Open window manager

```sh
ranger
```

3) Go to the desired destination

- Use `hjkl` to move and search like this `/Pro``+enter`.
- Press shift+d to change the terminal location to to the ranger directory.

4) Swich to the branch (or create) of the feature or goal

```sh
git checkout example_testing
```

5) Start work

```sh
nvim solver.cpp
code README.md
google-chrome report.pdf
```

- In case of standalone application use `ctrl+win+3` to move them to appropriate (e.g. 3rd) **workspace**.

6) Open another thing simultaneously

- Press `ctrl+shift+t` to open new **terminal tab**.
- Use `ctrl+4` to move to appropriate (e.g. 4th) tab.

## Test driven development

## Debugging

- Do not debug code with debugging prints. It is simple, it is straight forward and it is so bad.
- I was doing ti for much longer than i should have. Now I perform debugging inside of MS code.

- [link](https://code.visualstudio.com/docs/cpp/config-linux)

