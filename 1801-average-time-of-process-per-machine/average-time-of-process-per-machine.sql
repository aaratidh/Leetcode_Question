select a1.machine_id , round(avg( b1.timestamp  - a1.timestamp ),3) as  processing_time  
from Activity  a1 
join activity  b1
on b1.machine_id = a1.machine_id  and a1.process_id  = b1.process_id   and 
a1.activity_type  like  "start" and b1.activity_type like "end"
group by a1.machine_id 















































-- # Write your MySQL query statement below
-- select  m1.machine_id , round(avg(m1.timestamp - m2.timestamp),3)  as processing_time  
-- from activity m1 
-- join activity m2 
-- on m1.machine_id  = m2.machine_id  
-- where m1.activity_type = 'end'  
-- and m2.activity_type = 'start' 
-- and  m1.process_id = m2.process_id 
-- group by  m1.machine_id  


