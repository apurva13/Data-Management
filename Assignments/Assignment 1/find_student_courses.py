import requests
import sys
import json

# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"

def get_student_courses(student_id):
    
    # Check if the student exists in the database
    student_url = f"{firebase_url}/students/{student_id}.json"
    response = requests.get(student_url)

    if response.status_code != 200:
        return {"error": f"Student {student_id} does not exist in the database."}

    student_data = response.json()
    student_name = student_data.get("name", "")

    # Get the student's enrollment data
    enrollment_url = f"{firebase_url}/enrollment/{student_id}.json"
    response = requests.get(enrollment_url)

    if response.status_code != 200:
        return {"name": student_name, "courses": []}

    enrollment_data = response.json()
    courses = []

    for course_number, semesters in enrollment_data.items():
        course_url = f"{firebase_url}/courses/{course_number}.json"
        response = requests.get(course_url)

        if response.status_code == 200:
            course_data = response.json()
            course_title = course_data.get("title", "")
            for semester in semesters:
                courses.append({"number": course_number, "title": course_title, "semester": semester})

    return {"name": student_name, "courses": courses}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_student_courses.py <student_id>")
        sys.exit(1)

    student_id = sys.argv[1]

    student_courses = get_student_courses(student_id)
    print(json.dumps(student_courses, indent=4))
