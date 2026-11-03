# Power BI — Sales Performance Dashboard

## Objective
Create an interactive report to understand revenue, cost, profit, orders, customers, products, regions, and trends over time.

## Dataset fields
Category, City, Cost, Customer ID, Customer Segment, Discount Rate, Month, Month Number, Month Year, Order Date, Order ID, Payment Method, Product, Profit, Profit Margin, Quantity, Quarter, Region, Revenue, Sales Channel, Unit Price.

## DAX measures
Total Revenue = SUM(Sales_Data[Revenue])
Total Cost = SUM(Sales_Data[Cost])
Total Profit = SUM(Sales_Data[Profit])
Total Quantity = SUM(Sales_Data[Quantity])
Total Order = DISTINCTCOUNT(Sales_Data[Order ID])
Total Customer = DISTINCTCOUNT(Sales_Data[Customer ID])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Check table and column names and data types against your model before using these measures.

## Suggested report pages
1. Executive Overview — KPIs and revenue/profit trends.
2. Sales Performance — category, channel, and payment method.
3. Customer and Product Analysis — segments, products, and order patterns.
4. Geographic and Time Analysis — region, city, and monthly trends.

Quality checks: verify the date-table relationship, sort Month by Month Number, format currency and percentages consistently, test slicers and page navigation, and reconcile totals with source data.

The actual PBIX report file is not included yet; this folder currently documents the project.
