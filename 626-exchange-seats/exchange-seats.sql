select
case when mod(id,2)=0 then id-1
     when mod(id,2)=1 and id+1 not in (select id from seat) then id
     else id+1 
end as id,
student
from seat order by id













-- # Write your MySQL query statement below
-- with cte as (
-- select  
-- id, 
-- student, 
-- lead(student) over (order by id )  as ledd,
-- lag(student) over (order by id) as lagg
-- from  seat 

-- )

-- select id, 
-- case 
--   when id = (select max(id) from Seat  ) and  id % 2 <> 0 then  student 
--   when id % 2 <> 0 then  ledd
--   when id % 2 = 0 then  lagg
-- end as student

-- from cte

