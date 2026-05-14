'''Explain the steps to perform a multiple sequence alignment using MUSCLE in Biopython. Write
a script to align three sequences of your choice and save the results to a file.'''

from Bio import AlignIO
import subprocess

# Define sequences
seq1 = """>seq1
ATGCGTACGTA
"""

seq2 = """>seq2
ATGCGTACGTC
"""

seq3 = """>seq3
ATGCGTACGAG
"""

# Write FASTA input file
with open("input_sequences.fasta", "w") as f:
    f.write(seq1)
    f.write(seq2)
    f.write(seq3)

# Run MUSCLE (assumes MUSCLE is installed and in PATH)
# For MUSCLE v5+, use -in and -out
subprocess.run([
    "muscle",
    "-in", "input_sequences.fasta",
    "-out", "aligned_sequences.fasta"
], check=True)

# Read alignment
alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

# Print result
print(alignment)