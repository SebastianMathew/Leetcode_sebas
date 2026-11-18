-- Write your PostgreSQL query statement below
with dhs as (
    select d.name as department,
    e.name as employee,
    e.salary as salary,
    rank() over (partition by d.name order by e.salary desc) as rnk
    from employee e join department d on e.departmentid = d.id
)
select department,employee,salary
from dhs where rnk = 1