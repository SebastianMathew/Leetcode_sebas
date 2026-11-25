-- Write your PostgreSQL query statement below
select contest_id, round(((count(contest_id)::numeric/(select count(*) from users))*100),2) as percentage
from Users u left join Register r on u.user_id = r.user_id
group by contest_id
having contest_id is not null
order by percentage desc, contest_id asc