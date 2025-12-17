# Day 11: Gene Expression Visualization
# Plot gene expression using matplotlib and save as PNG

import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build safe path to CSV file
csv_path = os.path.join(BASE_DIR, "sample_genes.csv")

# Load data
df = pd.read_csv(csv_path)

# Select data for plotting
genes = df["gene"]
expression = df["expression"]

# Create bar plot
plt.figure(figsize=(8, 5))
plt.bar(genes, expression)

# Labels and title
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")

# Save plot in the same folder
output_path = os.path.join(BASE_DIR, "gene_expression_day11.png")
plt.savefig(output_path)

# Show plot
plt.show()

print("Plot saved as gene_expression_day11.png")
