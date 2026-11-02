# Write your MySQL query statement below

SELECT 
r.contest_id, ROUND((COUNT(DISTINCT r.user_id) / (SELECT COUNT(user_id) FROM Users)) * 100, 2) as percentage 
FROM 
Register as r 
GROUP BY 
r.contest_id
ORDER BY
percentage DESC, r.contest_id ASC