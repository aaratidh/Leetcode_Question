# Write your MySQL query statement below
select p.product_id ,
IFNULL(round((sum(u.units* p.price ))/sum(u.units) ,2),0)  as average_price
from prices p 
left join UnitsSold u 
on u.product_id = p.product_id and  u.purchase_date >= p.start_date and u.purchase_date <= p.end_date
group by p.product_id  
  