# Write your MySQL query statement below
SELECT s.student_id,
s.student_name,
sub.subject_name,
COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;





















-- select s.student_id as  student_id , s.student_name as student_name, sb.subject_name  as subject_name,
-- count(*) as attended_exams 
-- from Students  s 
-- left  join  Examinations e 
-- on e.student_id  =  s.student_id 
-- join  Subjects sb 
-- on sb.subject_name  = e.subject_name
-- group by  1 , 2, 3
-- order by  student_id , student_name 
