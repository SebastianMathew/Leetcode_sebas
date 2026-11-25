-- Write your PostgreSQL query statement below
select teacher_id, count(subject_id) as cnt
from (select distinct teacher_id, subject_id
from teacher)
group by teacher_id
