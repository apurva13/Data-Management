import requests
import sys


# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"

def course_exists(entity_id):
    # Check if the given entity exists in the database
    response = requests.get(f"{firebase_url}/courses/{entity_id}.json")

    if response.status_code == 200:
        return True
    else:
        return False
    
def add_course(course_number, course_title, semester):
    
    # Check if the course already exists with the same course number and semester
    course_url = f"{firebase_url}/courses/{course_number}.json"
    response = requests.get(course_url)

    if response.status_code == 200:
        existing_data = response.json()
        if existing_data is None:
            existing_data = {}
        existing_semesters = existing_data.get("semesters", [])

        if semester in existing_semesters:
            print(f"Error: Course {course_number} for semester {semester} already exists. Skipping.")
            return

    # Check if the course exists in the database
    if not course_exists(course_number):
        print(f"Error: Course {course_number} does not exist in the database. Skipping.")
        return

    # Add the semester to the existing semesters list
    if semester not in existing_semesters:
        existing_semesters.append(semester)

    data = {
        "number": course_number,
        "title": course_title,
        "semesters": existing_semesters
    }

    # Send a PUT request to update the course data
    response = requests.put(course_url, json=data)

    if response.status_code == 200:
        print(f"Semester {semester} added to course {course_number}.")
    else:
        print(f"Failed to update course data. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_course.py <course_number> <course_title> <semester>")
        sys.exit(1)

    course_number = sys.argv[1]
    course_title = sys.argv[2]
    semester = sys.argv[3]

    add_course(course_number, course_title, semester)
