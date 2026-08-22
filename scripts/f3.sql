CREATE USER hr_user WITH LOGIN PASSWORD 'pass';


GRANT USAGE ON SCHEMA public TO hr_user;


GRANT SELECT
ON Employees
TO hr_user;


GRANT USAGE, SELECT
ON SEQUENCE employees_employeeid_seq
TO hr_user;


GRANT INSERT, UPDATE
ON Employees
TO hr_user;