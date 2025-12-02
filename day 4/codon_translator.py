# Dictionary of codons and amino acids
codon_table = {
    "ATG": "Methionine (M)",
    "TTT": "Phenylalanine (F)",
    "TTC": "Phenylalanine (F)",
    "TAA": "STOP",
    "TAG": "STOP",
    "TGA": "STOP"
}

while True:
    codon = input("Enter a codon (or 'q' to quit): ").upper()
    
    if codon == 'Q':
        print("Exiting...")
        break
    
    # Check if codon length is valid
    if len(codon) != 3:
        print("Codon must be of length 3!\n")
        continue
    
    # Lookup in dictionary
    if codon in codon_table:
        print("Amino Acid:", codon_table[codon], "\n")
    else:
        print("Unknown codon! Try again.\n")
