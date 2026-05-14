'''Using Bio.pairwise2, perform pairwise sequence alignment of two DNA sequences. Print the
alignment result and the alignment score.'''

from Bio.Align import PairwiseAligner

# Define two DNA sequences
seq1 = "AGTACACTGGT"
seq2 = "AGTACGCTGGT"

aligner = PairwiseAligner()
alignment = aligner.align(seq1, seq2)

print("Aligned Sequences:")
print(alignment[0])
print(alignment.score)