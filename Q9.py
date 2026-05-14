'''Using alignment data, construct a phylogenetic tree and visualize it with Bio.Phylo. Label each
branch with the sequence name.'''
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO

alignment = AlignIO.read("input_sequences.fasta", "fasta")

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

constructor = DistanceTreeConstructor()
tree= constructor.upgma(distance_matrix)

Phylo.draw(tree)