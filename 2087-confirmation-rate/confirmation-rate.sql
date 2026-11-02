# Write your MySQL query statement below

SELECT 
s.user_id, IFNULL(t.a,0) as confirmation_rate 
FROM
Signups as s 
LEFT JOIN
(SELECT
user_id, ROUND(AVG(action="confirmed"),2) as a 
FROM
Confirmations
GROUP BY 
user_id) as t 
on t.user_id = s.user_id