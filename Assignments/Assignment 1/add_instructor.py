import requests
import sys
import json
import pandas

# Firebase Realtime Database URL
firebase_url = "https://homework1-aef9f-default-rtdb.firebaseio.com/"

def instructor_exists(instructor_id):
    # Construct the URL for the student data
    instructor_url = f"{firebase_url}/instructors/{instructor_id}.json"
    print(instructor_url)

    # Send a GET request to check if the student already exists
    response = requests.get(instructor_url)

    if response.status_code == 200 and response.json():
        return True
    else:
        return False
    


def add_instructor(instructor_id, instructor_name, department):

    if instructor_exists(instructor_id):
        print(f"Instructor {instructor_id} already exists. Skipping.")
        return


    data = {
        "id": instructor_id,
        "name": instructor_name,
        "department": department
    }

    # Construct the URL for the instructor data
    instructor_url = f"{firebase_url}/instructors/{instructor_id}.json"

    # Send a PATCH request to add the instructor data
    response = requests.patch(instructor_url, json=data)

    if response.status_code == 200:
        print(f"Instructor {instructor_id} added successfully.")
    else:
        print(f"Failed to add instructor {instructor_id}. Error: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_instructor.py <instructor_id> <instructor_name> <department>")
        sys.exit(1)

    instructor_id = sys.argv[1]
    instructor_name = sys.argv[2]
    department = sys.argv[3]

    add_instructor(instructor_id, instructor_name, department)
