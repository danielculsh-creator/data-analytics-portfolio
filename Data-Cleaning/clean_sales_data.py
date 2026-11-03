"""Clean basic text whitespace in a CSV and save a separate copy."""
from pathlib import Path
import sys
import pandas as pd

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python Data-Cleaning/clean_sales_data.py input.csv output.csv")
    source, destination = Path(sys.argv[1]), Path(sys.argv[2])
    if not source.is_file():
        raise SystemExit(f"Input file not found: {source}")
    frame = pd.read_csv(source)
    frame.columns = frame.columns.str.strip()
    for column in frame.select_dtypes(include="object").columns:
        frame[column] = frame[column].astype("string").str.strip()
    print(f"Rows: {len(frame):,}")
    print("Missing values by column:")
    print(frame.isna().sum().to_string())
    print(f"Duplicate rows identified: {frame.duplicated().sum():,}")
    print("No rows have been automatically deleted.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(destination, index=False)
    print(f"Saved cleaned copy to: {destination}")

if __name__ == "__main__":
    main()
