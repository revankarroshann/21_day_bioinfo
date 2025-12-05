# Day 7: CLI Bioinformatics Tool
# Features:
# 1) Add sequences
# 2) List sequences
# 3) Export CSV with GC% and reverse complement

def clean_seq(seq):
    """Keep only A/T/G/C and uppercase."""
    seq = seq.upper()
    valid = []
    for base in seq:
        if base in "ATGC":
            valid.append(base)
    return "".join(valid)


def gc_percent(seq):
    """Return GC% of sequence, rounded to 2 decimals."""
    if len(seq) == 0:
        return 0.0
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)


def reverse_complement(seq):
    """Return reverse complement of DNA sequence."""
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rev = []
    for base in reversed(seq):
        rev.append(comp.get(base, "N"))
    return "".join(rev)


def show_menu():
    print("\n=== Bio CLI Tool ===")
    print("1. Add sequence")
    print("2. List sequences")
    print("3. Export CSV (GC% + reverse complement)")
    print("4. Quit")


def main():
    # Store sequences as: {id: sequence}
    sequences = {}

    while True:
        show_menu()
        choice = input("Choose option [1-4]: ").strip()

        if choice == "1":
            seq_id = input("Enter sequence ID: ").strip()
            if not seq_id:
                print("ID cannot be empty.")
                continue

            if seq_id in sequences:
                print("ID already exists, overwriting previous sequence.")

            raw_seq = input("Enter DNA sequence: ").strip()
            seq = clean_seq(raw_seq)

            if len(seq) == 0:
                print("No valid A/T/G/C bases found. Try again.")
                continue

            sequences[seq_id] = seq
            print(f"Added {seq_id} (length {len(seq)}).")

        elif choice == "2":
            if not sequences:
                print("No sequences stored yet.")
            else:
                print("\nStored sequences:")
                for sid, seq in sequences.items():
                    print(f"- {sid}: {seq} (len={len(seq)})")

        elif choice == "3":
            if not sequences:
                print("No sequences to export.")
                continue

            filename = "day7_output.csv"
            with open(filename, "w") as csv:
                csv.write("ID,Sequence,Length,GC%,ReverseComplement\n")
                for sid, seq in sequences.items():
                    gc = gc_percent(seq)
                    rev = reverse_complement(seq)
                    csv.write(f"{sid},{seq},{len(seq)},{gc},{rev}\n")

            print(f"Exported {len(sequences)} sequence(s) to {filename}.")
            # you can keep working after export, so we don't quit here

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
