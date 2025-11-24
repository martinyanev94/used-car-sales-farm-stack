from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
user_collection = db['users']

# Inserting a user with different attributes
user1 = {"username": "john_doe", "email": "john@example.com", "age": 30}
user2 = {"username": "jane_doe", "email": "jane@example.com", "age": 28, "profile_picture": "jane.png"}

user_collection.insert_one(user1)
user_collection.insert_one(user2)
