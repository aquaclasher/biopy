'''Using alignment data, construct a phylogenetic tree and visualize it with Bio.Phylo. Label each
branch with the sequence name.'''
from Bio import Phylo
from Bio.SeqRecord import SeqRecord
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq

print("Creating dummy alignment...")
align1 = SeqRecord(Seq("ATGCGTACGTA"), id="seq1")
align2 = SeqRecord(Seq("ATGCGTACGTC"), id="seq2")
align3 = SeqRecord(Seq("ATGCGTACGAG"), id="seq3")
alignment = MultipleSeqAlignment([align1, align2, align3])
AlignIO.write(alignment, "aligned_sequences.aln", "clustal")


alignment = AlignIO.read("aligned_sequences.aln", "clustal")

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

constructor = DistanceTreeConstructor()
tree= constructor.upgma(distance_matrix)

Phylo.draw(tree)