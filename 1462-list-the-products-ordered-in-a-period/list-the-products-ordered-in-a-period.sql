# Write your MySQL query statement below
with cte as (

select  product_id as product_id, sum(unit) as unit 
from Orders o 
where order_date >= '2020-02-01'  and order_date<= '2020-02-29'
group by product_id
Having sum(unit) >=100

)

select  p.product_name , c.unit
from Products p  
join cte c
on c.product_id = p.product_id 

