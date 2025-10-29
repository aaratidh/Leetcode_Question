with Daysum as (
select sum(amount) as amount ,
visited_on as visited_on
from  Customer  
group by  visited_on    

 )


select 
a.visited_on,
round(sum(b.amount),2) as amount, 
round(avg(b.amount),2) as  average_amount  
from  Daysum a 
join  Daysum b 
ON DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on
HAVING COUNT(*) = 7   -- ensures full 7-day window
ORDER BY a.visited_on;
