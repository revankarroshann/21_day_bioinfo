import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\rrosh\OneDrive\Desktop\21_day_bioinfo\day 9\sample_genes.csv")

print("\n=== FULL DATA ===")
print(df)

# First few rows
print("\n=== HEAD ===")
print(df.head())

# Last few rows
print("\n=== TAIL ===")
print(df.tail())

# Stats
print("\n=== SUMMARY STATS ===")
print(df.describe())

# High expression filter
threshold = 80   # you can change this
high = df[df["expression"] > threshold]

print(f"\n=== GENES WITH EXPRESSION > {threshold} ===")
print(high)

# Save results
output_file = "high_expression_genes.csv"
high.to_csv(output_file, index=False)

print(f"\nSaved filtered genes to: {output_file}")
