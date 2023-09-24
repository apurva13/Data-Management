import requests
import sys
import json
import pandas

# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"
    
def student_exists(student_id):
    # Check if the student exists in the student database
    response = requests.get(f"{firebase_url}/students/{student_id}.json")

    if response.status_code == 200 and response.json():
        return True
    else:
        return False
    
def course_exists(course_number):
    # Check if the student exists in the student database
    response = requests.get(f"{firebase_url}/courses/{course_number}.json")

    if response.status_code == 200 and response.json():
        return True
    else:
        return False
    
def semester_exists(course_number, semester):
    # Check if the semester exists for the given course
    response = requests.get(f"{firebase_url}/courses/{course_number}/semesters.json")

    if response.status_code == 200:
        semesters = response.json()
        if semester in semesters:
            return True
    return False

def take_course(student_id, course_number, semester):
    # Check if the student, course, and semester exist in the database

    if not student_exists(student_id):
        print(f"Error: Student {student_id} does not exist in the database.")
        return

    if not course_exists(course_number):
        print(f"Error: Course {course_number} does not exist in the database.")
        return
    
    if not semester_exists(course_number, semester):
        print(f"Error: Semester {semester} does not exist for course {course_number}.")
        return

    # Construct the URL for storing the relationship
    relationship_url = f"{firebase_url}/enrollment/{student_id}.json"

    # Check if the student is already taking this course in the same semester
    response = requests.get(relationship_url)

    if response.status_code == 200:
        enrollment = response.json()
        if enrollment is None:
            enrollment = {}

        if course_number in enrollment:
            if semester in enrollment[course_number]:
                print(f"Error: Student {student_id} is already taking course {course_number} in semester {semester}.")
                return
            else:
                enrollment[course_number].append(semester)
        else:
            enrollment[course_number] = [semester]

    else:
        enrollment = {course_number: [semester]}

    response = requests.put(relationship_url, json=enrollment)

    if response.status_code == 200:
        print(f"Student {student_id} is taking course {course_number} in semester {semester}.")
    else:
        print(f"Failed to update the relationship. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 take_course.py <student_id> <course_number> <semester>")
        sys.exit(1)

    student_id = sys.argv[1]
    course_number = sys.argv[2]
    semester = sys.argv[3]

    take_course(student_id, course_number, semester)

    