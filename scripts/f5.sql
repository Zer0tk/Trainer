CREATE FUNCTION CalculateAnnualBonus(EmployeeID INT, Salary DECIMAL)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN Salary * 0.1;
END;
$$;


SELECT FirstName, LastName, Salary, CalculateAnnualBonus(EmployeeID, Salary)
FROM Employees;


CREATE VIEW IT_Department_View AS
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'IT';


SELECT * FROM IT_Department_View;