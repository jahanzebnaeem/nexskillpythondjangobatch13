-- CRUD --
--CREATE TABLE Persons (
--    ID int NOT NULL,
--    LastName varchar(255) NOT NULL,
--    FirstName varchar(255),
--    Age int,
--    PRIMARY KEY (ID)
--);
--INSERT INTO Persons
--VALUES (2, 'Jahanzeb', 'Alishba', 10);
--UPDATE Persons
--SET lastname='Jahanzeb'
--WHERE id=2;
--DELETE FROM Persons WHERE id=2;
--SELECT * FROM Persons;
--CREATE TABLE Courses (
--    ID int NOT NULL,
--    Name varchar(255) NOT NULL,
--    Price int NOT NULL,
--    PRIMARY KEY (ID)
--);
--CREATE TABLE RegisteredCourses (
--    ID int NOT NULL,
--    PersonID int NOT NULL,
--    CourseID int NOT NULL,
--    PRIMARY KEY (ID)
--);
SELECT * FROM Persons;
SELECT * from Courses;
SELECT * FROM RegisteredCourses;