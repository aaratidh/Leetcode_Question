# Write your MySQL query statement below
select customer_id 
from Customer 
group by customer_id 
HAving count(distinct product_key ) = (select count(*) from product )