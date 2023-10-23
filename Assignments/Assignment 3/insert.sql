INSERT INTO Course (number, title, semester)
VALUES ('DSCI 351', 'Data Science', 'Spring 2023'),
       ('DSCI 250', 'Machine Learning', 'Spring 2023'),
       ('DSCI 450', 'Natural Language Processing', 'Fall 2023'),
       ('DSCI 550', 'Computer Vision', 'Fall 2023');

INSERT INTO Student (id, name, program)
VALUES ('S12345', 'Alice Smith', 'Computer Science'),
       ('S54321', 'Bob Jones', 'Data Science');

INSERT INTO Instructor (id, name, department)
VALUES ('JSMITH', 'John Smith', 'Computer Science'),
       ('MDOE', 'Mary Doe', 'Data Science');

INSERT INTO Take (sid, cno, semester)
VALUES ('S12345', 'DSCI 351', 'Spring 2023'),
       ('S12345', 'DSCI 250', 'Spring 2023'),
       ('S54321', 'DSCI 351', 'Spring 2023'),
       ('S54321', 'DSCI 450', 'Fall 2023'),
       ('S12345', 'DSCI 450', 'Fall 2023'),
       ('S12345', 'DSCI 351', 'Fall 2023');

INSERT INTO Teach (rid, cno, semester)
VALUES ('JSMITH', 'DSCI 450', 'Fall 2023'),
       ('JSMITH', 'DSCI 550', 'Fall 2023'),
       ('MDOE', 'DSCI 351', 'Fall 2023'),
       ('MDOE', 'DSCI 250', 'Fall 2023');

INSERT INTO TA (sid, hours)
VALUES ('S12345', 10),
       ('S54321', 20);

INSERT INTO Assist (sid, cno, semester)
VALUES ('S12345', 'DSCI 450', 'Fall 2023'),
       ('S54321', 'DSCI 450', 'Fall 2023'),
       ('S54321', 'DSCI 351', 'Fall 2023');





       