# Write your MySQL query statement below
select t1.name as Employee
from employee as t1
join 
employee as t2
on t1.managerId = t2.id
where t1.salary > t2.salary