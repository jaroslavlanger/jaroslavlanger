#!/bin/bash

var_1=90
var_2=not_text
var_3=( n o t " " a r r a y )

echo "${var_1} | ${var_2} | ${var_3}"

source ./config.bash

echo "${var_1} | ${var_2} | ${var_3}"
