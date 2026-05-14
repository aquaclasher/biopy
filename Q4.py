'''Given a FASTA file, write a Python script that reads the file and converts it into GenBank format,
while preserving the sequence and annotations.'''

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def convert(fasta_file, gen):
  records = []
  for record in SeqIO.parse(fasta_file, "fasta"):
    gb_record = SeqRecord(
      record.seq,
      id = record.id,
      name = "ExampleGene",
      description= record.description,
      annotations={
        "molecule_type":"DNA",
        "gene":"ExampleGene",
        "function":"Hypothetical Protein"
      }
    )

    records.append(gb_record)

  with open(gen, "w") as op:
    SeqIO.write(records, op, "genbank")
  
  print("DOne")
fasta_file = "fasta_file.fasta"
gen_file = "genbank_file.gb"

convert(fasta_file,gen_file)

print(f"Contents of GenBank records:\n")
for record in SeqIO.parse(gen_file, "genbank"):
  print(record)