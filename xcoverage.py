#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

"""
1. Make variables for genome size, read number, read length
2. Simulates random reads
3. Report min, max, and average coverage
"""

# 1. 
genome_size = int(sys.argv[1])
genome_read_num = int(sys.argv[2])
genome_read_len = int(sys.argv[3])

# 2.
genome = [0] * genome_size
for i in range(genome_read_num):
    r = random.randint(0, genome_size - genome_read_len)
    for j in range(genome_read_len):
        genome[j + r] += 1

# 3. 
min_value = genome[0]
max_value = genome[0]
sum_value = 0.0000

for i in range(1, len(genome)):
    if genome[i] < min_value: min_value = genome[i]
    if genome[i] > max_value: max_value = genome[i]

for j in range(len(genome)):
    sum_value += genome[j]

mean = float(sum_value / len(genome))

print(min_value, max_value, f'{mean:.5f}')


"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
