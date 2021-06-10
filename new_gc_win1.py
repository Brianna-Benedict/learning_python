# 4/22/21 exercise- shows that some programs take longer to write than others, but may run faster
# More wasteful way of doing it 
# Counting every G & C in the window, going back to the beginning of the window each time

seq = 'ACGTGCGCGCGCGCGCGCGC'
w = 5 # Window

for i in range(len(seq) -w+1): # Need to stop at end, so - window size + 1 (bc have to allow extra space)
    gc = 0 # Each time reset gc count to 0
    win = seq[i:i+w] # Create subset of sequence, called 'win', & assign it to a new variable
    for nt in win:
        if nt == 'G' or nt == 'C': gc += 1 # Count up every NT in that window
    # print(f'{i} {win} {gc/w:.4f}') # f string syntax; 4 sig figs 
    print(i, win, gc/w) # Print out i, window itself( whatever the sequence was in that window), & gc count/window

"""
0 ACGTG 0.6
1 CGTGC 0.8
2 GTGCG 0.8
3 TGCGC 0.8
4 GCGCG 1.0
5 CGCGC 1.0
6 GCGCG 1.0
7 CGCGC 1.0
8 GCGCG 1.0
9 CGCGC 1.0
10 GCGCG 1.0
11 CGCGC 1.0
12 GCGCG 1.0
13 CGCGC 1.0
14 GCGCG 1.0
15 CGCGC 1.0
"""