SELECT ProjectName
FROM Projects AS p
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    JOIN Employees AS e ON e.EmployeeID = ep.EmployeeID
    WHERE p.ProjectID = ep.ProjectID AND CONCAT(e.FirstName, ' ', e.LastName) = 'Bob Johnson' AND ep.HoursWorked > 150
);


UPDATE Projects AS p
SET Budget = Budget * 1.1
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    JOIN Employees AS e ON e.EmployeeID = ep.EmployeeID
    WHERE p.ProjectID = ep.ProjectID AND e.Department = 'IT'
);


SELECT * FROM Projects;


UPDATE Projects
SET EndDate = StartDate + Interval '1 year'
WHERE EndDate IS NULL;


SELECT * FROM Projects;


BEGIN;

WITH new_employee AS (
    INSERT INTO Employees
    (FirstName, LastName,  Department, Salary)
    VALUES
    ('Steven',  'Carter',  'IT',       60000.00)
    RETURNING id;
)

INSERT INTO EmployeeProjects
(EmployeeID, ProjectID,  HoursWorked)
SELECT id,   1,          80
FROM new_employee;

COMMIT;


SELECT * FROM Employees;


SELECT * FROM EmployeeProjects;