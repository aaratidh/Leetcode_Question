SELECT
  p1.product_id,
  COALESCE(
    MAX(CASE
          WHEN p1.change_date = (
            SELECT MAX(p2.change_date)
            FROM Products p2
            WHERE p2.product_id = p1.product_id
              AND p2.change_date <= '2019-08-16'
          )
          THEN p1.new_price
        END),
    10
  ) AS price
FROM Products p1
GROUP BY p1.product_id;



