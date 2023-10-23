-- a.	Find out which courses were offered in Spring 2023 but not in Fall 2023. Report course number and title
SELECT number, title
FROM Course
WHERE semester = 'Spring 2023'
AND number NOT IN (
  SELECT number
  FROM Course
  WHERE semester = 'Fall 2023'
);

-- b.	Find out titles of which courses in Fall 2023 contain “data” and are taught by Professor “John Smith”.
SELECT title
FROM Course
WHERE title LIKE '%data%'
AND semester = 'Fall 2023'
AND number IN (
  SELECT cno
  FROM Teach
  WHERE rid = (
    SELECT id
    FROM Instructor
    WHERE name = 'John Smith'
  )
);

-- c.	Find out which students have taken both DSCI 351 and DSCI 250 (both are course numbers). Report student id and name.
SELECT id,name
FROM Student where id IN 
(SELECT t1.sid FROM Take t1
INNER JOIN Take t2 ON t1.sid = t2.sid
WHERE t1.cno = 'DSCI 351'
AND t2.cno = 'DSCI 250');

-- d.	Find out which students have taken DSCI 351 but not DSCI 250. Report student id and name.
SELECT id, name
FROM Student WHERE id IN
(
  SELECT sid
  FROM Take
  WHERE cno = 'DSCI 351'
  AND sid NOT IN (
    SELECT sid FROM Take WHERE cno = 'DSCI 250')
);

-- e.	Find out which students did not take any courses in Fall 2023.
SELECT id, name
FROM Student
WHERE id NOT IN (
  SELECT sid
  FROM Take
  WHERE semester = 'Fall 2023'
);

-- f.	Find out which instructors teach the largest number of courses in Fall 2023. Report instructor id and name.

SELECT t.rid, i.name, COUNT(*) AS num_courses
FROM Teach t
JOIN 
Instructor i 
ON t.rid = i.id
WHERE t.semester = 'Fall 2023'
GROUP BY t.rid, i.name
ORDER BY num_courses DESC
LIMIT 1;


-- g.	Find out which instructors teach only one course in Fall 2023 without using aggregate functions in SQL. Report instructor names and course numbers.
SELECT t.rid, t.cno, i.name
FROM Teach t
JOIN Instructor i ON t.rid = i.id
WHERE NOT EXISTS (
  SELECT 1
  FROM Teach t2
  WHERE t2.rid = t.rid
  AND t2.cno != t.cno
  AND t2.semester = 'Fall 2023'
);


-- h.	Find out for each instructor, the average number of students in his/her courses offered in Fall 2023. For example, if an instructor teaches two courses, course X with 100 students and course Y with 200 students, then the average number of students in his/her course would be 150. Report the instructor id and the average number.
SELECT t.rid AS instructor_id, AVG(c.num_students) AS avg_students
FROM Teach t
JOIN (
    SELECT cno, semester, COUNT(sid) AS num_students
    FROM Take
    GROUP BY cno, semester
) c ON t.cno = c.cno AND t.semester = c.semester
WHERE t.semester = 'Fall 2023'
GROUP BY t.rid;


-- i.	Find out which courses offered in Fall 2023 have only one TA. Report the course titles.
SELECT title
FROM Course 
WHERE number IN
(
   SELECT cno
   FROM Assist WHERE semester='Fall 2023'  
   GROUP BY cno 
   HAVING COUNT(*)=1
);



-- j.	Find out which TAs work for more than 15 hours a week and take 3 courses in Fall 2023. Report names of such TAs.

SELECT s1.name
FROM Student s1
WHERE s1.id IN
(
    SELECT s.id
    FROM Student s
    JOIN TA t ON t.sid=s.id
    JOIN Take ta ON t.sid = ta.sid
    WHERE t.hours > 15
    AND ta.semester = 'Fall 2023'
    GROUP BY t.sid
    HAVING COUNT(DISTINCT(cno)) = 3 
);