# Write your MySQL query statement below
with  t1 as (
select departmentId , name , salary ,
dense_rank() over (partition by departmentId order by salary desc ) as rank1 
from  Employee   
) 


-- select * from t1


select  d.name  as Department, t1.name as Employee ,  t1.salary as  Salary
from  t1 
join Department  d 
on d.id  = t1.departmentId
where t1.rank1 <= 3
order by  t1.rank1  , t1.name asc
