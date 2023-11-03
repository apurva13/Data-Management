import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient()

# Get the Take collection
take_collection = client["course_management"]["Take"]

# Find students who have taken both DSCI 551 and DSCI 552
students = take_collection.aggregate([
    {
        "$match": {
            "$or": [
                {"cno": "DSCI 551"},
                {"cno": "DSCI 552"},
            ]
        }
    },
    {
        "$group": {
            "_id": "$sid",
            "count": {"$sum": 1}
        }
    },
    {
        "$match": {
            "count": {"$eq": 2},
        }
    },
    {
        "$project": {
            "_id": 1
        }
    }
])

# Print student IDs
for student in students:
    print(student["_id"])

# Close the connection to the MongoDB database
client.close()
