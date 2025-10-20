# Write your MySQL query statement below
with cte1 as
(
select min(order_date ) as first_ord, customer_id 
from Delivery 
group by customer_id
),
cte2 as (
 SELECT d.customer_id
  FROM Delivery d
  JOIN cte1 c
    ON d.customer_id = c.customer_id
   AND d.order_date  = c.first_ord
   AND d.order_date  = d.customer_pref_delivery_date
)

select Round( 100 * count(*)/(select count(*) from cte1) ,2) as immediate_percentage 
from cte2