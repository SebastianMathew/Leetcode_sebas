-- Write your PostgreSQL query statement below
delete
FROM Person p2
using Person p1 where p1.email = p2.email and p2.id>p1.id