import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- Load cleaned data ----
cleaned_csv = "data/fanduel_week4_2025_cleaned.csv"
df = pd.read_csv(cleaned_csv)

# ---- Streamlit Page Setup ----
st.set_page_config(page_title="FanDuel Analytics Dashboard", layout="wide")
st.title("🏈 FanDuel Fantasy Analytics Dashboard")
st.markdown("Analyze player stats, salaries, value scores, and hit rates interactively.")

# ---- Sidebar Filters ----
positions = df['position'].unique()
selected_positions = st.sidebar.multiselect("Filter by Position", positions, default=positions)

salary_tiers = df['Salary_Tier'].unique()
selected_tiers = st.sidebar.multiselect("Filter by Salary Tier", salary_tiers, default=salary_tiers)

filtered_df = df[(df['position'].isin(selected_positions)) & (df['Salary_Tier'].isin(selected_tiers))]

# ---- Scatter Plot: Salary vs Fantasy Points ----
st.subheader("Salary vs Fantasy Points")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x='Salary', y='fantasy_points', hue='position', s=100, alpha=0.7, ax=ax)
st.pyplot(fig)

# ---- Bar Chart: Hit Rate by Position ----
st.subheader("Hit Rate (≥10 Points) by Position")
hit_rates = filtered_df.groupby('position')['Hit_10'].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
sns.barplot(x=hit_rates.index, y=hit_rates.values, palette="coolwarm", ax=ax)
ax.set_ylim(0,1)
st.pyplot(fig)

# ---- Histogram: Distribution of Fantasy Points ----
st.subheader("Distribution of Fantasy Points")
fig, ax = plt.subplots()
sns.histplot(filtered_df['fantasy_points'], bins=30, kde=True, color='purple', ax=ax)
st.pyplot(fig)

# ---- Show Table of Top Value Players ----
st.subheader("Top 20 Value Players (Points per $1K)")
top_value = filtered_df.sort_values(by='Value_Score', ascending=False).head(20)
st.dataframe(top_value[['name','position','team','Salary','fantasy_points','Value_Score']])
