
import pandas as pd
import plotly.express as px
import os

# ==========================================================
# PROJECT PATHS
# ==========================================================

base_path = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    base_path, "data", "processed", "netflix_cleaned.csv"
)

dashboard_path = os.path.join(base_path, "dashboard")
os.makedirs(dashboard_path, exist_ok=True)

# Load Dataset
netflix_df = pd.read_csv(dataset_path)

print("=" * 65)
print("       NETFLIX PROFESSIONAL VISUAL DASHBOARD")
print("=" * 65)

# ==========================================================
# CHART 1: CONTENT TYPE DISTRIBUTION
# ==========================================================

content_counts = netflix_df["type"].value_counts().reset_index()
content_counts.columns = ["Content Type", "Count"]

fig1 = px.pie(
    content_counts,
    names="Content Type",
    values="Count",
    title="Netflix Content Type Distribution",
    hole=0.5,
    color_discrete_sequence=["#E50914", "#5646A5"]
)

fig1.update_traces(
    textinfo="label+percent",
    textposition="inside"
)

fig1.update_layout(
    template="plotly_dark",
    title_x=0.5
)

fig1.write_html(
    os.path.join(dashboard_path, "01_Content_Distribution.html")
)

print("\n1. Content Distribution Chart Created Successfully")


# ==========================================================
# CHART 2: TOP 10 COUNTRIES
# ==========================================================

country_counts = (
    netflix_df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

country_counts = country_counts[
    country_counts != "Not Given"
].value_counts().head(10).reset_index()

country_counts.columns = ["Country", "Content Count"]

fig2 = px.bar(
    country_counts.sort_values("Content Count"),
    x="Content Count",
    y="Country",
    orientation="h",
    title="Top 10 Netflix Content Producing Countries",
    text="Content Count",
    color="Content Count",
    color_continuous_scale="Reds"
)

fig2.update_layout(
    template="plotly_dark",
    title_x=0.5,
    yaxis_title="Country",
    xaxis_title="Number of Titles"
)

fig2.write_html(
    os.path.join(dashboard_path, "02_Country_Analysis.html")
)

print("2. Country Analysis Chart Created Successfully")


# ==========================================================
# CHART 3: TOP 10 GENRES
# ==========================================================

genre_counts = (
    netflix_df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
    .reset_index()
)

genre_counts.columns = ["Genre", "Content Count"]

fig3 = px.bar(
    genre_counts.sort_values("Content Count"),
    x="Content Count",
    y="Genre",
    orientation="h",
    title="Top 10 Popular Netflix Genres",
    text="Content Count",
    color="Content Count",
    color_continuous_scale="Purples"
)

fig3.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Number of Titles",
    yaxis_title="Genre"
)

fig3.write_html(
    os.path.join(dashboard_path, "03_Genre_Analysis.html")
)

print("3. Genre Analysis Chart Created Successfully")


# ==========================================================
# CHART 4: RELEASE YEAR TREND
# ==========================================================

year_counts = (
    netflix_df["release_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_counts.columns = ["Release Year", "Content Count"]

fig4 = px.line(
    year_counts,
    x="Release Year",
    y="Content Count",
    title="Netflix Content Release Year Trend",
    markers=True
)

fig4.update_traces(
    line=dict(width=3),
    marker=dict(size=6)
)

fig4.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Release Year",
    yaxis_title="Number of Titles"
)

fig4.write_html(
    os.path.join(dashboard_path, "04_Release_Year_Trend.html")
)

print("4. Release Year Trend Chart Created Successfully")


# ==========================================================
# FINAL SUMMARY
# ==========================================================

print("\n" + "=" * 65)
print("       ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
print("=" * 65)

print("\nDashboard Files:")

for file_name in os.listdir(dashboard_path):
    print("-", file_name)

print("\nDashboard Location:")
print(dashboard_path)

print("\n" + "=" * 65)
