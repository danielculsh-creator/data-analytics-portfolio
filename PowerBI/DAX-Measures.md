# DAX Measures — Sales Performance Dashboard

These measures were found in the dashboard's embedded DAX query. They are listed here as a reference; confirm the table and column names in Power BI before reusing them.

```dax
Total Revenue = SUM(Sales_Data[Revenue])
Total Cost = SUM(Sales_Data[Cost])
Total Profit = SUM(Sales_Data[Profit])
Total Quantity = SUM(Sales_Data[Quantity])
Total Orders = DISTINCTCOUNT(Sales_Data[Order_ID])
Total Customers = DISTINCTCOUNT(Sales_Data[Customer_ID])
Profit Margin = DIVIDE([Total Profit], [Total Revenue], 0)

Total Products = DISTINCTCOUNT(Sales_Data[Product])
Total Categories = DISTINCTCOUNT(Sales_Data[Category])
Average Unit Price = AVERAGE(Sales_Data[Unit_Price])
Average Discount Rate = AVERAGE(Sales_Data[Discount_Rate])
Average Quantity per Order = DIVIDE([Total Quantity], [Total Orders], 0)
Total Customer Segments = DISTINCTCOUNT(Sales_Data[Customer_Segment])
Average Revenue per Customer = DIVIDE([Total Revenue], [Total Customers], 0)
Average Profit per Customer = DIVIDE([Total Profit], [Total Customers], 0)

Total Regions = DISTINCTCOUNT(Sales_Data[Region])
Total Cities = DISTINCTCOUNT(Sales_Data[City])
Average Revenue per Order = DIVIDE([Total Revenue], [Total Orders], 0)
Average Profit per Order = DIVIDE([Total Profit], [Total Orders], 0)

Total Years = DISTINCTCOUNT(Sales_Data[Year])
Total Months = DISTINCTCOUNT(Sales_Data[Month])
Total Quarters = DISTINCTCOUNT(Sales_Data[Quarter])
Revenue per Month = DIVIDE([Total Revenue], [Total Months], 0)
Profit per Month = DIVIDE([Total Profit], [Total Months], 0)
```

## Notes

- These measures are filter-sensitive: slicers, page filters, and visual filters can change their results.
- `Profit Margin` should be formatted as a percentage.
- The monthly averages above divide by the number of distinct month labels in the current filter context. If the report spans multiple years, consider using a distinct Year-Month key for monthly calculations.
- Validate whether the model's `Month` field is a month name, month number, or unique month-year value before interpreting `Total Months`.
- The DAX list is a documentation transcription, not an independent audit of the underlying dataset or business definitions.
