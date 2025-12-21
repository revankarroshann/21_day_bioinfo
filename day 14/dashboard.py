# Day 14: Bio-Data Dashboard
# Load cleaned data, compute stats, and visualize expression

import pandas as pd
import matplotlib.pyplot as plt
import os

# Get script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
csv_path = os.path.join(BASE_DIR, "cleaned_expression.csv")
plot_path = os.path.join(BASE_DIR, "expression_plot.png")

# Load cleaned data
df = pd.read_csv(csv_path)

print("\n=== CLEANED DATA ===")
print(df)

# Summary statistics
print("\n=== SUMMARY STATISTICS ===")
print(df["expression"].describe())

# Create bar plot
plt.figure(figsize=(8, 5))
plt.bar(df["gene"], df["expression"])
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Dashboard")

# Save plot
plt.savefig(plot_path)
plt.show()

print("\nDashboard plot saved as expression_plot.png")
