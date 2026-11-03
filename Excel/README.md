# Excel Sales Analysis

Suggested workflow:
1. Convert the source range into an Excel Table (Ctrl+T).
2. Check date formats, numeric values, blanks, and duplicate order IDs.
3. Investigate unusual values before changing them.
4. Build PivotTables for revenue by category, region, and month.
5. Add charts with clear titles, units, and date ranges.
6. Reconcile totals against the source data.

Example formulas, assuming an Excel Table named Sales:
- Total revenue: =SUM(Sales[Revenue])
- Average order value: =IFERROR(SUM(Sales[Revenue])/COUNTA(Sales[Order ID]),0)
- Blank customer IDs: =COUNTBLANK(Sales[Customer ID])

Formula separators can vary with regional settings.
