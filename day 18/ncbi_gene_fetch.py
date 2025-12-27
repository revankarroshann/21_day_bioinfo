# Day 18: Fetch gene information from NCBI using Entrez

from Bio import Entrez

# REQUIRED by NCBI
Entrez.email = "revankarroshan2020@gmail.com"  # change this

# Example: search for TP53 gene in Homo sapiens
query = "TP53[Gene] AND Homo sapiens[Organism]"

# Search NCBI Gene database
handle = Entrez.esearch(db="gene", term=query, retmax=1)
record = Entrez.read(handle)
handle.close()

# Get Gene ID
gene_ids = record["IdList"]

if not gene_ids:
    print("No gene found.")
else:
    gene_id = gene_ids[0]
    print("Gene ID:", gene_id)

    # Fetch gene summary
    handle = Entrez.esummary(db="gene", id=gene_id)
    summary = Entrez.read(handle)
    handle.close()

    gene_info = summary["DocumentSummarySet"]["DocumentSummary"][0]

    print("\n=== GENE INFO ===")
    print("Name:", gene_info["Name"])
    print("Description:", gene_info["Description"])
    print("Chromosome:", gene_info["Chromosome"])
    print("Organism:", gene_info["Organism"]["ScientificName"])
