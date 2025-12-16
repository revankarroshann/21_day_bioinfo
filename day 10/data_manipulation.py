import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\rrosh\OneDrive\Desktop\21_day_bioinfo\day 10\genes_extended.csv"
)

print("\n=== FULL DATA ===")
print(df)

# 1) FILTER: genes with expression > 80
high = df[df["expression"] > 80]
print("\n=== EXPRESSION > 80 ===")
print(high)

# 2) GROUPBY: average expression per pathway
grouped = df.groupby("pathway")["expression"].mean()
print("\n=== AVERAGE EXPRESSION BY PATHWAY ===")
print(grouped)

# 3) SAVE results
high.to_csv("high_expression_genes_day10.csv", index=False)
grouped.to_csv("pathway_expression_summary_day10.csv")

print("\nSaved outputs:")
print("- high_expression_genes_day10.csv")
print("- pathway_expression_summary_day10.csv")
