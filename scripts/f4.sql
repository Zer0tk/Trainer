SELECT * FROM Employees;


DELETE FROM Employees AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM EmployeeProjects AS ep
    WHERE ep.EmployeeID = e.EmployeeID
);


SELECT * FROM Employees;


BEGIN;

INSERT INTO Projects
(ProjectName,               Budget,     StartDate,     EndDate     )
VALUES
('Cloud Migration',         125000.00,  '2023-02-20',  '2023-08-15');

INSERT INTO EmployeeProjects
(EmployeeID, ProjectID,  HoursWorked)
VALUES
(2,          4,          140),
(4,          4,          125);

COMMIT;


SELECT * FROM Projects;

SELECT * FROM EmployeeProjects;