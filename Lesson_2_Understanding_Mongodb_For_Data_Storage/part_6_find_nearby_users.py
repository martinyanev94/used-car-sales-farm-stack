async def find_nearby_users(longitude, latitude, max_distance):
    nearby_users = await db.users.find({
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                },
                "$maxDistance": max_distance
            }
        }
    }).to_list(length=None)
    return nearby_users
