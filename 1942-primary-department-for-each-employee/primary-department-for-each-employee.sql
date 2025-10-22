# Write your MySQL query statement below
with cte as (

select  employee_id, count(department_id)
from employee 
group by employee_id
having count(*) = 1

) 



select  employee_id  , department_id  
from  Employee  
where  primary_flag  = 'Y'

union 

select employee_id , department_id 
from employee
where employee_id  in (select employee_id from cte)
