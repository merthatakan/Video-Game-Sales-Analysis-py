import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---  Data Acquisition ---
print("Initializing dataset download from Kaggle...")
dataset_path = kagglehub.dataset_download("gregorut/videogamesales")
csv_file_path = os.path.join(dataset_path, "vgsales.csv")

df = pd.read_csv(csv_file_path)
print(f"Dataset successfully loaded from: {csv_file_path}\n")

# --- Data Exploration & Professional Styling ---
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [12, 7]


# --- Data Cleaning ---
df_cleaned = df.dropna().copy()
df_cleaned['Year'] = df_cleaned['Year'].astype(int)

print("Data Preview (First 5 Rows):")
print(df.head(5))

# --- Analysis - Top Selling Genres in Europe (EU) ---
eu_market_analysis = df.groupby('Genre')['EU_Sales'].sum().sort_values(ascending=False).reset_index()

plt.figure()
sns.barplot(data=eu_market_analysis, x='EU_Sales', y='Genre', palette='viridis')
plt.title('Video Game Sales Performance: European Market (EU)', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales (Millions)', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.tight_layout()
plt.show()

# --- Analysis - Global Sales Trend Over Time ---

yearly_global_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()

plt.figure()
sns.lineplot(data=yearly_global_sales, x='Year', y='Global_Sales', marker='o', color='#e74c3c', linewidth=2.5)
plt.title('Global Video Game Sales Evolution (1980-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Global Sales (Millions)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --- Analysis - Top 10 Publishers in Europe ---
eu_publishers = df_cleaned.groupby('Publisher')['EU_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure()
sns.barplot(data=eu_publishers, x='EU_Sales', y='Publisher', palette='flare')
plt.title('Top 10 Publishers by Sales in Europe', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\nAnalysis complete. Visualizations generated.")