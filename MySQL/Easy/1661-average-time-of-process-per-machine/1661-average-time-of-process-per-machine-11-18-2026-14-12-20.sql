# Write your MySQL query statement below
select ast.machine_id, round(avg(aen.timestamp-ast.timestamp), 3) as processing_time
from Activity ast join Activity aen on ast.machine_id = aen.machine_id and ast.process_id = aen.process_id and ast.activity_type = 'start' and aen.activity_type = 'end'
group by ast.machine_id