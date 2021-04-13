#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here
dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
def codons(dna):
    dna_len=len(dna)
    for codon in range(0,dna_len,3):
        print(dna[codon:codon+3])

"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
