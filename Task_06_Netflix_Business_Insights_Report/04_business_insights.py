
import pandas as pd
import os

# ==========================================================
# PROJECT PATHS
# ==========================================================

base_path = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    base_path, "data", "processed", "netflix_cleaned.csv"
)

report_path = os.path.join(base_path, "reports")
os.makedirs(report_path, exist_ok=True)

# Load Dataset
netflix_df = pd.read_csv(dataset_path)

# ==========================================================
# BUSINESS ANALYSIS
# ==========================================================

total_content = len(netflix_df)

content_types = netflix_df["type"].value_counts()

movie_count = content_types.get("Movie", 0)
tv_count = content_types.get("TV Show", 0)

movie_percentage = (movie_count / total_content) * 100
tv_percentage = (tv_count / total_content) * 100

# Country Analysis
country_counts = (
    netflix_df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

country_counts = country_counts[
    country_counts != "Not Given"
].value_counts()

top_country = country_counts.index[0]
top_country_count = country_counts.iloc[0]

# Genre Analysis
genre_counts = (
    netflix_df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

top_genre = genre_counts.index[0]
top_genre_count = genre_counts.iloc[0]

# Release Year Analysis
year_counts = netflix_df["release_year"].value_counts()

peak_year = year_counts.idxmax()
peak_year_count = year_counts.max()

# Rating Analysis
rating_counts = netflix_df["rating"].value_counts()

top_rating = rating_counts.index[0]
top_rating_count = rating_counts.iloc[0]

rating_percentage = (top_rating_count / total_content) * 100

# Director Analysis
director_counts = (
    netflix_df[netflix_df["director"] != "Not Given"]["director"]
    .value_counts()
)

top_director = director_counts.index[0]
top_director_count = director_counts.iloc[0]

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

insights = [
    f"1. CONTENT DISTRIBUTION: Movies represent {movie_percentage:.2f}% "
    f"of the total catalog, while TV Shows represent {tv_percentage:.2f}%.",

    f"2. COUNTRY PERFORMANCE: {top_country} has the highest number "
    f"of country-associated content records ({top_country_count}).",

    f"3. GENRE PERFORMANCE: {top_genre} is the most frequently "
    f"listed genre with {top_genre_count} entries.",

    f"4. RELEASE YEAR TREND: {peak_year} is the peak release year "
    f"in the dataset, with {peak_year_count} titles.",

    f"5. CONTENT RATINGS: {top_rating} is the most common rating, "
    f"representing {rating_percentage:.2f}% of all titles.",

    f"6. DIRECTOR PERFORMANCE: {top_director} has the highest "
    f"number of directed titles in this dataset ({top_director_count})."
]

recommendations = [
    "1. Maintain a balanced content portfolio by monitoring both "
    "Movies and TV Shows.",

    "2. Study country-wise content performance to identify "
    "opportunities for regional content expansion.",

    "3. Analyze popular genres to guide future content planning.",

    "4. Monitor release-year patterns to understand historical "
    "content trends.",

    "5. Review rating distribution to understand the catalog's "
    "content classification mix.",

    "6. Track director contributions to identify recurring "
    "creative partnerships."
]

# ==========================================================
# GENERATE BUSINESS INSIGHTS REPORT
# ==========================================================

report_file = os.path.join(
    report_path, "Netflix_Business_Insights_Report.txt"
)

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("           NETFLIX BUSINESS INSIGHTS REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write("1. EXECUTIVE SUMMARY\n")
    file.write("-" * 70 + "\n")
    file.write(f"Total Netflix Titles Analyzed: {total_content}\n")
    file.write(f"Movies: {movie_count} ({movie_percentage:.2f}%)\n")
    file.write(f"TV Shows: {tv_count} ({tv_percentage:.2f}%)\n\n")

    file.write("2. KEY BUSINESS INSIGHTS\n")
    file.write("-" * 70 + "\n")

    for insight in insights:
        file.write(insight + "\n\n")

    file.write("3. BUSINESS RECOMMENDATIONS\n")
    file.write("-" * 70 + "\n")

    for recommendation in recommendations:
        file.write(recommendation + "\n\n")

    file.write("4. DATA QUALITY\n")
    file.write("-" * 70 + "\n")
    file.write(
        f"Missing Values: {netflix_df.isnull().sum().sum()}\n"
    )
    file.write(
        f"Duplicate Records: {netflix_df.duplicated().sum()}\n"
    )

    file.write("\n" + "=" * 70 + "\n")
    file.write("              END OF BUSINESS INSIGHTS REPORT\n")
    file.write("=" * 70 + "\n")

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 70)
print("           NETFLIX BUSINESS INSIGHTS REPORT")
print("=" * 70)

print("\n1. EXECUTIVE SUMMARY")
print("-" * 70)

print("Total Content:", total_content)
print(f"Movies: {movie_count} ({movie_percentage:.2f}%)")
print(f"TV Shows: {tv_count} ({tv_percentage:.2f}%)")

print("\n2. KEY BUSINESS INSIGHTS")
print("-" * 70)

for insight in insights:
    print(insight + "\n")

print("\n3. BUSINESS RECOMMENDATIONS")
print("-" * 70)

for recommendation in recommendations:
    print(recommendation + "\n")

print("\n4. REPORT STATUS")
print("-" * 70)
print("Business Insights Report Generated Successfully!")
print("Report Location:", report_file)

print("\n" + "=" * 70)
