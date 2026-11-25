-- Write your PostgreSQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from Activity
group by activity_date
having activity_date between '2019-07-27'::date -29 and '2019-07-27'::date
