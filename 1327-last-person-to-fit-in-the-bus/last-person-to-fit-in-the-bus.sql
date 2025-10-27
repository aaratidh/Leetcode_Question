# Write your MySQL query statement below
with cte as(
select  
q.turn  as Turn,  
q.person_id  As ID ,
q.person_name  as Name , 
q.weight  as Weight,
SUM(weight) OVER (ORDER BY q.turn) AS Total_Weight
from Queue q
),
cte2 as (
select *,
lead(Total_Weight) OVER (Order by Turn) As lead_weight
from cte
)

select  Name  as person_name 
from cte2 
where (lead_weight> 1000 or lead_weight is NULL ) and  Total_Weight <=1000 




