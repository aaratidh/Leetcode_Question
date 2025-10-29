Select results from
(
Select   mr.user_id ,  u.name  as results
from users  u 
join movierating mr 
on  mr.user_id = u.user_id 
group by  mr.user_id ,   u .name
order by Count(*) desc , u.name 
limit 1 
) t2


Union all 

SELECT results from  
(
Select avg(mr.rating), m.title as results ,  mr.movie_id 
from  Movies m 
join Movierating mr 
on m.movie_id  = mr.movie_id    
WHERE mr.created_at >= '2020-02-01'
AND mr.created_at <  '2020-03-01'
group by mr.movie_id  , m.title
order by avg(mr.rating) desc ,  m.title 
limit 1
) t1















