-- Write your PostgreSQL query statement below
with nr as (
    select id, num,
    lead(id,1) over (order by id) as ni1,
    lead(id,2) over (order by id) as ni2,
    lead(num,1) over (order by id) as nn1,
    lead(num,2) over (order by id) as nn2
    from logs
)
select distinct num as consecutivenums
from nr
where ni1-id = 1 and ni2-ni1 = 1 and num = nn1 and nn1 = nn2