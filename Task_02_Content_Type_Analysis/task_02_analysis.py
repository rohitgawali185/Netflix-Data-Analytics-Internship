
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# NETFLIX CONTENT TYPE ANALYSIS
# ==========================================

# Step 1: Load Cleaned Dataset
netflix_data = pd.read_csv(
    "data/processed/netflix_cleaned.csv"
)

# Step 2: Dataset Overview
print("=" * 55)
print("       NETFLIX CONTENT TYPE ANALYSIS")
print("=" * 55)

print("\nDataset Shape:", netflix_data.shape)

print("\nTotal Records:", len(netflix_data))

# Step 3: Content Type Count
content_count = netflix_data["type"].value_counts()

print("\nCONTENT TYPE DISTRIBUTION")
print("-" * 40)
print(content_count)

# Step 4: Total Movies and TV Shows
total_movies = content_count.get("Movie", 0)
total_tv_shows = content_count.get("TV Show", 0)

print("\nTOTAL CONTENT")
print("-" * 40)
print("Total Movies:", total_movies)
print("Total TV Shows:", total_tv_shows)
print("Total Content:", total_movies + total_tv_shows)

print("\nAnalysis completed successfully!")
# Step 5: Calculate Content Percentage

total_content = len(netflix_data)

movie_percentage = (total_movies / total_content) * 100
tv_show_percentage = (total_tv_shows / total_content) * 100

print("\nCONTENT TYPE PERCENTAGE")
print("-" * 40)

print(f"Movies Percentage: {movie_percentage:.2f}%")
print(f"TV Shows Percentage: {tv_show_percentage:.2f}%")

# Step 6: Content Distribution Bar Chart

plt.figure(figsize=(10, 6))

sns.countplot(
    data=netflix_data,
    x="type",
    hue="type",
    palette="viridis",
    legend=False
)

plt.title(
    "Netflix Content Type Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Content Type", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

# Display Count Labels
for j, count in enumerate(content_count.values):
    plt.text(
        j,
        count + 100,
        str(count),
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

plt.tight_layout()

# Save Chart
plt.savefig(
    "reports/charts/content_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nBar Chart saved successfully!")

# Step 7: Content Proportion Pie Chart

plt.figure(figsize=(9, 7))

plt.pie(
    [total_movies, total_tv_shows],
    labels=["Movies", "TV Shows"],
    autopct="%1.2f%%",
    startangle=90,
    explode=(0.05, 0),
    shadow=True,
    colors=["#6C63FF", "#FF6584"],
    textprops={"fontsize": 12}
)

plt.title(
    "Netflix Content Type Proportion",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

# Save Pie Chart
plt.savefig(
    "reports/charts/content_proportion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nPie Chart saved successfully!")

# Step 8: Business Insights

print("\n" + "=" * 55)
print("           NETFLIX BUSINESS INSIGHTS")
print("=" * 55)

print("\n1. Movies Distribution:")
print(f"   Netflix has {total_movies} Movies.")
print(f"   Movies represent {movie_percentage:.2f}% of total content.")

print("\n2. TV Shows Distribution:")
print(f"   Netflix has {total_tv_shows} TV Shows.")
print(f"   TV Shows represent {tv_show_percentage:.2f}% of total content.")

print("\n3. Content Comparison:")
difference = total_movies - total_tv_shows

print(f"   Movies exceed TV Shows by {difference} titles.")

print("\n4. Key Finding:")
print("   Movies dominate the Netflix content library.")
print("   Movies account for a larger share than TV Shows.")

print("\n" + "=" * 55)
print("          ANALYSIS COMPLETED")
print("=" * 55)
