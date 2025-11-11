with t1 as (
select  distinct  product_id as product_id ,  max(change_date) as change_date
from products  
where  change_date <= '2019-08-16'
group by product_id 
)

select  p.product_id  as product_id , p.new_price  as price 
from products  p 
join t1 
on t1.product_id = p.product_id and t1.change_date = p.change_date

union 

select  product_id , 10 as price 
from products 
where  product_id not in (  select product_id from t1)
order by product_id
