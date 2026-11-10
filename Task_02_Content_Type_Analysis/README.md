# Netflix Content Type Analysis Dashboard

## 1. Project Overview

This project focuses on analyzing the distribution of Movies and TV Shows available on Netflix using Python and data visualization techniques.

The objective is to understand the content distribution and generate meaningful business insights.

## 2. Project Objectives

- Analyze Netflix content types.
- Calculate total Movies and TV Shows.
- Compare content proportions.
- Create professional data visualizations.
- Generate meaningful business insights.

## 3. Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code

## 4. Dataset Information

- Dataset: Netflix Cleaned Dataset
- Total Records: 8,790
- Total Columns: 10
- Data Source: Task 1 – Netflix Data Cleaning & Preparation

## 5. Content Type Analysis

| Content Type | Count | Percentage |
|---|---:|---:|
| Movies | 6,126 | 69.69% |
| TV Shows | 2,664 | 30.31% |
| Total | 8,790 | 100% |

## 6. Data Visualizations

Two visualizations were created:

**1. Content Distribution Bar Chart**

Compares the total number of Movies and TV Shows.

**2. Content Proportion Pie Chart**

Displays the percentage distribution of Movies and TV Shows.

### Chart Locations

- `reports/charts/content_distribution.png`
- `reports/charts/content_proportion.png`

## 7. Key Business Insights

1. Movies account for 69.69% of the analyzed Netflix content.
2. TV Shows account for 30.31%.
3. Movies exceed TV Shows by 3,462 titles.
4. Movies dominate the analyzed Netflix content library.
5. The dataset shows a significantly higher proportion of Movies compared to TV Shows.

## 8. Project Structure

```text
Netflix_Data_Analytics/
│
├── data/
│   └── processed/
│       └── netflix_cleaned.csv
│
├── reports/
│   └── charts/
│       ├── content_distribution.png
│       └── content_proportion.png
│
├── Task_01_Submission/
│
└── Task_02_Content_Type_Analysis/
    │
    ├── task_02_analysis.py
    ├── README.md
    │
    ├── documentation/
    │   └── Task_02_Report.md
    │
    └── screenshots/
        ├── 01_dataset_analysis.png
        ├── 02_percentage_analysis.png
        ├── 03_bar_chart.png
        ├── 04_pie_chart.png
        └── 05_business_insights.png
```

## 9. How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install pandas matplotlib seaborn
```

### Step 2: Run the Python Script

Execute from the main project directory:

```bash
python Task_02_Content_Type_Analysis/task_02_analysis.py
```

### Step 3: View Results

The script displays:
- Dataset information
- Content type distribution
- Percentage calculations
- Business insights
- Bar chart
- Pie chart

Generated charts are saved in the `reports/charts/` directory.

## 10. Conclusion

The analysis demonstrates that Movies represent a larger share of Netflix's content library than TV Shows.

Using Python, Pandas, Matplotlib, and Seaborn, this project successfully analyzes and visualizes Netflix content distribution.

## 11. Internship Details

**Organization:** Auspify Technologies

**Internship:** Data Analysis Using Python

**Task:** Task 02 – Content Type Analysis Dashboard

**Status:** Completed

---

*Developed as part of the Netflix Data Analytics Internship learning journey.*