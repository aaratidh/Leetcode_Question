# Write your MySQL query statement below
-- select  s.user_id ,  coalesce(avg(c.action = 'confirmed'),0) as confirmation_rate 
-- from Signups  s 
-- left join Confirmations  c
-- on s.user_id  = c.user_id 
-- group by s.user_id
-- ORDER BY s.user_id;


SELECT
  s.user_id,
  round(COALESCE(AVG(c.action = 'confirmed'), 0),2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
  ON c.user_id = s.user_id
GROUP BY s.user_id
ORDER BY s.user_id;