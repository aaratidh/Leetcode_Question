-- price as of 2019-08-16
(
  SELECT p1.product_id, p1.new_price AS price
  FROM Products p1
  WHERE p1.change_date = (
    SELECT MAX(p2.change_date)
    FROM Products p2
    WHERE p2.product_id = p1.product_id
      AND p2.change_date <= '2019-08-16'
  )
)
UNION ALL
(
  -- products with NO change on/before the date → default price 10
  SELECT p.product_id, 10 AS price
  FROM Products p
  GROUP BY p.product_id
  HAVING SUM(p.change_date <= '2019-08-16') = 0
);
