#!/bin/bash
shopt -s globstar
scripts=$(dirname $0)

$scripts/clean.bash
$scripts/maketree.py > tree.html
cp -sfv tree.html docinfo-header.html
asciidoctor -v **/*.adoc
