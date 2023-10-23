import sys
from sqlalchemy import create_engine
import pandas as pd
import pymysql

def find_courses(student_id):

    # Connect to the MySQL database
    engine = create_engine("mysql+pymysql://dsci551:Dsci-551@localhost:3306/dsci551")

    print("ENGINE:", engine)

# Output student name, program, titles and semesters of all courses taken by the student.
    query = f"""
        SELECT s.name AS student_name, s.program, c.title, c.semester
        FROM Student s
        JOIN Take t ON s.id = t.sid
        JOIN Course c ON t.cno = c.number AND t.semester = c.semester
        WHERE s.id = '{student_id}'
    """

    # Execute the query and print the result using pandas
    result = pd.read_sql(query, engine)
    print(result)

if __name__ == "__main__":
    # Check if a student ID is provided as a command-line argument
    
    if len(sys.argv) != 2:
        print("Usage: python3 find_courses.py <student_id>")
        sys.exit(1)

    student_id = sys.argv[1]
    print("student_id:", student_id)
    find_courses(student_id)

