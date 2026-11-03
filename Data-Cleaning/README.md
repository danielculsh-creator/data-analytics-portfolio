# Data Cleaning Workflow

1. Profile row counts, columns, data types, and missing values.
2. Standardise column names and trim accidental spaces.
3. Validate dates, numeric ranges, categories, and identifiers.
4. Investigate duplicate records before removing anything.
5. Understand why values are missing; do not automatically replace them with zero.
6. Document each change and its reason.
7. Compare row counts and key totals before and after cleaning.

See clean_sales_data.py for a cautious starter script. It creates a cleaned copy and reports duplicates without silently deleting rows.
