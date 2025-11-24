pipeline = [
    { "$unwind": "$comments" },
    { 
        "$group": { 
            "_id": "$_id", 
            "mostLikedComment": { "$max": "$comments.likes" }, 
            "commentDetails": { "$push": "$comments" } 
        } 
    },
    { 
        "$project": { 
            "mostLikedComment": 1, 
            "details": { "$arrayElemAt": ["$commentDetails", 0] }
        } 
    }
]

result = list(blog_posts_collection.aggregate(pipeline))
print(result)
