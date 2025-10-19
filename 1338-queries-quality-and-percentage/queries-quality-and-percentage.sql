-- Select q.query_name ,
-- Round((sum(q.rating/q.position))/count(q.query_name) ,2) as quality,
-- Round((select count(q1.query_name) from Queries q1 where rating <3 and q1.query_name = q.query_name)*100/count(q.query_name), 2) as poor_query_percentage
-- from Queries q
-- group by q.query_name 
SELECT query_name,ROUND(AVG(rating/position),2) AS quality,
ROUND(AVG(IF(rating < 3,1,0)) * 100,2) as poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name;