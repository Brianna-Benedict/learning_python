#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

rcdna = ''
for i in range(len(dna) -1, -1, -1):
    nt=dna[i]
    if   nt == 'A' : rcdna += 'T'
    elif nt == 'T' : rcdna += 'A'
    elif nt == 'C' : rcdna += 'G'
    elif nt == 'G' : rcdna += 'C'
    else           : rcdna += 'N'
print (rcdna)

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
