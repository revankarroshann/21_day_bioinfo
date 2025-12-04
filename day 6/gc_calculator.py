# Day 6: GC% Calculator (FASTA or Direct Input)

def gc_percent(seq):
    # Count G and C, calculate GC%
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)


print("Choose Input Method:")
print("1. FASTA File")
print("2. Enter DNA Sequence Directly")

choice = input("Enter 1 or 2: ").strip()
sequences = {}

if choice == "1":
    filename = input("Enter FASTA filename: ").strip()
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        exit()

    current_id = ""
    current_seq = ""

    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if current_id != "":
                sequences[current_id] = current_seq
            current_id = line[1:]  # Remove '>'
            current_seq = ""
        else:
            current_seq += line

    if current_id != "":
        sequences[current_id] = current_seq

elif choice == "2":
    seq = input("Enter DNA sequence: ").strip().upper()
    sequences["seq1"] = seq  # Just name it seq1 by default

else:
    print("Invalid choice!")
    exit()


# Save output to CSV file
with open("gc_output.csv", "w") as csv:
    csv.write("ID,Length,GC%\n")
    for seq_id, seq in sequences.items():
        gc = gc_percent(seq)
        csv.write(f"{seq_id},{len(seq)},{gc}\n")

print("Done! Results saved to gc_output.csv")

