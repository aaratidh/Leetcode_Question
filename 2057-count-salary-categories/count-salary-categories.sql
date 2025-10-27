WITH t AS (
  SELECT 
    CASE WHEN income < 20000 THEN 'Low Salary' END       AS `Low Salary`,
    CASE WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary' END AS `Average Salary`,
    CASE WHEN income > 50000 THEN 'High Salary' END      AS `High Salary`
  FROM Accounts
)
SELECT 'High Salary' AS category,
       SUM(CASE WHEN `High Salary`    IS NOT NULL THEN 1 ELSE 0 END) AS accounts_count
FROM t
UNION ALL
SELECT 'Low Salary',
       SUM(CASE WHEN `Low Salary`     IS NOT NULL THEN 1 ELSE 0 END)
FROM t
UNION ALL
SELECT 'Average Salary',
       SUM(CASE WHEN `Average Salary` IS NOT NULL THEN 1 ELSE 0 END)
FROM t
ORDER BY FIELD(category, 'High Salary','Low Salary','Average Salary');
