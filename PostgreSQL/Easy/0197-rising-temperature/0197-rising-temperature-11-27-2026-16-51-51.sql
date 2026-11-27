-- Write your PostgreSQL query statement below
select w2.id
from Weather w1 join Weather w2 on w2.recorddate - 1 = w1.recorddate
where w2.temperature>w1.temperature