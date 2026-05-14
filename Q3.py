'''Using a SeqRecord object, write the DNA sequence along with its annotations (e.g., gene name,
function) to a GenBank file format'''

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

dna_seq = Seq("ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")

record = SeqRecord(
  dna_seq,
  id = "seq1",
  name = "Example_gene",
  description = "Example Gene Sequence",
  annotations = {
    "molecule_type" : "DNA", #wont work without this line
    "gene" : "ExampleGene",
    "function" : "Hypothetical Protein"
  }
)

op_fp = "genbank_file.gb"

with open(op_fp, "w") as op:
  SeqIO.write(record, op, "genbank")

print("Successful\n")

with open(op_fp, "r") as ip:
  print("Contents of the GenBank file are:\n",SeqIO.read(ip,"genbank"))