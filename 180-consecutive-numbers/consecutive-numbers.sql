# Write your MySQL query statement below
with cte as (
select  id  , num , 
lead(num) over(order by id)  as led,
lag(num)over (order by id ) as lg

from  Logs  
)



select distinct num as ConsecutiveNums 
from cte 
where num = lg and num = led and led= lg