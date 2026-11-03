# Sales Performance Analysis — Synthetic Practice Project

## Business question
How do sales revenue and estimated profit vary across product categories, regions, and months?

## Dataset
This project uses datasets/sample_sales.csv, a small **synthetic** dataset created for learning. It does not describe a real company or real customers. Currency units are illustrative and are not assigned a currency symbol.

## Methods
- Validate required columns and parse dates.
- Convert quantity, unit price, and unit cost to numeric values.
- Calculate revenue as quantity multiplied by unit price.
- Calculate estimated profit as quantity multiplied by (unit price minus unit cost).
- Summarise orders, customers, category, region, and monthly performance.

## Run the Python analysis
From the repository root:
```bash
pip install -r requirements.txt
python Python/sales_analysis.py
```

To use another CSV with the same required columns:
```bash
python Python/sales_analysis.py path/to/your_file.csv
```

## SQL analysis
Import the CSV into a SQLite table named sample_sales, then run SQL/sample_sales_analysis.sql.

## Interpretation
Use the output to identify which categories, regions, and months contribute most to revenue. Profit is an estimate based only on the supplied unit cost; it excludes shipping, tax, discounts, overhead, and returns. Do not treat it as audited accounting profit.

## Limitations
The dataset has only 12 illustrative records. Results are demonstrations of analytical methods, not statistically reliable business conclusions.

## Example results from the included sample

Running the analysis on the included 12-row sample produces:
- Total revenue: 174,200 illustrative units
- Estimated profit: 73,900 illustrative units
- Highest-revenue category: Electronics (117,500)
- Highest-revenue region: West (54,300)
- Highest-revenue month: February 2026 (82,400)

These figures are calculated from the synthetic sample only. They should not be generalised to a real business.
