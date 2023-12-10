#!/bin/bash

project_path=/home/langerjaros/Projects/learning/informatics/combinatorial_optimization/homeworks/hw03

data_path=${project_path}/data
scripts_path=${project_path}/scripts

gen_cmd=${project_path}/gen/kg2
perm_cmd=${project_path}/gen/kg_perm
knap=${project_path}/compute/build/knapsack

# I     # Frist ID
n=16    # number of items
N=100   # number of instances
m=0.8   # ratio of capacity/total_weight
W=5000  # max weight of an item 
w=bal   # more light or heavy items, or balanced
C=5000  # max value of an item
c=uni   # weith,value correlation
k=1     # granularity exponent
d=1     # delta (number instances to be permutated)

ns=(1 4 7 10 13 16 19 22 25 28)
ms=(0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1)
Ws=(1000 2000 3000 4000 5000 6000 7000 8000 9000 10000)
ws=(bal light heavy)
Cs=(1000 2000 3000 4000 5000 6000 7000 8000 9000 10000)
cs=(uni corr strong)
ks=(0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1)
ps=(0 1 2 3 4 5 6 7 7 8 9)

methods=("1:bf" "2:bab" "3:dp" "4:gh" "5:redux")
