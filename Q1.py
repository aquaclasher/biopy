'''
Using the Seq class from biopython 
create a dna sequence object and slice the sequence to extract a specific region
concat a seq with another seq
transcribe and translate the combined sequence into rna and protein sequences
'''

from Bio.Seq import Seq
import warnings

#warnings.filterwarnings("ignore")

dna_seq = Seq("ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")

# Slice the sequence to extract a specific region
sliced_seq = dna_seq[5:8]
print("Sliced Sequence:", sliced_seq)

new_seq = sliced_seq + sliced_seq
print("Concatenated Sequence: ",new_seq)

#converting into rna

print(f"RNA Sequenec: {new_seq.transcribe()}")

print(f"Protein Sequence: {new_seq.transcribe().translate()}")