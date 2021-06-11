#!/usr/bin/env python3

import argparse
import mcb185
import random

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

# 1. 
# Set-up
parser = argparse.ArgumentParser(description = 'explore open reading frame')

# Required arguments => None needed
# Optional arguements with default parameters
parser.add_argument('--size', required = False, type =int, default = 450000, metavar = '<str>', 
    help = 'genome size [%(default)i]')
parser.add_argument('--orfmin', required = False, type =int, default = 100, metavar = '<int>', 
    help = 'minimum open reading frame [%(default)i]')
parser.add_argument('--gc', required = False, type =float, default = 0.5, metavar = '<float>', 
    help = 'gc fraction [%(default).3f]')
# Switches
parser.add_argument('--info', action = 'store_true', 
    help = 'provide additional info')
parser.add_argument('--seed', action = 'store_true', 
    help = 'fix random seed')

# Finalization
arg = parser.parse_args()

if arg.info: print(arg.size, arg.orfmin, arg.gc)

# Get same random numbers every time you run the program
if arg.seed: random.seed(1)

# Generate randome genome of specified size, GC composition
seq = mcb185.randseq(arg.size, arg.gc)
# print(seq)

#look for ATG
# 2.
lengths = []
for i in range(len(seq) - 2):
    start = None
    stop = None
    if seq[i:i + 3] == 'ATG':
        start = i
        for j in range(i, len(seq) - 2, 3):
            codon = seq[j:j + 3]
            if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                stop = j
                break
    if stop != None: lengths.append(int((stop - start)/3))
lengths.sort()
count = 0
for n in lengths:
    if n > arg.orfmin: 
        count += 1
# print(lengths)
#print(count) # aa lengths

#Thought Q's
# histogram: how many counts at each length
histogram = []
histogram = [0] * int(lengths[-1]+1)

for k in lengths:
    histogram[k] += 1
print(histogram)