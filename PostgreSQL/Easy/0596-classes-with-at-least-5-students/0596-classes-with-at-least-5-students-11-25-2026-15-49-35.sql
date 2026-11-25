-- Write your PostgreSQL query statement below
select class
from (select class, count(student)
from Courses
group by class)
where count>=5
