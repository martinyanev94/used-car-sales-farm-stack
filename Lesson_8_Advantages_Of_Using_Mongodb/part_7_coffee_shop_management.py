# Creating a coffee shops collection
coffee_shops = db['coffee_shops']

# Inserting a coffee shop with geolocation
coffee_shop = {
    "name": "Best Coffee",
    "location": {"type": "Point", "coordinates": [-73.856077, 40.848447]}
}
coffee_shops.insert_one(coffee_shop)

# Querying coffee shops within 1 km of a location
nearby_shops = coffee_shops.find({
    "location": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [-73.856077, 40.848447]
            },
            "$maxDistance": 1000
        }
    }
})
