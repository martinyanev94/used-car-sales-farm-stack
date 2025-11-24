pipeline = [
    { "$unwind": "$comments" },
    { "$match": { "comments.user": "John" } },
    { "$group": { "_id": None, "averageLikes": { "$avg": "$comments.likes" } } }
]

result = list(blog_posts_collection.aggregate(pipeline))
print(result)
