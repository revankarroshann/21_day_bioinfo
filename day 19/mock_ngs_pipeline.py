# Day 19: Mock NGS Pipeline
# Simulates FASTQ -> Alignment -> Variant Calling

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Step 1: FASTQ (mock)
fastq_path = os.path.join(BASE_DIR, "sample.fastq")

with open(fastq_path, "w") as f:
    f.write("@read1\nATGCGTAC\n+\nFFFFFFFF\n")
    f.write("@read2\nATGCGTTC\n+\nFFFFFFFF\n")

print("FASTQ file created.")

# Step 2: Alignment (mock SAM)
sam_path = os.path.join(BASE_DIR, "aligned.sam")

with open(sam_path, "w") as f:
    f.write("@SQ\tSN:chr1\tLN:1000\n")
    f.write("read1\t0\tchr1\t100\t255\t8M\t*\t0\t0\tATGCGTAC\t*\n")
    f.write("read2\t0\tchr1\t105\t255\t8M\t*\t0\t0\tATGCGTTC\t*\n")

print("Alignment file (SAM) created.")

# Step 3: Variant Calling (mock VCF)
vcf_path = os.path.join(BASE_DIR, "variants.vcf")

with open(vcf_path, "w") as f:
    f.write("##fileformat=VCFv4.2\n")
    f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
    f.write("chr1\t107\t.\tA\tT\t99\tPASS\t.\n")

print("VCF file created.")

print("\nMock NGS pipeline completed successfully.")
