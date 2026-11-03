"""Analyse the repository's sample sales CSV.

Usage:
    python Python/sales_analysis.py
    python Python/sales_analysis.py datasets/sample_sales.csv

All currency values are in the dataset's illustrative units; the sample is
synthetic and does not represent a real business.
"""
from pathlib import Path
import sys
import pandas as pd

REQUIRED = {"order_id", "order_date", "customer_id", "region",
            "category", "product", "quantity", "unit_price", "cost"}

def main():
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("datasets/sample_sales.csv")
    if not csv_path.exists():
        raise SystemExit(f"Dataset not found: {csv_path}")

    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SystemExit("Missing required columns: " + ", ".join(sorted(missing)))

    for column in ["quantity", "unit_price", "cost"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_id", "order_date", "quantity", "unit_price", "cost"]).copy()
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["profit"] = df["revenue"] - df["quantity"] * df["cost"]

    print("\nSALES PERFORMANCE SUMMARY")
    print(f"Valid rows: {len(df):,}")
    print(f"Orders: {df['order_id'].nunique():,}")
    print(f"Customers: {df['customer_id'].nunique():,}")
    print(f"Revenue: {df['revenue'].sum():,.2f}")
    print(f"Estimated profit: {df['profit'].sum():,.2f}")

    print("\nREVENUE BY CATEGORY")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).to_string())

    print("\nREVENUE BY REGION")
    print(df.groupby("region")["revenue"].sum().sort_values(ascending=False).to_string())

    monthly = df.assign(month=df["order_date"].dt.to_period("M"))
    print("\nREVENUE BY MONTH")
    print(monthly.groupby("month")["revenue"].sum().to_string())

if __name__ == "__main__":
    main()
