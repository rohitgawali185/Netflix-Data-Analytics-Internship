# Netflix Content Rating & Genre Analysis

## Project Overview
This project focuses on analyzing Netflix content ratings and genres using Python. The objective is to understand content distribution, identify popular genres, compare ratings across Movies and TV Shows, and generate meaningful audience insights.

## Internship Details
- **Organization:** Auspify Technologies
- **Program:** Data Analysis Using Python Internship
- **Task:** Task 5 – Content Rating & Genre Analysis
- **Difficulty:** Advanced

## Objectives
- Analyze Netflix content rating categories.
- Identify the most common genres.
- Compare ratings across Movies and TV Shows.
- Create interactive visualizations.
- Generate business and audience insights.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- VS Code

## Dataset Information
- Dataset: Netflix Movies and TV Shows
- Records: 8,790
- Columns: 10
- Data Source: Previously cleaned Netflix dataset.

## Project Structure
```text
Task_05_Content_Rating_Genre_Analysis/
│
├── content_rating_genre_analysis.py
├── output/
│   ├── rating_distribution.csv
│   ├── genre_distribution.csv
│   └── rating_by_content_type.csv
│
├── visualizations/
│   ├── 01_rating_distribution.html
│   ├── 02_top_10_genres.html
│   ├── 03_rating_comparison.html
│   └── 04_content_type_distribution.html
│
├── documentation/
│   └── Business_Insights_Report.txt
│
├── screenshots/
│
└── README.md
```

## Analysis Performed

### 1. Content Rating Analysis
Analyzed the distribution of Netflix content ratings and identified the most common rating categories.

### 2. Genre Analysis
Identified the most common genres by separating multiple genres listed for individual titles.

### 3. Rating Comparison
Compared rating distributions between Movies and TV Shows using Pandas Crosstab.

### 4. Interactive Visualizations
Created four interactive charts using Plotly:
- Content Rating Distribution
- Top 10 Most Common Genres
- Rating Comparison Across Content Types
- Movies vs TV Shows Distribution

### 5. Business Insights
Generated a report containing dataset statistics, rating insights, genre insights, content type distribution, and audience suitability observations.

## How to Run the Project

1. Install Python.
2. Install required libraries:

```bash
pip install pandas plotly
```

3. Ensure the cleaned dataset exists at:

```text
data/processed/netflix_cleaned.csv
```

4. Run the Python script:

```bash
python content_rating_genre_analysis.py
```

5. Open the generated HTML visualization files in Google Chrome.

## Key Findings
- Total Netflix records analyzed: 8,790.
- Total rating categories identified: 14.
- TV-MA is the most common content rating.
- TV-14 is the second most common content rating.
- Genre distribution helps identify major Netflix content categories.
- Rating comparison provides insights into Movies and TV Shows.

## Project Deliverables
- Python source code
- Rating analysis CSV
- Genre analysis CSV
- Rating comparison CSV
- Four interactive HTML charts
- Business Insights Report
- Project screenshots
- README documentation

## Conclusion
This project demonstrates practical data analysis skills using Python, Pandas, and Plotly. It explores Netflix content ratings, genres, and content type patterns through structured analysis and interactive visualizations.

**Project completed as part of the Auspify Technologies Data Analysis Using Python Internship.**