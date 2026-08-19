# Часть 1: WHERE #

### Задача 1 ###
Найдите всех клиентов из страны 'USA', которым больше 25 лет.

#### Запрос ####
```sql
SELECT first_name, last_name, age, coutry
FROM Customers
WHERE coutry = 'USA' AND age > 25;
```

#### Скриншот ####
![image](/images/p1_1.png)


### Задача 2 ###
Выведите все заказы, у которых сумма (amount) больше 1000.

#### Запрос ####
```sql
SELECT * FROM Orders
WHERE amount > 1000;
```

#### Скриншот ####
![image](/images/p1_2.png)


# Часть 2: JOIN #

### Задача 1 ###
Получите список заказов вместе с именем клиента, который сделал заказ.

#### Запрос ####
```sql
SELECT c.first_name, c.last_name, o.item, o.amount
FROM Orders AS o
JOIN Customers AS c ON c.customer_id = o.customer_id;
```

#### Скриншот ####
![image](/images/p2_1.png)


### Задача 2 ###
Выведите список доставок со статусом и именем клиента. 

#### Запрос ####
```sql
SELECT s.status, c.first_name, c.last_name
FROM Customers AS c
JOIN Shippings AS s ON c.customer_id = s.customer;
```

#### Скриншот ####
![image](/images/p2_2.png)


# Часть 3: GROUP BY #

### Задача 1 ###
Подсчитайте количество клиентов в каждой стране.

#### Запрос ####
```sql
SELECT coutry, COUNT(customer_id) AS count
FROM Customers
GROUP BY coutry;
```

#### Скриншот ####
![image](/images/p3_1.png)


### Задача 2 ###
Посчитайте общее количество заказов и среднюю сумму по каждому товару.

#### Запрос ####
```sql
SELECT item, COUNT(*), ROUND(AVG(amount), 2)
FROM Orders
GROUP BY item;
```

#### Скриншот ####
![image](/images/p3_2.png)


# Часть 4: ORDER BY #
Выведите список клиентов, отсортированный по возрасту по убыванию.

#### Запрос ####
```sql
SELECT first_name, age
FROM Customers
ORDER BY age DESC;
```

#### Скриншот ####
![image](/images/p4.png)


# Часть 5: SUBQUERIES #
Найдите всех клиентов, которые сделали заказ с максимальной суммой.

#### Запрос ####
```sql
SELECT c.first_name, c.last_name, o.amount
FROM Customers as c
JOIN Orders AS o ON o.customer_id = c.customer_id
WHERE o.amount = (
    SELECT MAX(amount)
    FROM Orders
);
```

#### Пояснение ####
Поскольку нам нужно значение *максимальной суммы*, то найдем его через подзапрос (subquery) из таблицы Orders при помощи функции *MAX*.

#### Скриншот ####
![image](/images/p5.png)


# Часть 6: WINDOW FUNCTIONS #
Для каждого заказа добавьте колонку с суммой всех заказов этого клиента (используя 
оконную функцию).

#### Запрос ####
```sql
SELECT order_id, customer_id, item, amount,
SUM(amount) OVER ( PARTITION BY customer_id ) AS total_by_customer
FROM Orders;
```

#### Пояснение ####
Поскольку нам нужна колонка _с суммой всех заказов_ клиента, то добавим отдельную window function, которая найдет сумму _amount_ (через соответствующую функцию *SUM*) по каждому отдельному *customer_id*.

#### Скриншот ####
![image](/images/p6.png)


# Часть 7 #
Найдите клиентов, которые: 
1. Сделали хотя бы 2 заказа (любых), 
2. Имеют хотя бы одну доставку со статусом 'Delivered'.

Для каждого такого клиента выведите: 
* full_name (имя + фамилия), 
* общее количество заказов, 
* общую сумму заказов, 
* страну проживания. 

#### Запрос ####
```sql
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
```

#### Пояснения ####
1\. Условия

Поскольку у нас есть условие по полю, полученному через aggregate function (`total_orders`), к которому мы не можем обратиться обычным способом (такое поле отсутствует в таблице, взятой из FROM), то обернем полученную через SELECT таблицу как subquery, которую возьмем через FROM (теперь у нас есть доступ к этому полю).

Для второго условия нам потребуется взять отдельную таблицу из Shippings и проверить вхождение данных из исходного subquery через *EXISTS*.

2\. Поле `full_name` получим при помощи склеивания строк (concatenate) *first_name* и *last_name* (между ними дополнительно добавим строку с пробелом) через соответствующую функцию *CONCAT*, принимающую в качестве аргументов эти строки.

3\. Поскольку в результате получаем дублирование строк, то исключим повторения из основного запроса через *DISTINCT*.

#### Скриншот ####
![image](/images/p7.png)