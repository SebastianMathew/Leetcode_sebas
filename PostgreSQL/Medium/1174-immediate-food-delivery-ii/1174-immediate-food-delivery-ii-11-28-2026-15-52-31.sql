-- Write your PostgreSQL query statement below
select round(avg(case when od = cpdd then 100.00 else 0.00 end),2) as immediate_percentage
from (select customer_id, min(order_date) as od, min(customer_pref_delivery_date) as cpdd
from Delivery
group by customer_id)
