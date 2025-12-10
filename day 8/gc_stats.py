import numpy as np

# Sample DNA sequences (normally these would come from FASTA files)
sequences = [
    "ATGCGT",
    "TTTTGGGCCC",
    "ATATATAT",
    "GCGCGCGC"
]

def gc_percent(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100   # No rounding here so NumPy handles precision


# Convert GC% list → NumPy array
gc_values = np.array([gc_percent(seq) for seq in sequences])

print("\nGC% array:", gc_values)

# Use NumPy stats
print("\n📊 GC% Statistics:")
print("Mean GC%:", round(gc_values.mean(), 2))
print("Median GC%:", np.median(gc_values))
print("Max GC%:", gc_values.max())
print("Min GC%:", gc_values.min())
