# Write your MySQL query statement below
SELECT EMployeeUNI.unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI 
ON Employees.id = EmployeeUNI.id;

