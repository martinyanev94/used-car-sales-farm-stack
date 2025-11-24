from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
blog_posts_collection = db['blogPosts']

pipeline = [
    { "$unwind": "$comments" },
    { "$group": { "_id": "$_id", "totalComments": { "$sum": 1 } } }
]

result = list(blog_posts_collection.aggregate(pipeline))
print(result)
