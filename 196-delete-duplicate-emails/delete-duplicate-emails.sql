# Write your MySQL query statement below
with cte as (
select min(id)  from Person 
group by  email
having count(*) >= 1
)


Delete 
from 
Person
where id not in ( select * from cte)

