# Day 13: Data Cleaning & Prep for Dashboard

import pandas as pd
import os

# Safe path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(BASE_DIR, "sample_expression_dirty.csv")
output_path = os.path.join(BASE_DIR, "cleaned_expression.csv")

# Load dirty data
df = pd.read_csv(input_path)

print("\n=== RAW DATA ===")
print(df)

# Convert expression to numeric (invalid values -> NaN)
df["expression"] = pd.to_numeric(df["expression"], errors="coerce")

# Remove rows with missing values
clean_df = df.dropna()

print("\n=== CLEANED DATA ===")
print(clean_df)

# Save cleaned data
clean_df.to_csv(output_path, index=False)

print("\nCleaned data saved as cleaned_expression.csv")
