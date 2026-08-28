UPDATE Employees
SET Salary = Salary * 1.1
WHERE Department = 'HR';


SELECT * FROM Employees;


UPDATE Employees
SET Department = 'Senior IT'
WHERE Salary > 70000.00;


SELECT * FROM Employees;


DELETE FROM Employees AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    WHERE ep.EmployeeID = e.EmployeeID
);


SELECT * FROM Employees;


BEGIN;

WITH new_project AS (
    INSERT INTO Projects
    (ProjectName,               Budget,     StartDate,     EndDate     )
    VALUES
    ('Cloud Migration',         125000.00,  '2023-02-20',  '2023-08-15')
    RETURNING id;
)

INSERT INTO EmployeeProjects
(EmployeeID, ProjectID,  HoursWorked)
VALUES
(2,          (SELECT id FROM new_project),          140),
(4,          (SELECT id FROM new_project),          125);

COMMIT;


SELECT * FROM Projects;

SELECT * FROM EmployeeProjects;