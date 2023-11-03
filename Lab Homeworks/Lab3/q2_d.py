import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("localhost", 27017)
db = client["course_management"]

# Get the Teach collection
teach_collection = db["Teach"]

# Find the number of courses taught by each instructor in Fall 2023
instructor_counts = teach_collection.aggregate([
    {
        "$match": {
            "semester": "Fall 2023"
        }
    },
    {
        "$group": {
            "_id": "$rid",
            "count": {"$sum": 1}
        }
    }
])

# Find the instructor with the largest number of courses
max_instructor_count = max(instructor_counts, key=lambda instructor: instructor["count"])

# Print the instructor ID
print(max_instructor_count["_id"])

# Close the connection to the MongoDB database
client.close()
