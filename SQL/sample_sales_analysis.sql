-- Run against a SQLite table named sample_sales.
-- Import datasets/sample_sales.csv into SQLite before running these queries.
-- Revenue and profit are calculated from quantity, unit_price, and unit cost.

-- Overall KPIs.
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(quantity * unit_price) AS total_revenue,
    SUM(quantity * (unit_price - cost)) AS estimated_profit
FROM sample_sales;

-- Revenue by product category.
SELECT
    category,
    SUM(quantity * unit_price) AS total_revenue
FROM sample_sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Revenue by region.
SELECT
    region,
    SUM(quantity * unit_price) AS total_revenue
FROM sample_sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Revenue by month (SQLite date function).
SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    SUM(quantity * unit_price) AS total_revenue
FROM sample_sales
GROUP BY strftime('%Y-%m', order_date)
ORDER BY sales_month;
