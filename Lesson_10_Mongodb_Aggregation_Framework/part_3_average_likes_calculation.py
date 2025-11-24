pipeline = [
    { "$unwind": "$comments" },
    { "$group": { "_id": None, "averageLikes": { "$avg": "$comments.likes" } } }
]

result = list(blog_posts_collection.aggregate(pipeline))
print(result)
