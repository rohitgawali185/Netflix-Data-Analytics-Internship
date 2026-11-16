
# ============================================================
# TASK 4: NETFLIX RELEASE YEAR TREND ANALYSIS
# Auspify Technologies - Data Analytics Internship
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# STEP 1: LOAD CLEANED DATASET
# ------------------------------------------------------------

print("=" * 65)
print("          NETFLIX RELEASE YEAR TREND ANALYSIS")
print("=" * 65)

project_path = Path(__file__).resolve().parent.parent

file_path = (
    project_path /
    "data" /
    "processed" /
    "netflix_cleaned.csv"
)

netflix_data = pd.read_csv(file_path)

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 65)

print("Dataset Shape:", netflix_data.shape)

print("\nColumn Names:")
print(netflix_data.columns.tolist())

print("\nFirst 5 Records:")
print(netflix_data.head())

print("\nRelease Year Information:")
print(netflix_data["release_year"].describe())

print("\nContent Type Distribution:")
print(netflix_data["type"].value_counts())

print("\nMissing Values:")
print(netflix_data.isnull().sum())

print("\n" + "=" * 65)
print("          STEP 1 COMPLETED")
print("=" * 65)

# ------------------------------------------------------------
# STEP 2: YEAR-WISE CONTENT AGGREGATION
# ------------------------------------------------------------

print("\n2. YEAR-WISE CONTENT AGGREGATION")
print("-" * 65)

# Group content by release year
yearly_summary = (
    netflix_data
    .groupby("release_year")
    .agg(
        total_content=("show_id", "count"),
        movie_count=("type", lambda j: (j == "Movie").sum()),
        tv_show_count=("type", lambda j: (j == "TV Show").sum())
    )
    .reset_index()
)

# Sort by release year
yearly_summary = yearly_summary.sort_values(
    by="release_year"
).reset_index(drop=True)

print("\nYear-Wise Content Summary:")
print(yearly_summary.tail(15).to_string(index=False))

print("\nTotal Years Analyzed:", yearly_summary["release_year"].nunique())

# Identify year with maximum content
highest_year = yearly_summary.loc[
    yearly_summary["total_content"].idxmax()
]

print("\nYear with Highest Content Releases:")
print("Year:", highest_year["release_year"])
print("Total Content:", highest_year["total_content"])

# Export yearly summary
output_path = Path(__file__).resolve().parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

yearly_summary.to_csv(
    output_path / "yearly_content_summary.csv",
    index=False
)

print("\nYearly Summary Exported Successfully!")

print("\n" + "=" * 65)
print("          STEP 2 COMPLETED")
print("=" * 65)

# ============================================================
# STEP 3: YEAR-OVER-YEAR GROWTH & DECLINE ANALYSIS
# ============================================================

print("\n" + "=" * 65)
print("       YEAR-OVER-YEAR GROWTH & DECLINE ANALYSIS")
print("=" * 65)

# Calculate yearly content changes
yearly_summary = yearly_summary.sort_values(
    by="release_year"
).reset_index(drop=True)

yearly_summary["content_change"] = (
    yearly_summary["total_content"].diff()
)

yearly_summary["growth_percentage"] = (
    yearly_summary["total_content"]
    .pct_change(fill_method=None) * 100
).round(2)

# Identify growth or decline
yearly_summary["trend"] = yearly_summary[
    "growth_percentage"
].apply(
    lambda j: (
        "First Year" if pd.isna(j)
        else "Growth" if j > 0
        else "Decline" if j < 0
        else "No Change"
    )
)

# Display recent 15 years
print("\nYearly Growth and Decline:")
print(
    yearly_summary.tail(15).to_string(index=False)
)

# Find highest growth and decline years
valid_trends = yearly_summary[
    yearly_summary["release_year"] >= 2007
].dropna(
    subset=["growth_percentage"]
)


highest_growth = valid_trends.loc[
    valid_trends["growth_percentage"].idxmax()
]

highest_decline = valid_trends.loc[
    valid_trends["growth_percentage"].idxmin()
]

print("\nHighest Growth Year:")
print("Year:", int(highest_growth["release_year"]))
print("Growth:", highest_growth["growth_percentage"], "%")

print("\nHighest Decline Year:")
print("Year:", int(highest_decline["release_year"]))
print("Change:", highest_decline["growth_percentage"], "%")

# Export trend analysis
output_path = Path(__file__).resolve().parent / "output"
output_path.mkdir(parents=True, exist_ok=True)

yearly_summary.to_csv(
    output_path / "yearly_trend_analysis.csv",
    index=False
)

print("\nTrend Analysis Exported Successfully!")

print("\n" + "=" * 65)
print("          STEP 3 COMPLETED")
print("=" * 65)

# ============================================================
# STEP 4: DATA VISUALIZATION
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

visualization_path = Path(__file__).resolve().parent / "visualizations"
visualization_path.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="darkgrid")

plt.figure(figsize=(14, 7))

sns.barplot(
    data=yearly_summary,
    x="release_year",
    y="total_content",
    color="steelblue"
)

plt.title(
    "Netflix Content Releases by Year",
    fontsize=18,
    fontweight="bold"
)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Total Content", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualization_path / "01_Year_Wise_Content_Releases.png",
    dpi=300
)

plt.show()
plt.close()

print("Year-Wise Content Chart Saved Successfully!")

# ============================================================
# STEP 4.2: GROWTH & DECLINE TREND CHART
# ============================================================

plt.figure(figsize=(14, 7))

sns.lineplot(
    data=yearly_summary,
    x="release_year",
    y="growth_percentage",
    marker="o",
    linewidth=2.5,
    color="darkorange"
)

plt.axhline(y=0, color="black", linestyle="--")

plt.title(
    "Netflix Year-over-Year Content Growth Trend",
    fontsize=18,
    fontweight="bold"
)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Growth / Decline (%)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualization_path / "02_Yearly_Growth_Trend.png",
    dpi=300
)

plt.show()
plt.close()

print("Growth Trend Chart Saved Successfully!")

# ============================================================
# STEP 4.3: MOVIES VS TV SHOWS TREND
# ============================================================

plt.figure(figsize=(14, 7))

plt.plot(
    yearly_summary["release_year"],
    yearly_summary["movie_count"],
    marker="o",
    linewidth=2.5,
    label="Movies"
)

plt.plot(
    yearly_summary["release_year"],
    yearly_summary["tv_show_count"],
    marker="o",
    linewidth=2.5,
    label="TV Shows"
)

plt.title(
    "Netflix Movies vs TV Shows Release Trend",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualization_path / "03_Movies_vs_TV_Shows_Trend.png",
    dpi=300
)

plt.show()
plt.close()

print("Movies vs TV Shows Trend Chart Saved Successfully!")

# ============================================================
# STEP 5: BUSINESS INSIGHTS REPORT
# ============================================================

report_path = Path(__file__).resolve().parent / "documentation"
report_path.mkdir(parents=True, exist_ok=True)

highest_content = yearly_summary.loc[
    yearly_summary["total_content"].idxmax()
]

valid_trends = yearly_summary[
    yearly_summary["release_year"] >= 2007
].dropna(
    subset=["growth_percentage"]
)


highest_growth = valid_trends.loc[
    valid_trends["growth_percentage"].idxmax()
]

highest_decline = valid_trends.loc[
    valid_trends["growth_percentage"].idxmin()
]

total_movies = netflix_data[
    netflix_data["type"] == "Movie"
].shape[0]

total_tv_shows = netflix_data[
    netflix_data["type"] == "TV Show"
].shape[0]

report = f"""
============================================================
       NETFLIX RELEASE YEAR TREND ANALYSIS
              BUSINESS INSIGHTS REPORT
============================================================

1. PROJECT OVERVIEW
------------------------------------------------------------
Project: Netflix Release Year Trend Analysis
Dataset: Netflix Cleaned Dataset
Total Records: {len(netflix_data)}
Total Movies: {total_movies}
Total TV Shows: {total_tv_shows}
Years Analyzed: {yearly_summary['release_year'].nunique()}

2. KEY FINDINGS
------------------------------------------------------------
Highest Content Release Year:
Year: {int(highest_content['release_year'])}
Total Content: {int(highest_content['total_content'])}

Highest Year-over-Year Growth:
Year: {int(highest_growth['release_year'])}
Growth: {highest_growth['growth_percentage']}%

Highest Year-over-Year Decline:
Year: {int(highest_decline['release_year'])}
Change: {highest_decline['growth_percentage']}%

3. CONTENT TYPE INSIGHTS
------------------------------------------------------------
Total Movies: {total_movies}
Total TV Shows: {total_tv_shows}

Movies represent the larger share of the dataset.
TV Shows also show substantial growth in recent
release years within the available dataset.

4. BUSINESS INSIGHTS
------------------------------------------------------------
1. Content releases increased significantly over
   several years, reaching a peak in 2018.

2. The number of titles by original release year
   declined after 2018 in this dataset.

3. Movies account for a larger share of the total
   Netflix catalog than TV Shows.

4. TV Show releases increased in the later years
   compared with earlier years.

5. These patterns can help understand the historical
   composition of the Netflix content catalog.

5. CONCLUSION
------------------------------------------------------------
The analysis identifies release-year patterns,
yearly content changes, and differences between
Movies and TV Shows.

Note: Release year represents the original year
of content release, not the date Netflix added it.

============================================================
                 END OF REPORT
============================================================
"""

report_file = report_path / "Business_Insights_Report.txt"
report_file.write_text(report, encoding="utf-8")

print("\nBusiness Insights Report Generated Successfully!")
print("Report Location:", report_file)
