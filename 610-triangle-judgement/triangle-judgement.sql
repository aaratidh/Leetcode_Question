select  x , y , z , 
case 
   when  x + y > z  and z + x > y and y + z > x then 'Yes' 
   else 'No' 
   end  as triangle 

from triangle;



-- SELECT
--   x, y, z,
--   CASE
--     WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
--     ELSE 'No'
--   END AS triangle
-- FROM triangle;
