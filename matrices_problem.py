# 4/22/21 exercise- make 4 different mways of making matrices (from memory) 

# 1. Everything in the matrix 
aa = "ACGT"

for nt1 in aa:
    for nt2 in aa:
        print(nt1, nt2)
print('end of matrix 1')

# 2. Everything except the major diagonal 
for nt1 in aa:
    for nt2 in aa:
        if nt1 != nt2: print(nt1, nt2)
print("end of matrix 2")

# 3. All pairwise combinations except redundant ones 
for i in range(len(aa)):
    for j in range(i, len(aa)):
        print(aa[i], aa[j]) # i & j start at same # every time (Ex: i starts at 0, j starts at 0)
print('end of matrix 3')

# 4. No major diagonal & no redundant pairwise cominations 
for i in range(len(aa)):
    for j in range(i + 1, len(aa)): # j starts at a dif # greater than i by 1 (Ex: i starts at 0, j starts at 1)
        print(aa[i], aa[j])
print('end of matrix 4')

"""
A A
A C
A G
A T
C A
C C
C G
C T
G A
G C
G G
G T
T A
T C
T G
T T
end of matrix 1
A C
A G
A T
C A
C G
C T
G A
G C
G T
T A
T C
T G
end of matrix 2
A A
A C
A G
A T
C C
C G
C T
G G
G T
T T
end of matrix 3
A C
A G
A T
C G
C T
G T
end of matrix 4
"""