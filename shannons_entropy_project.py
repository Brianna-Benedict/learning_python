import sys
import math

# Shannon's Entropy was invented by Claude Shannon
# It's information content as it's the average information per message
# The loop below allows you to calculate Shannon's Entropy (of a sum of information)

H = 0 # H: information content
for p in sys.argv[1:]:
    p = float(p) # p: probability of message
    H -= p * math.log2(p)

print(f'{H:.3f}')

"""
python3 shannons_entropy_project 0.2 0.4 0.6 0.8
"""