
import pandas as pd
import os

# Project Base Path
base_path = os.path.dirname(os.path.abspath(__file__))

# Dataset Path
dataset_path = os.path.join(
    base_path,
    "data",
    "processed",
    "netflix_cleaned.csv"
)

print("=" * 65)
print("       NETFLIX BUSINESS INSIGHTS REPORT")
print("=" * 65)

# Load Dataset
if os.path.exists(dataset_path):

    netflix_df = pd.read_csv(dataset_path)

    print("\n1. DATASET LOADED SUCCESSFULLY")
    print("-" * 65)

    print("Dataset Shape:", netflix_df.shape)

    print("\n2. DATASET COLUMNS")
    print("-" * 65)
    print(list(netflix_df.columns))

    print("\n3. FIRST FIVE RECORDS")
    print("-" * 65)
    print(netflix_df.head().to_string(index=False))

    print("\n4. DATASET INFORMATION")
    print("-" * 65)
    netflix_df.info()

    print("\n5. DATA TYPES")
    print("-" * 65)
    print(netflix_df.dtypes)

    print("\n6. DATASET SUMMARY")
    print("-" * 65)
    print(netflix_df.describe(include="all").to_string())

    print("\n7. DATA QUALITY CHECK")
    print("-" * 65)
    print("Missing Values:", netflix_df.isnull().sum().sum())
    print("Duplicate Records:", netflix_df.duplicated().sum())

    print("\n" + "=" * 65)
    print("       DATASET VALIDATION COMPLETED")
    print("=" * 65)

else:
    print("ERROR: Dataset file not found!")
    print("Expected Path:", dataset_path)
