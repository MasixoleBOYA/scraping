WITH CurrentMonth AS (
    SELECT
        transporter,
        DATE_TRUNC('month', date) AS month,
        date,
        wasted_per_transporter,
        SUM(wasted_per_transporter) OVER (PARTITION BY transporter, DATE_TRUNC('month', date) ORDER BY date) AS mtd_waste
    FROM your_table
    WHERE date <= '2024-08-03' -- Replace this date with your date of interest
),
PreviousMonth AS (
    SELECT
        transporter,
        DATE_TRUNC('month', DATEADD('month', -1, date)) AS month,
        date,
        wasted_per_transporter,
        SUM(wasted_per_transporter) OVER (PARTITION BY transporter, DATE_TRUNC('month', DATEADD('month', -1, date)) ORDER BY date) AS mtd_waste
    FROM your_table
    WHERE date <= DATEADD('month', -1, '2024-08-03') -- Adjust to the previous month and same day
)

SELECT 
    c.transporter,
    c.month AS current_month,
    c.date AS current_date,
    c.mtd_waste AS mtd_waste_current,
    p.month AS previous_month,
    p.date AS previous_date,
    p.mtd_waste AS mtd_waste_previous
FROM 
    CurrentMonth c
LEFT JOIN 
    PreviousMonth p ON c.transporter = p.transporter 
                   AND DAY(c.date) = DAY(p.date) -- Ensures we compare the same day of the month
ORDER BY 
    c.transporter, c.date;


Explanation of the Query
CurrentMonth CTE:

Retrieves the month-to-date waste (mtd_waste) for each transporter up to the specified date in the current month.
Filters data to the date of interest ('2024-08-03' in this case) to avoid counting future values.
PreviousMonth CTE:

Retrieves month-to-date waste values for each transporter, but for the same day in the previous month.
Filters data up to the same day in the previous month (DATEADD('month', -1, '2024-08-03')).
Main Query:

Joins the two CTEs based on the transporter and day of the month, so it lines up the current and previous month values by transporter and date.
Orders by transporter and date for easy comparison.
This will yield a result with the cumulative month-to-date waste for each transporter, along with the equivalent values for the previous month up to the same day.



WITH CurrentMonth AS (
    SELECT
        transporter,
        DATE_FORMAT(date, '%Y-%m-01') AS month,
        date,
        wasted_per_transporter,
        SUM(wasted_per_transporter) OVER (PARTITION BY transporter, DATE_FORMAT(date, '%Y-%m') ORDER BY date) AS mtd_waste
    FROM your_table
    WHERE date <= '2024-08-03' -- Replace this with your date of interest
),
PreviousMonth AS (
    SELECT
        transporter,
        DATE_FORMAT(DATE_SUB(date, INTERVAL 1 MONTH), '%Y-%m-01') AS month,
        date,
        wasted_per_transporter,
        SUM(wasted_per_transporter) OVER (PARTITION BY transporter, DATE_FORMAT(DATE_SUB(date, INTERVAL 1 MONTH), '%Y-%m') ORDER BY date) AS mtd_waste
    FROM your_table
    WHERE date <= DATE_SUB('2024-08-03', INTERVAL 1 MONTH) -- Adjust to the same day in the previous month
)

SELECT 
    c.transporter,
    c.month AS current_month,
    c.date AS current_date,
    c.mtd_waste AS mtd_waste_current,
    p.month AS previous_month,
    p.date AS previous_date,
    p.mtd_waste AS mtd_waste_previous
FROM 
    CurrentMonth c
LEFT JOIN 
    PreviousMonth p ON c.transporter = p.transporter 
                   AND DAY(c.date) = DAY(p.date) -- Match same day of the month
ORDER BY 
    c.transporter, c.date;

Explanation of Changes for MySQL
DATE_FORMAT: MySQL doesn’t have a DATE_TRUNC function like PostgreSQL, so DATE_FORMAT(date, '%Y-%m-01') is used to get the first day of the month.

DATE_SUB: MySQL uses DATE_SUB instead of DATEADD to subtract intervals (e.g., INTERVAL 1 MONTH).

Window Functions: MySQL 8.0+ supports window functions, so the cumulative sum with SUM(...) OVER (...) works as in other SQL dialects.

This query will now work with MySQL, providing month-to-date totals for each transporter alongside the same metrics for the same day in the previous month.
