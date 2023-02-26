# Documents

`2021 Feb 03, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Convert documents](#convert-documents)
    * [Pandoc](#pandoc)
* [Markdown](#markdown)
* [$LaTeX$](#latex)
* [XML](#xml)
* [HTML](#html)
* [CSS](#css)
* [Excel (XLS)](#excel-xls)

<!-- /TOC -->

## Convert documents

### Pandoc

* [Pandoc a universal document converter](https://pandoc.org/)

Installation

```sh
wget "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-1-amd64.deb"
sudo dpkg -i pandoc-2.11.4-1-amd64.deb
```

* [Pandoc releases (github.com)](https://github.com/jgm/pandoc/releases/)

**Basic usage**

* [Democ (pandoc.org)](https://pandoc.org/demos.html)

Convert markdown to PDF

```sh
pandoc report.md --pdf-engine=xelatex -o report.pdf
```

Convert markdown to HTML

```sh
# HTML fragment (plain html)
pandoc page.md -o page.html

# HTML with style (-s for standalone)
pandoc -s page.md -o page.html

# Add advanced LaTeX math
pandoc -s page.md --mathjax -o page.html
```

* [use --mathjax (tex.stackexchange.com)](https://tex.stackexchange.com/questions/551960/pandoc-cannot-parse-equation-with-a-fraction)

## Markdown

## $LaTeX$

## XML

## HTML

## CSS

## Excel (XLS)

