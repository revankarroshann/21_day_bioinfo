
# list to store (id, seq) tuples
sequences = []

# ---- Add a few sequences manually ----
sequences.append(("seq1", "ATGCAGT"))
sequences.append(("seq2", "AATTCC"))
sequences.append(("seq3", "GATGGG"))

# ---- Read (print all) ----
print("\nStored sequences:")
for i, (sid, seq) in enumerate(sequences):
    print(f"{i}: {sid} -> {seq}")

# ---- Stats using list comprehension + set ----
lengths = [len(seq) for (_id, seq) in sequences]   # list comp
unique_lengths = set(lengths)                      # set

print("\nStats:")
print(f"Total sequences: {len(sequences)}")
print(f"Lengths: {lengths}")
print(f"Unique lengths: {unique_lengths}")
print(f"Min length: {min(lengths)}, Max length: {max(lengths)}")

