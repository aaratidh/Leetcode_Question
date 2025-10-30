-- # Write your MySQL query statement below
with cte as (

select accepter_id as id , coalesce(count(* ) , 0) as num
 from  RequestAccepted  
 group by accepter_id  

),

cte2 as (

select requester_id   as id,  COALESCE(count(*), 0 )  as num
from   RequestAccepted 
group by requester_id 

)


select  id as id, SUM(num) as num from  (
select  *  from cte
Union all 
select * from cte2 
) T1
group by id 
ORDER BY  NUM  desc
LIMIT 1








-- select  a. id as id  , a.sum1 + b.sum2 as num 
-- from cte a  
-- cross join  cte2 b 
-- on   a.id = b.id 
-- group by a.id
-- order by   a.sum1 + b.sum2 desc
-- limit 1 