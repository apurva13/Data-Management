import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient()

# Get the Take collection
take_collection =client["course_management"]["Take"]

# Find students who have taken DSCI 551 but not DSCI 552
students = take_collection.aggregate([
  {
    "$match": {
      "cno": "DSCI 551",
    }
  },
  {
    "$lookup": {
      "from": "Take",
      "localField": "sid",
      "foreignField": "sid",
      "as": "all_takes"
    }
  },
  {
    "$unwind": "$all_takes"
  },
  {
    "$match": {
      "all_takes.cno": "DSCI 552",
      "$expr": {"$eq": [{"$size": "$all_takes"}, 1]},
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
