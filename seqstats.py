#!/usr/bin/env python3

import argparse
import mcb185
import statistics

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library

parser = argparse.ArgumentParser(description = 'stats about sequence')

# Required arguments
parser.add_argument('--file', required = True, type = str,
    metavar = '<str>', help = 'required fasta file')
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
    length.append(len(seq))
length.sort()
# print(length)

# 1. Min
print('min is', min(length)) 

# 2. Max
print('max is', max(length)) 

# 3. Sum
# sum = 0
# for value in length:
#   sum += value
print('sum is', sum(length))
# print(sum(length)) # Easy way to get sum using functions in python

# 4. Mean
print('mean is', statistics.mean(length)) 

# 5. Median
print('median is', statistics.median(length)) 

print('n50 is', mcb185.n50(length))
# print(length)
# N50 - sum values, once is greater than 1/2 total sum, that is N50
