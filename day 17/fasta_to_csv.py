# Day 17: FASTA to CSV Converter
# Parse multi-FASTA and export ID, length, GC%

from Bio import SeqIO
import os

# Safe paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fasta_path = os.path.join(BASE_DIR, "multi_sequences.fasta")
csv_path = os.path.join(BASE_DIR, "sequences_summary.csv")

def gc_percent(seq):
    seq = str(seq).upper()
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

# Write CSV
with open(csv_path, "w") as out:
    out.write("id,length,gc_percent\n")
    for record in SeqIO.parse(fasta_path, "fasta"):
        sid = record.id
        length = len(record.seq)
        gc = gc_percent(record.seq)
        out.write(f"{sid},{length},{gc}\n")

print("CSV created:", csv_path)
