INSERT INTO Employees
(FirstName, LastName,  Department, Salary)
VALUES
('Howard',   'Swift',  'HR',       58000.00),
('Dalton',   'Rhodes', 'Finance',  57000.00);


SELECT * FROM Employees;


SELECT FirstName, LastName
FROM Employees
WHERE Department = 'IT';


UPDATE Employees
SET Salary = 65000.00
WHERE CONCAT(FirstName, ' ', LastName) = 'Alice Smith';


DELETE FROM Employees
WHERE CONCAT(FirstName, ' ', LastName) = 'Eve Davis';


SELECT * FROM Employees;