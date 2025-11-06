select  w2.id 
from Weather w1 
join Weather w2 
on w1.recordDate + INTERVAL  '1' day = w2.recordDate 
and w1.temperature < w2.temperature 

