# Write your MySQL query statement below
with cte as (
select
dense_rank() over (order by  salary desc) as  SecondHighestSalary, salary
from  Employee  
) 

SELECT  max(salary)  as SecondHighestSalary
FROM cte WHERE  SecondHighestSalary = 2 


-- Select * from cte   