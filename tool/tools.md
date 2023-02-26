# Software Tools

## Overview

1. Operating system (linux, mac os, windows)
1. Desktop environment (gnome, xfce, kde)
1. Internet browser (chromium)
1. Terminal emulator (xterm, cygwin, kitty, putty)
1. Shell (sh, bash, zsh)
1. Text Editor (vim, neovim, vs code, sublime text)
1. Text Specification, see [text](/text)
1. Version control (git, github, gitlab)
1. Programming language, see [code](/code)
1. Other (make, jupyter notebook, docker)

## Terminal management - tmux

* [A Quick and Easy Guide to tmux (Ham Vocke)](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)

Install tmux and work with sessions.

```sh
# Install tmux (ubuntu)
sudo apt-get install tmux

# Create tmux session
tmux
# Create named session
tmux new -s SESSION_NAME

# List all tmux sessions
tmux ls

# Attach to the first session
tmux attach -t 0
# Attach to the named session
tmux attach -t SESSION_NAME
```

Work with tabs.

| Keystrokes      | Action                       |
| ---             | ---                          |
| `<ctrl><b> <d>` | Detach from current session. |
| `<ctrl><b> <c>` | Create new tab.              |
| `<ctrl><b> <,>` | Rename current tab.          |
| `<ctrl><b> <,>` | Rename current tab.          |
| `<ctrl><b> <4>` | Change to the fourth tab.    |
| `<ctrl><d>`     | Close current tab.           |

Splitting the screen.

| Keystrokes       | Action                     |
| ---              | ---                        |
| `<ctrl><b> <%>`  | Split screen horizontally. |
| `<ctrl><b> <">`  | Split screen vertically.   |
| `<ctrl><b> <up>` | Change to upper section.   |

Scroll up the terminal.

| Keystrokes       | Action                    |
| ---              | ---                       |
| `<ctrl><b> <[>`  | Start the scrolling mode. |
| `<pgup>`         | Scroll up.                |
| `<ctrl><c>`      | Exit the scrolling mode.  |

* [How can I page up or down in tmux with Terminal.app?](https://unix.stackexchange.com/questions/81540/how-can-i-page-up-or-down-in-tmux-with-terminal-app)

## Code editor - nvim
