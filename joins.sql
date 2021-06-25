select distinct customerName, creditLimit from orders t1 join customers t2 on t1.customerNumber = t2.customerNumber where state in ('CA') and t1.status not in ('shipped') and creditLimit > 10000 order by creditLimit Desc;


SELECT *
FROM customers
INNER JOIN orders
ON customers.customerNumber = orders.customerNumber;

