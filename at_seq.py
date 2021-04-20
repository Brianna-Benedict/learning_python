#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

at_count = 0
bp = 30
seq = ''
t = 0.6
for i in range(bp):
    r = random.random()
    if r < t:
        if random.random() < 0.5:
            seq += 'a'
        else:
            seq += 't'
    else:
        seq += random.choice('gc')

for i in range(len(seq)):
    if seq[i] == "a" or seq[i] == "t":
        at_count += 1

print(len(seq), f'{at_count/len(seq)}', seq)




"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
