
# ============================================================
# TASK 3: COUNTRY-WISE NETFLIX CONTENT ANALYSIS
# Auspify Technologies - Data Analytics Internship
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# STEP 1: LOAD CLEANED DATASET
# ------------------------------------------------------------

print("=" * 60)
print("       COUNTRY-WISE NETFLIX CONTENT ANALYSIS")
print("=" * 60)

project_path = Path(__file__).resolve().parent.parent

file_path = project_path / "data" / "processed" / "netflix_cleaned.csv"

netflix_data = pd.read_csv(file_path)

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 60)

print("Dataset Shape:", netflix_data.shape)

print("\nColumn Names:")
print(netflix_data.columns.tolist())

print("\nFirst 5 Records:")
print(netflix_data.head())

print("\nCountry Column Sample:")
print(netflix_data["country"].head(10))

print("\nDataset Information:")
print(netflix_data.info())

print("\n" + "=" * 60)
print("       STEP 1 COMPLETED")
print("=" * 60)

# ------------------------------------------------------------
# STEP 2: EXTRACT AND CLEAN COUNTRY INFORMATION
# ------------------------------------------------------------

print("\n2. EXTRACTING AND CLEANING COUNTRY DATA")
print("-" * 60)

# Split multiple countries
country_data = netflix_data.assign(
    country=netflix_data["country"].str.split(",")
)

# Convert multiple countries into separate rows
country_data = country_data.explode("country")

# Remove extra spaces
country_data["country"] = country_data["country"].str.strip()
country_data = country_data[
    ~country_data["country"].str.lower().isin(
        ["not given", "unknown"]
    )
].copy()

# Remove empty country values
country_data = country_data[
    country_data["country"].notna() &
    (country_data["country"] != "")
].copy()

# Reset index
country_data.reset_index(drop=True, inplace=True)

print("Original Dataset Records:", len(netflix_data))
print("Country-wise Records:", len(country_data))

print("\nFirst 10 Country Records:")
print(country_data[["title", "country"]].head(10))

print("\nTotal Unique Countries:")
print(country_data["country"].nunique())

print("\nTop 10 Countries by Content Count:")
print(
    country_data["country"]
    .value_counts()
    .head(10)
)

# Save cleaned country data
output_path = Path(__file__).resolve().parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

country_data.to_csv(
    output_path / "country_cleaned_data.csv",
    index=False
)

print("\nCleaned Country Data Exported Successfully!")

print("\n" + "=" * 60)
print("       STEP 2 COMPLETED")
print("=" * 60)

# ------------------------------------------------------------
# STEP 3: COUNTRY-WISE CONTENT AGGREGATION
# ------------------------------------------------------------

print("\n3. COUNTRY-WISE CONTENT AGGREGATION")
print("-" * 60)

# Calculate total content by country
country_summary = (
    country_data
    .groupby("country")
    .agg(
        total_content=("show_id", "count"),
        movie_count=("type", lambda j: (j == "Movie").sum()),
        tv_show_count=("type", lambda j: (j == "TV Show").sum())
    )
    .reset_index()
)

# Sort countries by total content
country_summary = country_summary.sort_values(
    by="total_content",
    ascending=False
).reset_index(drop=True)

# Add ranking
country_summary.insert(
    0,
    "rank",
    range(1, len(country_summary) + 1)
)

print("\nTop 10 Countries by Netflix Content:")
print(country_summary.head(10).to_string(index=False))

print("\nTotal Countries Analyzed:", len(country_summary))

print("\nTop Content Producing Country:")
print(country_summary.iloc[0]["country"])

print("\nHighest Content Count:")
print(country_summary.iloc[0]["total_content"])

# Export country-wise summary
country_summary.to_csv(
    output_path / "country_wise_summary.csv",
    index=False
)

print("\nCountry-Wise Summary Exported Successfully!")

print("\n" + "=" * 60)
print("       STEP 3 COMPLETED")
print("=" * 60)

# ------------------------------------------------------------
# STEP 4: COUNTRY-WISE DATA VISUALIZATION
# ------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

print("\n4. CREATING COUNTRY-WISE VISUALIZATIONS")
print("-" * 60)

# Set visualization style
sns.set_theme(style="darkgrid")

# Select Top 10 Countries
top_countries = country_summary.head(10)

# ------------------------------------------------------------
# CHART 1: TOP 10 COUNTRIES BY CONTENT
# ------------------------------------------------------------

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_countries,
    x="total_content",
    y="country",
    hue="country",
    palette="viridis",
    legend=False
)

plt.title(
    "Top 10 Countries by Netflix Content",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Total Content", fontsize=12)
plt.ylabel("Country", fontsize=12)

plt.tight_layout()

plt.savefig(
    Path(__file__).resolve().parent /
    "visualizations" / "top_10_countries.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ------------------------------------------------------------
# CHART 2: MOVIES VS TV SHOWS BY COUNTRY
# ------------------------------------------------------------

top_countries_plot = top_countries.sort_values(
    by="total_content",
    ascending=True
)

top_countries_plot.set_index("country")[
    ["movie_count", "tv_show_count"]
].plot(
    kind="barh",
    figsize=(12, 7),
    color=["#E50914", "#3498DB"]
)

plt.title(
    "Movies vs TV Shows by Top 10 Countries",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.legend(["Movies", "TV Shows"])

plt.tight_layout()

plt.savefig(
    Path(__file__).resolve().parent /
    "visualizations" / "movies_vs_tv_shows.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nBoth Visualizations Saved Successfully!")

print("\n" + "=" * 60)
print("       STEP 4 COMPLETED")
print("=" * 60)

# ------------------------------------------------------------
# STEP 5: BUSINESS INSIGHTS REPORT
# ------------------------------------------------------------

print("\n5. GENERATING BUSINESS INSIGHTS REPORT")
print("-" * 60)

# Identify key insights
top_country = country_summary.iloc[0]

top_movie_country = country_summary.loc[
    country_summary["movie_count"].idxmax()
]

top_tv_country = country_summary.loc[
    country_summary["tv_show_count"].idxmax()
]

total_countries = country_summary["country"].nunique()

total_movies = country_summary["movie_count"].sum()

total_tv_shows = country_summary["tv_show_count"].sum()

total_content = total_movies + total_tv_shows

# Generate business insights
insights = f"""
============================================================
        NETFLIX COUNTRY-WISE BUSINESS INSIGHTS REPORT
============================================================

PROJECT: Country-Wise Netflix Content Analysis
INTERNSHIP: Auspify Technologies
TOOLS: Python, Pandas, Matplotlib, Seaborn

------------------------------------------------------------
1. DATASET OVERVIEW
------------------------------------------------------------

Original Netflix Records: {len(netflix_data)}
Total Countries Analyzed: {total_countries}
Total Country-Title Records: {len(country_data)}

------------------------------------------------------------
2. KEY PERFORMANCE FINDINGS
------------------------------------------------------------

Top Content Producing Country:
{top_country['country']}

Total Content Records:
{top_country['total_content']}

Country with Highest Movie Count:
{top_movie_country['country']}

Movie Count:
{top_movie_country['movie_count']}

Country with Highest TV Show Count:
{top_tv_country['country']}

TV Show Count:
{top_tv_country['tv_show_count']}

------------------------------------------------------------
3. CONTENT DISTRIBUTION
------------------------------------------------------------

Total Movie Country-Title Records: {total_movies}
Total TV Show Country-Title Records: {total_tv_shows}

------------------------------------------------------------
4. TOP 10 COUNTRIES RANKING
------------------------------------------------------------

{country_summary.head(10).to_string(index=False)}

------------------------------------------------------------
5. BUSINESS INSIGHTS
------------------------------------------------------------

1. {top_country['country']} has the highest
   country-wise Netflix content count.

2. {top_movie_country['country']} has the highest
   movie count among the analyzed countries.

3. {top_tv_country['country']} has the highest
   TV Show count among the analyzed countries.

4. Country-wise analysis helps identify content
   distribution patterns across different markets.

5. These findings can support content planning
   and regional market analysis.

------------------------------------------------------------
6. CONCLUSION
------------------------------------------------------------

The analysis identifies country-wise Netflix content
distribution and highlights the leading countries
based on Movies and TV Shows.

Python Pandas was used for data cleaning, aggregation,
and ranking, while Matplotlib and Seaborn were used
for data visualization.

============================================================
                END OF REPORT
============================================================
"""

# Display report
print(insights)

# Export report
report_path = (
    Path(__file__).resolve().parent /
    "documentation" /
    "business_insights_report.txt"
)

report_path.parent.mkdir(parents=True, exist_ok=True)

with open(report_path, "w", encoding="utf-8") as report_file:
    report_file.write(insights)

print("\nBusiness Insights Report Exported Successfully!")
print("Report Location:", report_path)

print("\n" + "=" * 60)
print("       TASK 3 ANALYSIS COMPLETED")
print("=" * 60)
