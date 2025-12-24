# Day 15: BioPython FASTA Reader
# Reads FASTA file and prints sequence ID and length

from Bio import SeqIO
import os

# Get directory where script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to FASTA file
fasta_path = os.path.join(BASE_DIR, "sample.fasta")

print("\n=== FASTA SEQUENCES ===")

# Parse FASTA file
for record in SeqIO.parse(fasta_path, "fasta"):
    print("ID:", record.id)
    print("Length:", len(record.seq))
    print("-" * 30)
