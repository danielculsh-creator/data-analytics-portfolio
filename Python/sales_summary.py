"""Summarise a business sales CSV supplied by the user."""
from pathlib import Path
import sys
import pandas as pd

METRICS = ["revenue", "cost", "profit", "quantity"]

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python Python/sales_summary.py path/to/sales.csv")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")
    data = pd.read_csv(path)
    data.columns = data.columns.str.strip().str.lower()
    print(f"Rows: {len(data):,}")
    print(f"Columns: {len(data.columns):,}")
    print("\nColumn types:")
    print(data.dtypes.to_string())
    print("\nMissing values:")
    print(data.isna().sum().to_string())
    available = [name for name in METRICS if name in data.columns]
    if available:
        for name in available:
            data[name] = pd.to_numeric(data[name], errors="coerce")
        print("\nNumeric summary:")
        print(data[available].describe().round(2).to_string())
    else:
        print("\nNo standard sales metrics found.")
        print("Available columns:", ", ".join(data.columns))

if __name__ == "__main__":
    main()
