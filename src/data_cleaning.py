# ============================================================
# PROJECT: NETFLIX DATA ANALYTICS
# TASK 1: DATA CLEANING & PREPARATION
# MODULE: DATA QUALITY INSPECTION
# ============================================================

import pandas as pd
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "raw" / "Dataset.csv"

# Load dataset
netflix_data = pd.read_csv(DATA_PATH)

print("=" * 60)
print("       NETFLIX DATA ANALYTICS PROJECT")
print("       INITIAL DATA QUALITY INSPECTION")
print("=" * 60)

# Dataset dimensions
print("\n1. DATASET DIMENSIONS")
print("-" * 40)

print("Total Records:", netflix_data.shape[0])
print("Total Columns:", netflix_data.shape[1])

# Column information
print("\n2. COLUMN INFORMATION")
print("-" * 40)

print(netflix_data.info())

# Missing values
print("\n3. MISSING VALUE ANALYSIS")
print("-" * 40)

print(netflix_data.isnull().sum())

# Duplicate records
print("\n4. DUPLICATE RECORD ANALYSIS")
print("-" * 40)

print("Duplicate Records:", netflix_data.duplicated().sum())

# Data types
print("\n5. DATA TYPES")
print("-" * 40)

print(netflix_data.dtypes)

# Unique values
print("\n6. UNIQUE VALUE ANALYSIS")
print("-" * 40)

for column in netflix_data.columns:
    print(f"{column}: {netflix_data[column].nunique()}")

print("\n" + "=" * 60)
print("INITIAL DATA INSPECTION COMPLETED SUCCESSFULLY!")
print("=" * 60)
# ============================================================
# STEP 2: DATA FORMATTING & CONSISTENCY ANALYSIS
# ============================================================

print("\n7. TEXT FORMATTING ANALYSIS")
print("-" * 50)

text_columns = netflix_data.select_dtypes(
    include=["object"]
).columns

for column in text_columns:

    total_spaces = (
        netflix_data[column]
        .dropna()
        .astype(str)
        .ne(
            netflix_data[column]
            .dropna()
            .astype(str)
            .str.strip()
        )
        .sum()
    )

    print(f"{column}: {total_spaces} records with extra spaces")

print("\n8. CATEGORICAL VALUE ANALYSIS")
print("-" * 50)

categorical_columns = [
    "type",
    "rating",
    "country"
]

for column in categorical_columns:

    if column in netflix_data.columns:

        print(f"\n{column.upper()}")

        print(
            netflix_data[column]
            .value_counts(dropna=False)
            .head(15)
        )

print("\n9. DATE FORMAT VALIDATION")
print("-" * 50)

if "date_added" in netflix_data.columns:

    date_values = pd.to_datetime(
        netflix_data["date_added"],
        errors="coerce"
    )

    print("Valid Dates:", date_values.notna().sum())
    print("Invalid or Missing Dates:", date_values.isna().sum())

print("\nFORMATTING ANALYSIS COMPLETED!")
# ============================================================
# STEP 3: DATA STANDARDIZATION
# ============================================================

print("\n10. DATA STANDARDIZATION")
print("-" * 50)

# Create a separate copy for cleaning
cleaned_data = netflix_data.copy()

# Standardize text columns
text_columns = cleaned_data.select_dtypes(
    include=["object"]
).columns

for column in text_columns:

    cleaned_data[column] = (
        cleaned_data[column]
        .str.strip()
        .replace("", pd.NA)
    )

# Standardize multiple spaces
for column in text_columns:

    cleaned_data[column] = cleaned_data[column].str.replace(
        r"\s+",
        " ",
        regex=True
    )

# Standardize content type
if "type" in cleaned_data.columns:

    cleaned_data["type"] = cleaned_data["type"].replace({
        "movie": "Movie",
        "tv show": "TV Show"
    })

# Standardize country formatting
if "country" in cleaned_data.columns:

    cleaned_data["country"] = cleaned_data["country"].str.replace(
        r"\s*,\s*",
        ", ",
        regex=True
    )

# Display standardized values
print("\nStandardized Content Types:")

if "type" in cleaned_data.columns:
    print(cleaned_data["type"].value_counts(dropna=False))

print("\nStandardization completed successfully!")
# ============================================================
# STEP 4: EXPORT CLEANED DATASET
# ============================================================

OUTPUT_PATH = (
    BASE_DIR / "data" / "processed" / "netflix_cleaned.csv"
)

cleaned_data.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nCLEANED DATASET EXPORTED SUCCESSFULLY!")

print("Output Location:", OUTPUT_PATH)

print("Final Dataset Shape:", cleaned_data.shape)
# ============================================================
# STEP 5: FINAL DATA QUALITY VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("       FINAL DATA QUALITY VALIDATION")
print("=" * 60)

# 1. Dataset Shape Comparison

print("\n1. DATASET SHAPE COMPARISON")
print("-" * 40)

print("Original Dataset:", netflix_data.shape)
print("Cleaned Dataset:", cleaned_data.shape)

# 2. Missing Values

print("\n2. MISSING VALUE CHECK")
print("-" * 40)

print(cleaned_data.isnull().sum())

# 3. Duplicate Records

print("\n3. DUPLICATE RECORD CHECK")
print("-" * 40)

print(
    "Duplicate Records:",
    cleaned_data.duplicated().sum()
)

# 4. Data Type Validation

print("\n4. DATA TYPE VALIDATION")
print("-" * 40)

print(cleaned_data.dtypes)

# 5. Content Type Validation

print("\n5. CONTENT TYPE VALIDATION")
print("-" * 40)

if "type" in cleaned_data.columns:
    print(cleaned_data["type"].value_counts(dropna=False))

# 6. Final Quality Summary

print("\n6. FINAL QUALITY SUMMARY")
print("-" * 40)

print("Total Records:", len(cleaned_data))
print("Total Columns:", len(cleaned_data.columns))

print(
    "Total Missing Values:",
    cleaned_data.isnull().sum().sum()
)

print(
    "Total Duplicate Records:",
    cleaned_data.duplicated().sum()
)

print("\nDATA QUALITY VALIDATION COMPLETED!")