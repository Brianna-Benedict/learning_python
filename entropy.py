#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

p = []
"""
1st way: 
for i in range(1, len(sys.argv)):
    p.append(float(sys.argv[i]))
print(p)
"""
# 2nd way:
for s in sys.argv[1:]:
    p.append(float(s))
print(p) # Not in text format anymore

# Make sure all values add up to 1 (are not too different from 1)
print(sum(p))
# if sum(p) != 1 # Would use this, but can't bc floating point
assert(math.isclose(sum(p), 1, abs_tol = 0.2)) # Close enough

H = 0
for i in range(len(p)):
    H -= p[i] * math.log2(p[i])
print(f'{H:.3f}')

"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""
