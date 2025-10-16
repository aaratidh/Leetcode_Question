 select  p.project_id ,  Round(sum(e.experience_years)/count(e.employee_id),2) as average_years 
 from Employee e 
 join Project p
 on E.employee_id=P.employee_id
 group by project_id  
