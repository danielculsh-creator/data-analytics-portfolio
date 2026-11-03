-- Generic practice table: sales
-- Expected columns: order_id, customer_id, product, category, region,
-- order_date, quantity, unit_price, revenue

-- Preview records (PostgreSQL, SQLite, and MySQL support LIMIT).
SELECT * FROM sales LIMIT 10;

-- Overall performance.
SELECT COUNT(DISTINCT order_id) AS total_orders,
       COUNT(DISTINCT customer_id) AS total_customers,
       SUM(revenue) AS total_revenue
FROM sales;

-- Revenue by category.
SELECT category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Revenue by region.
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Monthly revenue (PostgreSQL syntax).
SELECT DATE_TRUNC('month', order_date) AS sales_month,
       SUM(revenue) AS total_revenue
FROM sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;

-- Top customers.
SELECT customer_id, SUM(revenue) AS customer_revenue
FROM sales
GROUP BY customer_id
ORDER BY customer_revenue DESC
LIMIT 10;
