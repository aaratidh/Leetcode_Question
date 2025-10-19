-- # Write your MySQL query statement below
-- with userpercontest  as 
-- (
-- select contest_id , count(user_id) as usercnt
-- from register 
-- group by(contest_id)

-- ),

-- countuser as (
-- select count(user_id) as total_user_sum
-- from users
-- )

-- select upc.contest_id as contest_id, Round( upc.usercnt*100/(select total_user_sum from countuser), 2) as percentage 
-- from  userpercontest upc
-- order by Round( upc.usercnt*100/(select total_user_sum from countuser), 2) desc ,contest_id  asc




SELECT b.contest_id, ROUND((count(distinct(b.user_id))*100/count(distinct(a.user_id))), 2) as percentage
FROM Users as a, Register as b
GROUP BY b.contest_id
ORDER by percentage DESC, b.contest_id ASC