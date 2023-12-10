!/bin/bash

steps=255 # 63 # 511

echo "$(date +%T.%N) - Computation started."
for i in {0..99}; do
    file_out=./outputs/ca_${i}_${steps}.png
    ./cellular_automaton.py -r ${i} -s ${steps} -o ${file_out}
    echo "$(date +%T.%N) - File ${file_out} done."
done
