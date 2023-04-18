# Neovim

Neovim - a Vim taken a step further.

`2021 Jan 31, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Introduction](#introduction)
* [References](#references)
* [Installation](#installation)
* [Create Config File](#create-config-file)
* [Create Space for Plugins](#create-space-for-plugins)
* [Install vim-plug Plugin Manager](#install-vim-plug-plugin-manager)
* [Plugins](#plugins)
    * [Conquer of Completition](#conquer-of-completition)
    * [Gruvbox Scheme](#gruvbox-scheme)
* [Add Plugins in the Config File](#add-plugins-in-the-config-file)
* [Neovim Diff](#neovim-diff)

<!-- /TOC -->

## Introduction

* [Meet Neovim (vimcasts.org)](http://vimcasts.org/episodes/meet-neovim/)

## References

* [How to Configure Vim like VSCode (benawad)](https://www.youtube.com/watch?v=gnupOrSEikQ)
  + [init.vim file from Ben Awad](https://gist.github.com/benawad/b768f5a5bbd92c8baabd363b7e79786f)

## Installation

```sh
sudo add-apt-repository ppa:neovim-ppa/stable       # version 0.4.4
# sudo add-apt-repository ppa:neovim-ppa/unstable   # version 0.5.0-dev
sudo apt-get update
sudo apt-get install neovim
```

* [Install neovim ubuntu/linux mint](https://vi.stackexchange.com/questions/25192/how-to-install-stable-version-of-neovim-on-ubuntu-18-04)

## Create Config File

```sh
# Do this only if the file does not exist already!
mkdir -p ~/.config/nvim
echo "\
set tabstop=4
set softtabstop=0
set expandtab
set shiftwidth=4
set smarttab
set list
" > ~/.config/nvim/init.vim
```

## Create Space for Plugins

```sh
mkdir -p ~/.vim/plugins
```

## Install vim-plug Plugin Manager

```sh
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

* [Install vim-plugin manager](https://www.linode.com/docs/guides/how-to-install-neovim-and-plugins-with-vim-plug/)

## Plugins

### Conquer of Completition

* [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)

Install nodejs >= 10.12:

```sh
curl -sL install-node.now.sh/lts | bash
```

### Gruvbox Scheme

* [morhetz/gruvbox](https://github.com/morhetz/gruvbox)

## Add Plugins in the Config File

Usually this is the very first lines of the init.vim file.

```init.vim
call plug#begin('~/.vim/plugins')

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'morhetz/gruvbox'

call plug#end()
```

Restart nvim and run `:PlugInstall`.

## Neovim Diff

```sh
nvim -d file_1 file_2
```
