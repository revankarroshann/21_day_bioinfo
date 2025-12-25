# Day 16: DNA Analyzer
# Performs GC%, complement, transcription, translation

# Codon table (simplified)
CODON_TABLE = {
    "AUG": "M", "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

def gc_percent(seq):
    """Calculate GC percentage"""
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

def complement(seq):
    """Return DNA complement"""
    comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join(comp.get(base, "N") for base in seq.upper())

def transcribe(seq):
    """DNA -> RNA"""
    return seq.upper().replace("T", "U")

def translate(rna):
    """RNA -> Protein"""
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3:
            break
        aa = CODON_TABLE.get(codon, "?")
        if aa == "STOP":
            break
        protein += aa
    return protein

# ---------- TEST ----------
dna = "ATGTTTTACTGA"

print("DNA:", dna)
print("GC%:", gc_percent(dna))
print("Complement:", complement(dna))

rna = transcribe(dna)
print("RNA:", rna)

protein = translate(rna)
print("Protein:", protein)
