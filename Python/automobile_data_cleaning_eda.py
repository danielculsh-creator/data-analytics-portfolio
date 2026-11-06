"""
Automobile Data Cleaning and Exploratory Data Analysis
Dataset: UCI Automobile (imports-85)
Purpose: Beginner practice in pandas, data cleaning, summary statistics and visualization.

Install dependencies:
    python -m pip install pandas matplotlib

Run:
    python Python/automobile_data_cleaning_eda.py

The script downloads the public dataset directly from UCI. It does not contain
personal customer information and does not overwrite the source dataset.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "autos/imports-85.data"
)

COLUMNS = [
    "symboling",
    "normalized_losses",
    "make",
    "fuel_type",
    "aspiration",
    "num_of_doors",
    "body_style",
    "drive_wheels",
    "engine_location",
    "wheel_base",
    "length",
    "width",
    "height",
    "curb_weight",
    "engine_type",
    "num_of_cylinders",
    "engine_size",
    "fuel_system",
    "bore",
    "stroke",
    "compression_ratio",
    "horsepower",
    "peak_rpm",
    "city_mpg",
    "highway_mpg",
    "price",
]

NUMERIC_COLUMNS = [
    "symboling",
    "normalized_losses",
    "wheel_base",
    "length",
    "width",
    "height",
    "curb_weight",
    "engine_size",
    "bore",
    "stroke",
    "compression_ratio",
    "horsepower",
    "peak_rpm",
    "city_mpg",
    "highway_mpg",
    "price",
]


def load_data() -> pd.DataFrame:
    """Load the UCI dataset and assign readable column names."""
    data = pd.read_csv(
        DATA_URL,
        header=None,
        names=COLUMNS,
        na_values="?",
    )

    # Convert numeric fields safely; invalid values become missing values.
    for column in NUMERIC_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    return data


def main() -> None:
    output_dir = Path("Python") / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data()

    print("\n--- Dataset overview ---")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(df.head())

    print("\n--- Missing values by column ---")
    print(df.isna().sum().sort_values(ascending=False))

    # Keep records with a known price for price-related analysis.
    # Other missing values remain visible and are not silently discarded.
    analysis_df = df.dropna(subset=["price"]).copy()

    print("\n--- Numeric summary ---")
    print(analysis_df.describe())

    print("\n--- Vehicle counts by make ---")
    print(analysis_df["make"].value_counts())

    print("\n--- Fuel type counts ---")
    print(analysis_df["fuel_type"].value_counts())

    # Chart 1: number of vehicles by make.
    make_counts = analysis_df["make"].value_counts().sort_values()
    plt.figure(figsize=(11, 7))
    make_counts.plot(kind="barh")
    plt.title("Number of Vehicles by Make")
    plt.xlabel("Number of vehicles")
    plt.ylabel("Vehicle make")
    plt.tight_layout()
    plt.savefig(output_dir / "vehicles_by_make.png", dpi=150)
    plt.show()

    # Chart 2: engine size versus price.
    engine_price = analysis_df.dropna(subset=["engine_size", "price"])
    plt.figure(figsize=(9, 6))
    plt.scatter(engine_price["engine_size"], engine_price["price"], alpha=0.7)
    plt.title("Engine Size vs Vehicle Price")
    plt.xlabel("Engine size")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(output_dir / "engine_size_vs_price.png", dpi=150)
    plt.show()

    # Chart 3: distribution of vehicle prices.
    plt.figure(figsize=(9, 6))
    analysis_df["price"].dropna().plot(kind="hist", bins=20, edgecolor="black")
    plt.title("Distribution of Vehicle Prices")
    plt.xlabel("Price")
    plt.ylabel("Number of vehicles")
    plt.tight_layout()
    plt.savefig(output_dir / "vehicle_price_distribution.png", dpi=150)
    plt.show()

    print(f"\nCharts saved in: {output_dir.resolve()}")
    print(
        "\nNote: Missing values were reported rather than removing every row. "
        "Only rows without a price were excluded from price-based analysis."
    )


if __name__ == "__main__":
    main()
