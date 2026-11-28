-- Write your PostgreSQL query statement below
select employee_id, department_id
from (select *, count(*) over (partition by employee_id) as cntt
        from Employee)
where primary_flag ='Y' or cntt = 1
