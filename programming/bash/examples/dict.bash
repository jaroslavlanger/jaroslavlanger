#!/bin/bash

methods=(
    "1:bf"
    "2:bab"
    "3:dp"
    "4:gh"
    "5:redux"
    "6:fptas"
)

for m in ${methods[@]}; do
    m_key=${m%%:*}
    m_name=${m#*:}
    printf "{%s: %s}\n" "$m_key" "$m_name"
done
