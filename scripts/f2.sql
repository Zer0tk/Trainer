-- Table 'Departments'
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);


ALTER TABLE Employees
ADD Email VARCHAR(100);


UPDATE Employees
SET Email = CONCAT(lower(FirstName), lower(LastName), EmployeeID, '@example.com');


ALTER TABLE Employees
ADD UNIQUE (Email);


SELECT * FROM Employees;


ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;