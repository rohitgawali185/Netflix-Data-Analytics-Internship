import pandas as pd
import os
import plotly.express as px

# Project paths
base_path = os.path.dirname(os.path.abspath(__file__))


dataset_path = os.path.join(
    base_path,
    "data",
    "processed",
    "netflix_cleaned.csv"
)

netflix_data = pd.read_csv(dataset_path)


# Load dataset
netflix_data = pd.read_csv(dataset_path)

print("=" * 60)
print("     NETFLIX CONTENT RATING & GENRE ANALYSIS")
print("=" * 60)

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 60)

print("Dataset Shape:", netflix_data.shape)

print("\nColumn Names:")
print(netflix_data.columns.tolist())

# Rating Analysis
print("\n2. CONTENT RATING ANALYSIS")
print("-" * 60)

rating_counts = netflix_data["rating"].value_counts()

print("\nRating Distribution:")
print(rating_counts)

print("\nTotal Rating Categories:", netflix_data["rating"].nunique())

print("\nTop 5 Content Ratings:")
print(rating_counts.head(5))

# Save rating analysis
output_path = os.path.join(base_path, "output")
os.makedirs(output_path, exist_ok=True)

rating_counts.to_csv(
    os.path.join(output_path, "rating_distribution.csv"),
    header=["Content_Count"]
)

print("\nRating analysis saved successfully!")

# Genre Analysis
print("\n3. GENRE ANALYSIS")
print("-" * 60)

# Split multiple genres and count individually
genre_data = netflix_data["listed_in"].dropna().str.split(",").explode()

genre_data = genre_data.str.strip()

# Calculate genre distribution
genre_counts = genre_data.value_counts()

print("\nTotal Unique Genres:", genre_counts.count())

print("\nTop 10 Most Common Genres:")
print(genre_counts.head(10))

# Save genre analysis
genre_counts.to_csv(
    os.path.join(output_path, "genre_distribution.csv"),
    header=["Content_Count"]
)

print("\nGenre analysis saved successfully!")


print("\n" + "=" * 60)
print("          STEP 2 COMPLETED")
print("=" * 60)

# Rating Comparison Across Content Types
print("\n4. RATING COMPARISON BY CONTENT TYPE")
print("-" * 60)

rating_comparison = pd.crosstab(
    netflix_data["rating"],
    netflix_data["type"]
)

print("\nRating Comparison:")
print(rating_comparison)

# Save comparison
rating_comparison.to_csv(
    os.path.join(output_path, "rating_by_content_type.csv")
)

print("\nRating comparison saved successfully!")

print("\n" + "=" * 60)
print("          STEP 4 COMPLETED")
print("=" * 60)

# INTERACTIVE VISUALIZATIONS
print("\n5. CREATING INTERACTIVE VISUALIZATIONS")
print("-" * 60)

# Create visualization folder
visualization_path = os.path.join(base_path, "visualizations")
os.makedirs(visualization_path, exist_ok=True)

# Chart 1: Content Rating Distribution
rating_chart = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    title="Netflix Content Rating Distribution",
    labels={"x": "Content Rating", "y": "Content Count"},
    color=rating_counts.index
)

rating_chart.write_html(
    os.path.join(visualization_path, "01_rating_distribution.html")
)

# Chart 2: Top 10 Genres
top_genres = genre_counts.head(10)

genre_chart = px.bar(
    x=top_genres.values,
    y=top_genres.index,
    orientation="h",
    title="Top 10 Most Popular Netflix Genres",
    labels={"x": "Content Count", "y": "Genre"}
)

genre_chart.update_layout(yaxis={"categoryorder": "total ascending"})

genre_chart.write_html(
    os.path.join(visualization_path, "02_top_10_genres.html")
)

# Chart 3: Rating Comparison
comparison_data = rating_comparison.reset_index().melt(
    id_vars="rating",
    var_name="Content Type",
    value_name="Content Count"
)

comparison_chart = px.bar(
    comparison_data,
    x="rating",
    y="Content Count",
    color="Content Type",
    barmode="group",
    title="Rating Comparison: Movies vs TV Shows"
)

comparison_chart.write_html(
    os.path.join(visualization_path, "03_rating_comparison.html")
)

# Chart 4: Content Type Distribution
content_type_counts = netflix_data["type"].value_counts()

content_chart = px.pie(
    names=content_type_counts.index,
    values=content_type_counts.values,
    title="Netflix Movies vs TV Shows Distribution",
    hole=0.4
)

content_chart.write_html(
    os.path.join(visualization_path, "04_content_type_distribution.html")
)

print("\nAll 4 Interactive Charts Created Successfully!")

print("\nVisualization Files:")
print(os.listdir(visualization_path))

print("\n" + "=" * 60)
print("       INTERACTIVE VISUALIZATION COMPLETED")
print("=" * 60)

# BUSINESS INSIGHTS REPORT
print("\n6. GENERATING BUSINESS INSIGHTS REPORT")
print("-" * 60)

documentation_path = os.path.join(base_path, "documentation")
os.makedirs(documentation_path, exist_ok=True)

total_records = len(netflix_data)

top_rating = rating_counts.index[0]
top_rating_count = rating_counts.iloc[0]

top_genre = genre_counts.index[0]
top_genre_count = genre_counts.iloc[0]

top_content_type = content_type_counts.index[0]
top_content_count = content_type_counts.iloc[0]

rating_percentage = (top_rating_count / total_records) * 100
content_percentage = (top_content_count / total_records) * 100

report = f"""
============================================================
       NETFLIX CONTENT RATING & GENRE ANALYSIS
                  BUSINESS INSIGHTS REPORT
============================================================

1. DATASET OVERVIEW
------------------------------------------------------------
Total Records       : {total_records}
Total Columns       : {netflix_data.shape[1]}
Unique Ratings      : {rating_counts.count()}
Unique Genres       : {genre_counts.count()}

2. CONTENT RATING INSIGHTS
------------------------------------------------------------
Most Common Rating  : {top_rating}
Content Count       : {top_rating_count}
Percentage          : {rating_percentage:.2f}%

Top 5 Ratings:
{rating_counts.head(5).to_string()}

3. GENRE INSIGHTS
------------------------------------------------------------
Most Common Genre   : {top_genre}
Content Count       : {top_genre_count}

Top 10 Genres:
{genre_counts.head(10).to_string()}

4. CONTENT TYPE INSIGHTS
------------------------------------------------------------
Most Common Type    : {top_content_type}
Content Count       : {top_content_count}
Percentage          : {content_percentage:.2f}%

Content Type Distribution:
{content_type_counts.to_string()}

5. RATING COMPARISON
------------------------------------------------------------
{rating_comparison.to_string()}

6. AUDIENCE TARGETING INSIGHTS
------------------------------------------------------------
- TV-MA is the most common content rating.
- TV-14 is the second most common rating.
- Genre distribution identifies Netflix's major
  content categories.
- Rating comparisons reveal differences between
  Movies and TV Shows.
- Content ratings help classify content for
  different audience suitability levels.

Note: Content ratings indicate suitability classifications.
They do not directly measure actual viewer demographics.

7. FINAL CONCLUSION
------------------------------------------------------------
This analysis examines Netflix content ratings,
genre distribution, and differences between
Movies and TV Shows.

Interactive visualizations support the exploration
of content patterns and audience suitability.

============================================================
                 END OF BUSINESS REPORT
============================================================
"""

report_path = os.path.join(
    documentation_path,
    "Business_Insights_Report.txt"
)

with open(report_path, "w", encoding="utf-8") as report_file:
    report_file.write(report)

print("\nBusiness Insights Report Generated Successfully!")
print("Report Location:", report_path)

print("\n" + "=" * 60)
print("          TASK 5 ANALYSIS COMPLETED")
print("=" * 60)
