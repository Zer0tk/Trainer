SELECT DISTINCT full_name, coutry, total_orders, total_amount
FROM (
    SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name, c.coutry,
    COUNT(o.order_id) OVER ( PARTITION BY c.customer_id ) AS total_orders,
    SUM(o.amount) OVER ( PARTITION BY c.customer_id ) AS total_amount
    FROM Customers AS c
    JOIN Orders AS o ON o.customer_id = c.customer_id
    WHERE EXISTS (
        SELECT 1
        FROM Shippings as s
        WHERE s.customer = c.customer_id AND s.status = 'Delivered'
    )
)
WHERE total_orders = 2;