import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient()

# Get the course_management database and the Course collection in one step
course_collection = client["course_management"]["Course"]

# Query for courses offered in Fall 2023
courses = course_collection.find({"semester": "Fall 2023"})

# Print course number and title
for course in courses:
    print(f"Course Number: {course['number']}, Title: {course['title']}")

# Close the MongoDB connection
client.close()