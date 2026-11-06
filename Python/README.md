# Python Data Analysis

Beginner-level scripts documenting practical data analysis exercises.

## Automobile Data Cleaning and EDA

File: `automobile_data_cleaning_eda.py`

This script uses the Automobile dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/10/automobile). It:

- Loads the dataset and assigns readable column names.
- Converts the dataset's `?` missing-value markers to missing values.
- Converts numeric fields to numeric data types.
- Reports missing values instead of silently deleting every row.
- Summarizes vehicle makes and fuel types.
- Creates charts for vehicle makes, engine size versus price, and price distribution.

### Requirements

```bash
python -m pip install pandas matplotlib
```

### Run

From the repository root:

```bash
python Python/automobile_data_cleaning_eda.py
```

The script downloads the dataset from UCI when it runs and saves charts in `Python/outputs/`.

## Other scripts

- `sales_analysis.py` — synthetic sales analysis practice.
- `sales_summary.py` — reusable CSV summary example.

All work is presented as learning practice, not paid client work.
