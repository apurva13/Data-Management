import requests
import sys
import json

# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"

def get_instructor_courses(instructor_id):
    # Check if the instructor exists in the database
    instructor_url = f"{firebase_url}/instructors/{instructor_id}.json"
    response = requests.get(instructor_url)

    if response.status_code != 200:
        return {"error": f"Instructor {instructor_id} does not exist in the database."}

    instructor_data = response.json()
    instructor_name = instructor_data.get("name", "")

    # Get the instructor's course assignments
    assignments_url = f"{firebase_url}/schedule/{instructor_id}.json"
    response = requests.get(assignments_url)

    if response.status_code != 200:
        return {"name": instructor_name, "courses": []}

    assignments_data = response.json()
    courses = []

    for course_number, semesters in assignments_data.items():
        course_url = f"{firebase_url}/courses/{course_number}.json"
        response = requests.get(course_url)

        if response.status_code == 200:
            course_data = response.json()
            course_title = course_data.get("title", "")
            for semester in semesters:
                courses.append({"number": course_number, "title": course_title, "semester": semester})

    return {"name": instructor_name, "courses": courses}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_instructor_courses.py <instructor_id>")
        sys.exit(1)

    instructor_id = sys.argv[1]

    instructor_courses = get_instructor_courses(instructor_id)
    print(json.dumps(instructor_courses, indent=4))
