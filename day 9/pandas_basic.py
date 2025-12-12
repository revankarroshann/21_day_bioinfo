import pandas as pd   # import pandas

# Load CSV
df = pd.read_csv(r"C:\Users\rrosh\OneDrive\Desktop\21_day_bioinfo\day 9\sample_genes.csv")
print("\n=== FULL DATAFRAME ===")
print(df)

# Show first rows
print("\n=== HEAD ===")
print(df.head())

# Show last rows
print("\n=== TAIL ===")
print(df.tail())

# Summary stats
print("\n=== SUMMARY STATS ===")
print(df.describe())

# Select one column
print("\n=== EXPRESSION COLUMN ===")
print(df["expression"])

# Filter genes above threshold
print("\n=== GENES WITH EXPRESSION > 80 ===")
high = df[df["expression"] > 80]
print(high)
