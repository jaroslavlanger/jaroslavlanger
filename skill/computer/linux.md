# Linux

The art of using PC like a human being.

`2020/11/14, Jaroslav Langer, using linux mint 19`

## Contents <!-- omit in toc -->
- [Terminal](#terminal)
  - [Copy and past in terminal](#copy-and-past-in-terminal)
  - [Linux directory structure](#linux-directory-structure)
  - [Type special characters](#type-special-characters)
- [Set caps lock to esc](#set-caps-lock-to-esc)
- [Set key stroke rate](#set-key-stroke-rate)
- [Redshift](#redshift)
- [Computers](#computers)
  - [BOM](#bom)

## Terminal

### Terminal shortcuts

| shortcut        | action                                               |
| ---             | ---                                                  |
| ctrl+shift+t    | Open new tab.                                        |
| ctrl+shift+w    | Close current tab.                                   |
| ctrl+pgup       | Go to upper (left) tab. Pgdn goes to the right tab). |
| ctrl+1          | Go to tab 1 (works for all numbers).                 |
| ctrl+shift+pgup | Move the tab one up (left). Pgdn moves to the right. |
| ctrl+k          | Kill - cut the rest of the line from the cursor.     |
| ctrl+k          | Kill - cut the rest of the line from the cursor.     |
| ctrl+w          | Kill the word right before the cursor.               |
| ctrl+u          | Kill the begging of the line up to the cursor.       |
| ctrl+y          | Yank - paste the text that was previously killed.    |
| alt+backspace   | Delete by words, not by characters.                  |

### Copy and past in terminal

#### Copy from terminal

Highlight the text and press Ctrl+Shift+C

#### Past to terminal

Press Ctrl+Shift+V

### Linux directory structure

+ /bin - executables
+ /home/* | /root - *users | roots personal data
+ /opt – Optional software (thigs you can't instal with package manager)
+ /etc - configuration files
+ /lib – Shared libraries

- [More information](https://linuxhandbook.com/linux-directory-structure/)

### Type special characters

Perhaps to write a dash, in linux there is a way to write unicode symbols.

1) press Ctrl+Shift+U
1) type the unicode code, perhaps 2014
1) press Space

## Set caps lock to esc

1) System Settings
2) Keyboard 
3) Layouts
4) Options
5) Caps Lock key behavior
6) Select Make Caps Lock an additional ESC

## Set key stroke rate

```sh
xset r rate 200 20
```
## Redshift

Program that lowers the temperature of the screen, so the eyes suffer much less.

- [redshift](http://jonls.dk/redshift/)

## Computers

### BOM

Byte order mark (BOM) is a particular usageof the special Unicode character, U+FEFF`

#### UTF-8 bom

```sh
0xEF,0xBB,0xBF
```

#### UTF-16 BOM

```sh
U+FEFF
```

- [Source](https://en.wikipedia.org/wiki/Byte_order_mark)

