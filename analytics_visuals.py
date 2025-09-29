import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- Load cleaned data ----
cleaned_csv = "data/fanduel_week4_2025_cleaned.csv"
df = pd.read_csv(cleaned_csv)

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = [12, 6]

# 1. Scatter Plot: Salary vs Fantasy Points
plt.figure()
sns.scatterplot(data=df, x='Salary', y='fantasy_points', hue='position', s=100, alpha=0.7)
plt.title("FanDuel: Salary vs Fantasy Points")
plt.savefig("salary_vs_points.png")
plt.show()

# 2. Bar Chart: Hit Rate by Position
hit_rates = df.groupby('position')['Hit_10'].mean().sort_values(ascending=False)
plt.figure()
sns.barplot(x=hit_rates.index, y=hit_rates.values, palette="coolwarm")
plt.title("Hit Rate (≥10 Points) by Position")
plt.ylim(0, 1)
plt.savefig("hit_rate_by_position.png")
plt.show()

# 3. Histogram: Distribution of Fantasy Points
plt.figure()
sns.histplot(df['fantasy_points'], bins=30, kde=True, color='purple')
plt.title("Distribution of Fantasy Points")
plt.savefig("fantasy_points_distribution.png")
plt.show()
