from collections import Counter

def clean_seq(seq):
    """
    Removes unwanted characters and converts everything to uppercase.
    Keeps only A, T, G, C, N.
    """
    seq = seq.upper()
    clean = ""
    for base in seq:
        if base in "ATGCN":
            clean += base
    return clean


def base_counts(seq):
    """
    Returns a dictionary with counts of A, T, G, C.
    Missing bases get count 0.
    """
    seq = clean_seq(seq)
    counts = Counter(seq)
    return {
        "A": counts.get("A", 0),
        "T": counts.get("T", 0),
        "G": counts.get("G", 0),
        "C": counts.get("C", 0)
    }
def gc_percentage(seq):
    """Return GC percentage (rounded to 2 decimals)."""
    seq = clean_seq(seq)
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return round(100.0 * gc / len(seq), 2)


def from_fasta(path):
    """
    Minimal FASTA parser: returns dict id -> sequence
    (handles multi-line sequences).
    """
    records = {}
    with open(path, 'r') as f:
        header = None
        seq_chunks = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header:
                    records[header] = ''.join(seq_chunks)
                header = line[1:].split()[0]
                seq_chunks = []
            else:
                seq_chunks.append(line)
        if header:
            records[header] = ''.join(seq_chunks)
    return records


def main():
    print("DNA Base Counter / FASTA inspector\n")
    choice = input("Mode (1) single sequence, (2) FASTA file [1/2]: ").strip()
    if choice == '1':
        seq = input("Paste DNA sequence: ").strip()
        counts = base_counts(seq)
        print("Counts:", counts)
        print("Length:", len(clean_seq(seq)))
        print("GC%:", gc_percentage(seq))
    elif choice == '2':
        path = input("Path to FASTA file (e.g. C:\\Users\\You\\Desktop\\sample.fasta): ").strip()
        try:
            recs = from_fasta(path)
        except FileNotFoundError:
            print("File not found. Check path and try again.")
            return
        print(f"Found {len(recs)} records in FASTA.")
        for rid, seq in recs.items():
            print(f">{rid} | len={len(clean_seq(seq))} | GC%={gc_percentage(seq)} | counts={base_counts(seq)}")
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
