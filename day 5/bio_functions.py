# Day 5: DNA Transcription + Translation

# Codon table (very small one for demo)
codon_table = {
    "ATG": "M",  # Start codon → Methionine
    "TTT": "F",
    "TTC": "F",
    "TAA": "*"   # Stop codon
}

# Function 1: DNA → RNA
def transcribe(dna):
    return dna.replace("T", "U")

# Function 2: DNA → Protein
def translate(dna):
    protein = ""
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        aa = codon_table.get(codon, "X")  # Unknown codons → X
        protein += aa
    return protein

# Input from user
dna = input("Enter DNA sequence: ").strip().upper()

# Check multiples of 3
if len(dna) % 3 != 0:
    print("Length must be multiple of 3.")
else:
    rna = transcribe(dna)
    protein = translate(dna)

    print("RNA:     ", rna)
    print("Protein: ", protein)
