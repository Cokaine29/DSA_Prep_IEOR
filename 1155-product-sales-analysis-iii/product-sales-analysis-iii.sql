# Write your MySQL query statement below

SELECT 
    s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
FROM
Sales as s
JOIN
(SELECT
    s.product_id,
    MIN(s.year) as first_year
FROM
Sales as s 
GROUP BY 
s.product_id) as t 
ON
s.product_id = t.product_id 
AND
s.year = t.first_year
