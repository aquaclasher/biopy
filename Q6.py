'''Write a script that uses Entrez to fetch a nucleotide sequence from the NCBI database by using a
known accession number, and print out the sequence and the related metadata.'''

from Bio import Entrez ,SeqIO

Entrez.email = "swapnil.is23@bmsce.ac.in"

# Step 2: Specify the accession number of the sequence
accession_number = "NM_001301717" # Example accession number for a human gene
# Step 3: Fetch the sequence from GenBank using Entrez
with Entrez.efetch(db = "nucleotide", id = accession_number, rettype= "gb", retmode = "text") as handle:
  seq_record = SeqIO.read(handle, "genbank")

# Step 5: Print the sequence and metadata
print(f"Accession Number: {seq_record.id}")
print(f"Description: {seq_record.description}")
print(f"Organism: {seq_record.annotations['organism']}")
print(f"Sequence: {seq_record.seq}")
print(f"Length of Sequence: {len(seq_record.seq)}")
print(f"Features: {seq_record.features}")
