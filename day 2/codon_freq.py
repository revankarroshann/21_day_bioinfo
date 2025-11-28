dna = input("Enter DNA sequence: ").upper().strip()

codons = []

# Loop in steps of 3
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        codons.append(codon)

# Count frequency
freq = {}
for c in codons:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print("Codon Frequencies:")
for c, count in freq.items():
    print(c, ":", count)
