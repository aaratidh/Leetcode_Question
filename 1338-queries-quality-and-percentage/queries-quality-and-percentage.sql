Select q.query_name ,
Round((sum(q.rating/q.position))/count(q.query_name) ,2) as quality,
Round((select count(q1.query_name) from Queries q1 where rating <3 and q1.query_name = q.query_name)*100/count(q.query_name), 2) as poor_query_percentage
from Queries q
group by q.query_name 
