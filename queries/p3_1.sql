SELECT coutry, COUNT(customer_id) AS count
FROM Customers
GROUP BY coutry;