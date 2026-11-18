-- Write your PostgreSQL query statement below
select m.name
from Employee m join Employee e on m.id = e.managerid
group by m.name,m.id
having count(e.id)>=5
