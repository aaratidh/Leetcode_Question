# Write your MySQL query statement below
-- select x , y , z,
-- case
--   when  x+y<=z, then 'Yes',
--   when  z+y<=x, then 'Yes' ,
--   when  z+x<=y, then 'Yes' ,
--   else 'NO'
-- end   as triangle 
-- from triangle


SELECT x, y, z,
       CASE
         WHEN x > 0 AND y > 0 AND z > 0
              AND x + y > z AND y + z > x AND x + z > y
           THEN 'Yes'
         ELSE 'No'
       END AS triangle
FROM Triangle;

