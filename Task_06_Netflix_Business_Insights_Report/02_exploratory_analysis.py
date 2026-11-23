
import pandas as pd
import os

# Project Path
base_path = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    base_path,
    "data",
    "processed",
    "netflix_cleaned.csv"
)

# Load Dataset
netflix_df = pd.read_csv(dataset_path)

print("=" * 65)
print("       NETFLIX EXPLORATORY DATA ANALYSIS")
print("=" * 65)

# 1. Content Distribution
print("\n1. CONTENT TYPE DISTRIBUTION")
print("-" * 65)

content_counts = netflix_df["type"].value_counts()

print(content_counts)

# 2. Content Percentage
print("\n2. CONTENT TYPE PERCENTAGE")
print("-" * 65)

content_percentage = (
    netflix_df["type"].value_counts(normalize=True) * 100
)

print(content_percentage.round(2))

# 3. Top 10 Countries
print("\n3. TOP 10 CONTENT PRODUCING COUNTRIES")
print("-" * 65)

country_counts = (
    netflix_df["country"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

print(country_counts.head(10))

# 4. Top 10 Genres
print("\n4. TOP 10 POPULAR GENRES")
print("-" * 65)

genre_counts = (
    netflix_df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

print(genre_counts.head(10))

# 5. Release Year Analysis
print("\n5. RELEASE YEAR ANALYSIS")
print("-" * 65)

year_counts = netflix_df["release_year"].value_counts().sort_index()

print("Earliest Release Year:", netflix_df["release_year"].min())
print("Latest Release Year:", netflix_df["release_year"].max())
print("Most Content Release Year:", year_counts.idxmax())
print("Highest Yearly Content Count:", year_counts.max())

# 6. Rating Distribution
print("\n6. CONTENT RATING DISTRIBUTION")
print("-" * 65)

print(netflix_df["rating"].value_counts().head(10))

# 7. Director Analysis
print("\n7. TOP 10 DIRECTORS")
print("-" * 65)

director_counts = (
    netflix_df[netflix_df["director"] != "Not Given"]["director"]
    .value_counts()
)

print(director_counts.head(10))

# 8. Duration Analysis
print("\n8. DURATION ANALYSIS")
print("-" * 65)

print("Most Common Durations:")
print(netflix_df["duration"].value_counts().head(10))

# Final Summary
print("\n" + "=" * 65)
print("       EXPLORATORY DATA ANALYSIS COMPLETED")
print("=" * 65)
