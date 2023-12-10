#!/bin/bash

# echo $0
# echo $1
matrix=$1

shift

# echo $@
flags=$@

echo ./build/solver_3 ${matrix} ${matrix%%_*}_vector.txt ${matrix%%_*}_output.txt ${flags}
./build/solver_3 ${matrix} ${matrix%%_*}_vector.txt ${matrix%%_*}_output.txt ${flags}

