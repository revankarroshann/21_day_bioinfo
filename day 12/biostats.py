# Day 12: Biostatistics on Gene Expression

import pandas as pd
import os

# Safe path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "gene_expression_two.csv")

# Load data
df = pd.read_csv(csv_path)

print("\n=== DATA ===")
print(df)

# Basic statistics
print("\n=== BASIC STATS ===")
print("Mean (Sample 1):", df["expression_sample1"].mean())
print("Median (Sample 1):", df["expression_sample1"].median())
print("Std Dev (Sample 1):", round(df["expression_sample1"].std(), 2))

# Correlation between two samples
corr = df["expression_sample1"].corr(df["expression_sample2"])
print("\nCorrelation between Sample 1 and Sample 2:", round(corr, 3))
