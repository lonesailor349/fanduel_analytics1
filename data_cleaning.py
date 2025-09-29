import pandas as pd

# Input/output files
raw_csv = "data/fanduel_week4_2025_raw.csv"
cleaned_csv = "data/fanduel_week4_2025_cleaned.csv"

# ---- Load raw data ----
df = pd.read_csv(raw_csv)

# ---- Basic cleaning ----
df = df.dropna(subset=['fantasy_points'])  # remove players w/ no data
df = df[df['Salary'] > 0]  # remove invalid salaries

# ---- Add value metrics ----
df['Value_Score'] = df['fantasy_points'] / (df['Salary'] / 1000)

# Hit thresholds
df['Hit_10'] = df['fantasy_points'] >= 10
df['Hit_20'] = df['fantasy_points'] >= 20
df['Hit_30'] = df['fantasy_points'] >= 30

# Salary tiers
df['Salary_Tier'] = pd.cut(df['Salary'],
                           bins=[0, 4500, 6000, 7500, 10000, 20000],
                           labels=['Cheap', 'Value', 'Mid', 'Stud', 'Elite'])

# ---- Save cleaned file ----
df.to_csv(cleaned_csv, index=False)
print(f"✅ Cleaned data saved to {cleaned_csv}")
