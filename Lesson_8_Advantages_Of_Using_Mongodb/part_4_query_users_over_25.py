# Querying users from the collection
users_over_25 = user_collection.find({"age": {"$gt": 25}}).sort("username")

for user in users_over_25:
    print(user)
