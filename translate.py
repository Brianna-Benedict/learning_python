import sys
import argparse
import mcb185

parser = argparse.ArgumentParser(description = 'translate RNAs to proteins')
parser.add_argument('--seq', required = True, type = str, nargs = '+', metavar = '<str>', 
	help = 'DNA sequ (file or sequences sep by spaces))')
arg = parser.parse_args()

if '.fa' in arg.seq:
	for name, seq in mcb185.read_fasta(arg.seq):
		print(f'>{name}') # Will print >name - looks like a fasta file
		print(mcb185.translate(seq))
else:
	for string in arg.seq:
		print(mcb185.translate(string))

"""
for seq in sys.argv[1:]:
	prot = ''
	for i in range(0, len(seq), 3):
		prot += gcode[seq[i:i+3]]
	print(prot)
"""
# You have been given the code above
# An example command line is
#	python3 translate.py ATGCGCCCGAACTAG ATGAAACCCGGGTTT

# Your task is to write a new program with the following features
# 1. Proper command line (argparse)
# 2. Reads sequences in from fasta format rather than sys.argv
# 3. Outputs sequences as fasta format
# 4. Accepts both uppercase and lowercase letters
# 5. Translates ambiguous amino acids as X (e.g. for weird codons)

# Hints
# 1. add functions and put them in your library
# 2. use string.upper() to normalize case
