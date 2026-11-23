
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# ======================================================
# PATH SETUP
# ======================================================

base_path = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    base_path, "data", "processed", "netflix_cleaned.csv"
)

dashboard_path = os.path.join(base_path, "dashboard")
os.makedirs(dashboard_path, exist_ok=True)

# Load Dataset
netflix_df = pd.read_csv(dataset_path)

# ======================================================
# DATA ANALYSIS
# ======================================================

total_titles = len(netflix_df)

content_counts = netflix_df["type"].value_counts()

movie_count = content_counts.get("Movie", 0)
tv_count = content_counts.get("TV Show", 0)

country_counts = (
    netflix_df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

country_counts = country_counts[
    country_counts != "Not Given"
].value_counts()

total_countries = len(country_counts)

top_10_countries = country_counts.head(10)

genre_counts = (
    netflix_df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts().head(10)
)

year_counts = (
    netflix_df["release_year"]
    .value_counts()
    .sort_index()
)

rating_counts = netflix_df["rating"].value_counts()

# ======================================================
# CREATE EXECUTIVE DASHBOARD
# ======================================================

fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{"type": "domain"}, {"type": "bar"}],
        [{"type": "bar"}, {"type": "scatter"}]
    ],
    subplot_titles=(
        "Content Type Distribution",
        "Top 10 Countries",
        "Top 10 Genres",
        "Content Release Year Trend"
    ),
    vertical_spacing=0.16,
    horizontal_spacing=0.12
)

# Chart 1: Content Distribution

fig.add_trace(
    go.Pie(
        labels=content_counts.index,
        values=content_counts.values,
        hole=0.55,
        textinfo="label+percent",
        marker=dict(
            colors=["#E50914", "#6254A5"]
        ),
        name="Content Type"
    ),
    row=1,
    col=1
)

# Chart 2: Country Analysis

fig.add_trace(
    go.Bar(
        x=country_counts.values[::-1],
        y=country_counts.index[::-1],
        orientation="h",
        marker_color="#E50914",
        text=country_counts.values[::-1],
        textposition="outside",
        name="Countries"
    ),
    row=1,
    col=2
)

# Chart 3: Genre Analysis

fig.add_trace(
    go.Bar(
        x=genre_counts.values[::-1],
        y=genre_counts.index[::-1],
        orientation="h",
        marker_color="#6254A5",
        text=genre_counts.values[::-1],
        textposition="outside",
        name="Genres"
    ),
    row=2,
    col=1
)

# Chart 4: Release Year Trend

fig.add_trace(
    go.Scatter(
        x=year_counts.index,
        y=year_counts.values,
        mode="lines+markers",
        line=dict(
            color="#E50914",
            width=3
        ),
        marker=dict(size=6),
        name="Yearly Releases"
    ),
    row=2,
    col=2
)

# ======================================================
# DASHBOARD DESIGN
# ======================================================


fig.update_layout(
    title=dict(
        text=(
            "NETFLIX BUSINESS INTELLIGENCE DASHBOARD"
            "<br><sup>Executive Overview | Data Analytics Report</sup>"
        ),
        x=0.5,
        y=0.98,
        xanchor="center",
        yanchor="top",
        font=dict(size=24)
    ),
    template="plotly_dark",
    height=1150,
    width=1600,
    showlegend=False,
    margin=dict(t=280, l=100, r=100, b=90),
    paper_bgcolor="#141414",
    plot_bgcolor="#1F1F1F"
)


fig.update_xaxes(showgrid=True, gridcolor="#333333")
fig.update_yaxes(showgrid=False)

# ======================================================
# KPI SUMMARY
# ======================================================

fig.add_annotation(
    x=0.16, y=1.18,
    xref="paper", yref="paper",
    text=f"<b>TOTAL TITLES</b><br>{total_titles:,}",
    showarrow=False,
    font=dict(size=19, color="white")
)

fig.add_annotation(
    x=0.40, y=1.18,
    xref="paper", yref="paper",
    text=f"<b>MOVIES</b><br>{movie_count:,}",
    showarrow=False,
    font=dict(size=19, color="#E50914")
)

fig.add_annotation(
    x=0.63, y=1.18,
    xref="paper", yref="paper",
    text=f"<b>TV SHOWS</b><br>{tv_count:,}",
    showarrow=False,
    font=dict(size=19, color="#A99BFF")
)

fig.add_annotation(
    x=0.86, y=1.18,
    xref="paper", yref="paper",
    text=f"<b>COUNTRIES</b><br>{total_countries}",
    showarrow=False,
    font=dict(size=19, color="#FFFFFF")
)

# ======================================================
# SAVE DASHBOARD
# ======================================================

output_file = os.path.join(
    dashboard_path,
    "05_Netflix_Executive_Dashboard.html"
)

fig.write_html(
    output_file,
    include_plotlyjs=True
)

print("=" * 65)
print("       NETFLIX EXECUTIVE DASHBOARD")
print("=" * 65)

print("\nDASHBOARD KPI SUMMARY")
print("-" * 65)

print("Total Titles:", total_titles)
print("Movies:", movie_count)
print("TV Shows:", tv_count)
print("Countries:", country_counts.size)

print("\nDASHBOARD COMPONENTS")
print("-" * 65)

print("1. Content Type Distribution")
print("2. Top 10 Countries")
print("3. Top 10 Genres")
print("4. Release Year Trend")

print("\nDashboard Generated Successfully!")
print("Saved Location:", output_file)

print("=" * 65)
