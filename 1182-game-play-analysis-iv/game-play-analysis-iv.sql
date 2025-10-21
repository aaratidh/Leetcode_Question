# Write your MySQL query statement below
with cte2 as (
select  player_id,min( event_date) as firstlog 
from Activity 
group by (player_id)

)

Select  Round(count(*)/(select count(distinct player_id) from Activity ),2) as  fraction  
from activity a2
join cte2 a1
on a1.firstlog  + INTERVAL 1 DAY = a2.event_date  and a1.player_id  = a2.player_id 
