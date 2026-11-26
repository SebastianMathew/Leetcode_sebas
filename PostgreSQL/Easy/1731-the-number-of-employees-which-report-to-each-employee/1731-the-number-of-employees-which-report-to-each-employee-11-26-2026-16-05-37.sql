-- Write your PostgreSQL query statement below
select m.employee_id , m.name, count(e.employee_id) as reports_count, round(avg(e.age),0) as average_age
from employees e left join employees m on e.reports_to = m.employee_id
group by m.employee_id,m.name
having m.employee_id is not null
order by m.employee_id 