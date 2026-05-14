'''Create a SeqRecord object for a DNA sequence and add annotations for a gene (start, end position,
description). Modify the annotations and print the updated SeqRecord.'''

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

dna_seq = Seq("ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")

record = SeqRecord(
  dna_seq,
  id = "seq1",
  name = "Example_gene",
  description = "Example Gene Sequence",
)

record.annotations["molecule_type"] = "DNA"
record.annotations["gene"] = "ExampleGene"
record.annotations["function"] = "Hypothetical Protein"

from Bio.SeqFeature import SeqFeature, FeatureLocation

gene_feature = SeqFeature(FeatureLocation(0,21),type = "gene", qualifiers={"gene":"ExampleGene"})
record.features.append(gene_feature)

record.annotations["function"] = "Hypothetical Protein with modified function"

SeqIO.write(record, "genbank_file.gb","genbank")

