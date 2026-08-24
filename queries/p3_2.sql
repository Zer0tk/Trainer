SELECT item, COUNT(*), ROUND(AVG(amount), 2)
FROM Orders
GROUP BY item;