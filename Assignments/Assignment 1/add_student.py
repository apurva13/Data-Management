import requests
import sys
import json
import pandas

# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"


def student_exists(student_id):
    # Construct the URL for the student data
    student_url = f"{firebase_url}/students/{student_id}.json"

    # Send a GET request to check if the student already exists
    response = requests.get(student_url)

    if response.status_code == 200 and response.json():
        return True
    else:
        return False


def add_student(student_id, student_name, program):

    if student_exists(student_id):
        print(f"Student {student_id} already exists. Skipping.")
        return

    data = {
        "id": student_id,
        "name": student_name,
        "program": program
    }

    # Construct the URL for the student data
    student_url = f"{firebase_url}/students/{student_id}.json"

    # Send a PATCH request to add the student data
    response = requests.patch(student_url, json=data)

    if response.status_code == 200:
        print(f"Student {student_id} added successfully.")
    else:
        print(f"Failed to add student {student_id}. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # print("Usage: python3 add_student.py <student_id> <student_name> <program>")
        sys.exit(1)
    student_id = sys.argv[1]
    student_name = sys.argv[2]
    program = sys.argv[3]

    add_student(student_id, student_name, program)
