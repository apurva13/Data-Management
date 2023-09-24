import requests
import sys


# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"
    
def instructor_exists(instructor_id):
    # Check if the student exists in the student database
    response = requests.get(f"{firebase_url}/instructors/{instructor_id}.json")

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

def teach_course(instructor_id, course_number, semester):
    # Check if the student, course, and semester exist in the database

    if not instructor_exists(instructor_id):
        print(f"Error: Instructor {instructor_id} does not exist in the database.")
        return

    if not course_exists(course_number):
        print(f"Error: Course {course_number} does not exist in the database.")
        return
    
    if not semester_exists(course_number, semester):
        print(f"Error: Semester {semester} does not exist for course {course_number}.")
        return

    # Construct the URL for storing the relationship
    relationship_url = f"{firebase_url}/schedule/{instructor_id}.json"

    # Check if the student is already taking this course in the same semester
    response = requests.get(relationship_url)

    if response.status_code == 200:
        schedule = response.json()
        if schedule is None:
            schedule = {}

        if course_number in schedule:
            if semester in schedule[course_number]:
                print(f"Error: Instructor {instructor_id} is already taking course {course_number} in semester {semester}.")
                return
            else:
                schedule[course_number].append(semester)
        else:
            schedule[course_number] = [semester]

    else:
        schedule = {course_number: [semester]}

    response = requests.put(relationship_url, json=schedule)

    if response.status_code == 200:
        print(f"Instructor {instructor_id} is taking course {course_number} in semester {semester}.")
    else:
        print(f"Failed to update the relationship. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 teach_course.py <instructor_id> <course_number> <semester>")
        sys.exit(1)

    instructor_id = sys.argv[1]
    course_number = sys.argv[2]
    semester = sys.argv[3]

    teach_course(instructor_id, course_number, semester)

    