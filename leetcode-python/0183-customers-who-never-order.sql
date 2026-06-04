-- Write your MySQL query statement below
SELECT Customers.name AS "Customers" FROM Customers
WHERE Customers.id NOT IN
(SELECT Customers.id FROM Customers
INNER JOIN Orders ON Orders.customerId = Customers.id
GROUP BY Customers.name)