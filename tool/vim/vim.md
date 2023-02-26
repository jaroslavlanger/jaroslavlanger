# Vim

Vi improved - visual text editor for life.

`2021 Apr 10, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [To Do](#to-do)
* [Introduction](#introduction)
    * [Where to Learn Vim](#where-to-learn-vim)
    * [Vim Modes](#vim-modes)
* [Basics](#basics)
    * [Basic Commands](#basic-commands)
    * [Normal Mode Movement](#normal-mode-movement)
    * [Single-stroke Editing Actions](#single-stroke-editing-actions)
    * [Composed Editing Actions](#composed-editing-actions)
    * [Composed Editing Example](#composed-editing-example)
    * [Basic Operations](#basic-operations)
    * [Search for Pattern](#search-for-pattern)
    * [Copy from and Paste to Clipboard](#copy-from-and-paste-to-clipboard)
    * [Autocomplete](#autocomplete)
* [Advanced](#advanced)
    * [Advanced Movement](#advanced-movement)
    * [Move to Desired Character](#move-to-desired-character)
    * [Visual Modes](#visual-modes)
    * [Visual Mode Actions](#visual-mode-actions)
    * [Change View](#change-view)
    * [Replace by Pattern](#replace-by-pattern)
    * [Mark Movements](#mark-movements)
    * [Commands](#commands)
* [More Files](#more-files)
    * [Tabs](#tabs)
* [Features](#features)
    * [Spell Checking](#spell-checking)
    * [Auto Increment](#auto-increment)
* [Settings](#settings)
    * [Configuration File](#configuration-file)
* [Terminal](#terminal)
* [Netrw](#netrw)
* [Vimdiff](#vimdiff)

<!-- /TOC -->

## To Do

* [Vim registers: The basics and beyond `:reg` (brianstorti.com)](https://www.brianstorti.com/vim-registers/)
* [Vim tips: Using tabs (linux.com)](https://www.linux.com/training-tutorials/vim-tips-using-tabs/)
* [Why I love Vim: It’s the lesser-known features that make it so amazing (freecodecamp.org)](https://www.freecodecamp.org/news/learn-linux-vim-basic-features-19134461ab85/)
* [Vim: you don't need NERDtree or (maybe) netrw](https://shapeshed.com/vim-netrw/)

## Introduction

* [What Are The Differences Between Vi And Vim? (shell-tips.com)](https://www.shell-tips.com/linux/vi-vs-vim/)

### Where to Learn Vim

1) Inside the vim editor.
   - `:Tutor` - start tutorial.
1) [vim tutor by Luke Smith](https://www.youtube.com/watch?v=d8XtNXutVto)
1) [Vim documentation: help (cs.auckland.ac.nz)](https://www.cs.auckland.ac.nz/references/gnu/vim/)
1) [learn by playing a game (vim adventures)](https://vim-adventures.com/)
1) [Basic Vi Commands (Colorado State University)](https://www.cs.colostate.edu/helpdocs/vi.html)

### Vim Modes

**Normal mode**

* Every vim session starts in normal mode.
* In normal mode keys do not write down their letters, they all have special actions.

**Insert mode**

* Insert mode works the same as normal text editor.
    * If you type "b" the "b" appears on the screen.
* To enter the insert mode press `[i]`.
* Press `[esc]` to exit the insert mode.

**Visual mode**

* Visual mode enables to visually select the text and apply editing to the selection.
* To enter the visual mode press `v`.
* Press `[esc]` to exit the visual mode.

**Command mode**

* Command mode allows you to use advanced commands such as replacing text with regex.
    * It also allows you to set up the editor e.g. set search to be case insensitive.
* To enter the command mode press `:`.
* Use `[backspace]` to exit the command mode.

## Basics

```sh
# Open file example.txt if exists otherwise create a new one.
vim example.txt
```

### Basic Commands

| Keystrokes           | Action                                                  | Alternatives |
| :---:                | ---                                                     | ---          |
| `[i]`                | Act like other text editors (insert mode).              |              |
| `[esc]`              | Return to the "Normal Mode" (necessary for exiting).    |              |
| `[i][h][i][esc]`     | Start editing write "hi" and end editing.               |              |
| `[shift-Z][shift-Q]` | Quit vim without saving (form Normal mode).             | `[:][q][!][enter]` |
| `[:][w][enter]`      | Save file (write the changes to the file).              |              |
| `[shift-Z][shift-Z]` | Save and quit.                                          | `[:][x][enter]`; `[:][w][q][enter]` |
| `[:][q][enter]`      | Safely quit vim (will not happen if file is not saved). |              |

### Normal Mode Movement

| Keystrokes  | Action                  |
| :---:       | ---                     |
| `[j]`       | Move down.              |
| `[k]`       | Move up.                |
| `[h]`       | Move right.             |
| `[l]`       | Move left.              |
| `[8][j]`    | Move 8 lines down.      |
| `[g][g]`    | Move to the first line. |
| `[shift-G]` | Move to the last line.  |

### Single-stroke Editing Actions

| Keystrokes  | Action                                                           |
| ---         | ---                                                              |
| `[x]`       | Delete character under the cursor.                               |
| `[p]`       | Paste deleted or yanked content (e.g. the deleted character).    |
| `[r][8]`    | Replace character under the cursor with number "9".              |
| `[i]`       | Start insert mode right before the cursor.                       |
| `[a]`       | Start insert mode right after the cursor.                        |
| `[o]`       | Create paragraph bellow the cursor and enter the insert mode.    |
| `[shift-X]` | Delete character before the cursor (backspace).                  |
| `[shift-P]` | Paste deleted or yanked content before the cursor.               |
| `[shift-R]` | Start replacing all characters (like insert mode) until `[esc]`. |
| `[shift-I]` | Start insert mode at the beginning of the line.                  |
| `[shift-A]` | Start insert mode at the end of the line.                        |
| `[shift-O]` | Create paragraph above the cursor and enter the insert mode.     |
| `[shift-J]` | Delete current line's newline.                                   |

### Composed Editing Actions

| Keystrokes  | Action                                                         |
| :---:       | ---                                                            |
| `[d][d]`    | Delete current line.                                           |
| `[y][y]`    | Yank (copy) current line.                                      |
| `[c][c]`    | Delete current line and enter the insert mode.                 |

### Composed Editing Example

The editing actions all behave similarly. Follows example of delete action, however the modifiers works the same for copying, replacing etc.
Delete action store the deleted text to the buffer, co it act as a "Cut" (`[ctrl-X]`) in other editors.

| Keystrokes  | Action                                                | Alternatives |
| ---         | ---                                                   | ---          |
| `[d][d]`    | Delete current line.                                  |              |
| `[9][d][d]` | Delete nine line down.                                |              |
| `[d][$]`    | Delete characters to the end of the line.             | `[shift-D]`  |
| `[d][0]`    | Delete characters to the beginning of the line.       |              |
| `[d][^]`    | Delete to the line's first not white-space character. |              |
| `[d][w]`    | Delete characters to the end of the word.             |              |
| `[d][i][w]` | Delete word under the cursor.                         |              |
| `[d][i][(]` | Delete content in `(` parentheses.                    |              |
| `[d][a][[]` | Delete content in `[` parentheses.                    |              |
| `[d][i]["]` | Delete content in `"` double quotes.                  |              |
| `[d][a][w]` | Delete word under the cursor with space around.       |              |
| `[d][i][p]` | Delete paragraph (content between empty lines).       |              |
| `[d][i][p]` | Delete paragraph and space around.                    |              |

### Basic Operations

| Keystrokes | Action              |
| :---:      | ---                 |
| `[u]`      | Undo action.        |
| `[ctrl-r]` | Redo action.        |
| `[.]`      | Repeat last action. |

### Search for Pattern

| Keystrokes  | Action                                                       |
| :---:       | ---                                                          |
| `[/][8]`    | Search for regex pattern `\8\` and go to the first match.    |
| `[n]`       | Go the next match.                                           |
| `[shift-N]` | Go to the previous match.                                    |
| `[*]`       | Search for the word under the cursor.                        |
| `:noh`      | Abbreviation for :nohlsearch (no highlight search).          |
| `[?][8]`    | Search for regex pattern `\8\` and go to the previous match. |

### Copy from and Paste to Clipboard

Use the `y` and `p` the same way, only type `"+` before the action.
* e.g use `"+p` to paste the content from the clipboard or use `"+yy` to copy the current line.

### Autocomplete

| Shortcut   | Action                         |
| :---:      | ---                            |
| `[ctrl-n]` | Go to next recommendation.     |
| `[ctrl-p]` | Go to previous recommendation. |

## Advanced

### Advanced Movement

| Shortcut           | Action                                        |
| :---:              | ---                                           |
| `[w]`              | Move to the beginning of the next word.       |
| `[shift-W]`        | Move one position after next whitespace.      |
| `[b]`              | Move to the beginning of the previous word.   |
| `[shift+B]`        | Move one position before previous whitespace. |
| `[e]`              | Move to the end of the next word.             |
| `[shift+E]`        | Move at the position before next whitespace.  |
| `[g][e]`           | Move to the end of the previous word.         |
| `[$]`              | Move to the end of the line.                  |
| `[0]`              | Move to the beginning of the line.            |
| `[^]`              | Move to the beginning of the first word.      |
| `[{]`              | Move to the previous empty line (paragraph).  |
| `[}]`              | Move to the next empty line (paragraph).      |
| `[(]`              | Move to the previous sentence.                |
| `[)]`              | Move to the next sentence.                    |
| `[%]`              | Move to the matching  parentheses.            |
| `[1][1][shift-G]`  | Move to the 11th line.                        |
| `[:][1][1][enter]` | Move to the line 11.                          |
| `[ctrl+g]`         | Show current line of the file and percentage. |
| `[2][0][%]`        | Move to the 20% of the document.              |
| `[ctrl-d]`         | Move half page down.                          |
| `[ctrl-u]`         | Move half page up.                            |
| `[ctrl-f]`         | Move page down.                               |
| `[ctrl-b]`         | Move page up.                                 |

### Move to Desired Character

| Keystrokes | Action                                                         |
| ---        | ---                                                            |
| `[f][8]`   | Move to the next `8` on the current line.                      |
| `[F][8]`   | Move to the previous `8` on the current line.                  |
| `[t][8]`   | Move one character before the next `8` on the current line.    |
| `[T][8]`   | Move one character after the previous `8` on the current line. |
| `[;]`      | Repeat the action of `[f]` `[F]` `[t]` `[T]`.                  |
| `[,]`      | Repeat the action in the oposite direction.                    |

### Visual Modes

| Keystrokes  | Action                      |
| ---         | ---                         |
| `[v]`       | Triggers visual mode.       |
| `[shift-V]` | Triggers line visual mode.  |
| `[ctrl+v]`  | Triggers block visual mode. |

### Visual Mode Actions

| Keystrokes | Action                                                   |
| ---        | ---                                                      |
| `[d]`      | Deletes highlighted characters.                          |
| `[y]`      | Yanks highlighted characters.                            |
| `[c]`      | Changes highlighted characters.                          |
| `:norm`    | Apply normal mode commands to every highlighted line.    |
| `:norm I#` | Add hashtag before first word on every highlighted line. |

### Change View

| Keystrokes | Action                          |
| ---        | ---                             |
| `[z][t]`   | Move current line to the top.   |
| `[z][z]`   | Move cursor line to the middle. |
| `[z][b]`   | Move cursor line to the bottom. |

### Replace by Pattern

| Command                      | Action                                                 |
| ---                          | ---                                                    |
| `:s/pattern/substituent/`    | Substitute one match (sed syntax).                     |
| `:s/pattern/substituent/g`   | Substitute all matches (on the same line).             |
| `:%s/pattern/substituent/g`  | Substitute all matches (all lines).                    |
| `:%s/pattern/substituent/gc` | Confirm all substitutions for all matches (all lines). |

* [Search_and_replace (vim.fandom.com)](https://vim.fandom.com/wiki/Search_and_replace)

### Mark Movements

| Keystrokes      | Action                                       |
| ---             | ---                                          |
| `[m][a]`        | Set mark `a` to the current cursor location. |
| `['][a]`        | Jump to the beginning of line with mark `a`. |
| `[backtick][a]` | Jump to the line and column of mark `a`.     |
| `['][']`        | Jump to location before last jump.           |

* [Using_marks (vim.fandom.com)](https://vim.fandom.com/wiki/Using_marks)

### Commands

Command mode starts with press of the key `:`.

| Command   | Example usage  | Description                                          | Alternatives |
| :---:     | ---            | ---                                                  | ---          |
| `e`       | `:e filename`  | Open file for editing.                               |              |
| `r`       | `:r filename`  | Open file for reading.                               |              |
| `!`       | `:! ls`        | Runs any terminal command.                           |              |
| `w`       | `:w filename`  | Write as a filename.                                 |              |
| `w`       | `:w !sh`       | Execute like a shell script (write buffer to shell). | `:w !bash`   |
| `source`  | `:so %`        | Read file and treat it as a vim script.              |              |
| `retab`   | `:retab`       | Convert tabs to spaces.                              |              |
| `qa`      | `:qa`          | Quit all files.                                      |              |
| `sort`    | `:sort`        |                                                      |              |
| `earlier` | `:earlier 15m` |                                                      |              |
| `later`   | `:later 10m`   |                                                      |              |

* [https://superuser.com/questions/132029/how-do-you-reload-your-vimrc-file-without-restarting-vim (superuser.com)](https://superuser.com/questions/132029/how-do-you-reload-your-vimrc-file-without-restarting-vim)
* [Execute current buffer as bash script from vim (stackexchange.com)](https://vi.stackexchange.com/questions/10209/execute-current-buffer-as-bash-script-from-vim)

## More Files

```bash
# Open files horizontally split windows
vi -o file1 file2
# Open files vertically split windows
vi -O file1 file2
```

| Keystrokes         | Action                                 | Alternatives |
| ---                | ---                                    | ---          |
| `:split`           | Horizontally split vim window in half. | `:sp`        |
| `:vsplit`          | Vertically split vim window in half.   | `:vs`        |
| `:botright vs`     | Vertically split open in right window. |              |
| `[ctrl-w][ctrl-w]` | Switch to the next window.             |              |
| `[ctrl-w][ctrl-k]` | Switch to upper window, options: hjkl. |              |

### Tabs

| Keystrokes     | Action                  |
| ---            | ---                     |
| `:tabnew FILE` | Open FILE in new tab.   |
| `[g][t]`       | Go to the next tab.     |
| `[g][shift-T]` | Go to the previous tab. |
| `[8][g][t]`    | Go to the 8th tab.      |

## Features

### Spell Checking

| Keystrokes                         | Action                                            |
| ---                                | ---                                               |
| `:set spell! spelllang=en_us`      | Turn on spell checking.                           |
| `:setlocal spell! spelllang=en_us` | Turn spell checking only for the current file.    |
| `:set nospell`                     | Turn off spell checking.                          |
| `[z][=]`                           | Get the dictionary to choose from.                |
| `[]][s]`                           | Go to the next misspelled word.                   |
| `[z][g]`                           | Add the word under cursor to the dictionary.      |
| `[z][u][w]`                        | Remove the word under cursor from the dictionary. |

### Auto Increment

| Keystrokes | Action                                      |
| ---        | ---                                         |
| `[ctrl-a]` | Auto increment the next number on the line. |

## Settings

| Command            | Action                                         |
| ---                | ---                                            |
| :set nu!           | turns on/off the line number                   |
| :set tabstop=4     | sets the number of spaces for tab              |
| :set softtabstop=0 |                                                |
| :set expandtab     |                                                |
| :set shiftwidth=4  |                                                |
| :set smarttab      |                                                |
| :set ignorecase    | also `set ic` search will be case insensitive  |

### Configuration File

* [How to configuration](https://www.linode.com/docs/guides/introduction-to-vim-customization/)

## Terminal

| Keystrokes         | Action                      |
| ---                | ---                         |
| `:term`            | Opens terminal in vim.      |
| `[ctrl-\][ctrl-n]` | Returns to the normal mode. |

## Netrw

| Keystrokes | Action           |
| ---        | ---              |
| `[%]`      | Create new file. |
| `[t]`      | Open in new tab. |

## Vimdiff

`vimdiff file_1 file_2`

| Keystrokes        | Action                                |
| ---               | ---                                   |
| `[]][c]`          | Go to the next change.                |
| `[[][c]`          | Go to the previous change.            |
| `[d][p]`          | Apply this change to the second file. |
| `[d][o]`          | Apply change from the other file.     |
| `:windo diffthis` | Start diff mode from windows split.   |
| `:diffoff`        | Turn off the diff mode.               |
