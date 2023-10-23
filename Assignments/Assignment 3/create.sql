SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Take;
DROP TABLE IF EXISTS Teach;
DROP TABLE IF EXISTS TA;
DROP TABLE IF EXISTS Assist;
SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE Course (number VARCHAR(255), title VARCHAR(255), semester VARCHAR(255), PRIMARY KEY (number,semester) );


CREATE TABLE Student ( id VARCHAR(4), name VARCHAR(255), program VARCHAR(255), PRIMARY KEY (id,program) );


CREATE TABLE Instructor (id VARCHAR(255), name VARCHAR(255), department VARCHAR(255), PRIMARY KEY (id,department) );


CREATE TABLE Take (sid VARCHAR(4), cno VARCHAR(255), semester VARCHAR(255), PRIMARY KEY(sid, cno, semester), FOREIGN KEY (sid) REFERENCES Student(id), FOREIGN KEY (cno) REFERENCES Course(number) );


CREATE TABLE Teach (rid VARCHAR(255),  cno VARCHAR(255), semester VARCHAR(255), PRIMARY KEY(rid, cno, semester), FOREIGN KEY (rid) REFERENCES Instructor(id), FOREIGN KEY (cno) REFERENCES Course(number) );


CREATE TABLE TA (sid VARCHAR(4), hours INT, PRIMARY KEY (sid) );


CREATE TABLE Assist (sid VARCHAR(4), cno VARCHAR(255), semester VARCHAR(255), PRIMARY KEY(sid, cno, semester), FOREIGN KEY (sid) REFERENCES Student(id), FOREIGN KEY (cno) REFERENCES Course(number) );

