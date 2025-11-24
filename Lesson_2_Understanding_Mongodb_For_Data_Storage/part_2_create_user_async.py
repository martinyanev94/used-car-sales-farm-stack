from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.social_media_db

async def create_user(name, email, posts):
    user_data = {
        "name": name,
        "email": email,
        "posts": posts
    }
    result = await db.users.insert_one(user_data)
    return str(result.inserted_id)

# Example usage
await create_user("Jane Doe", "jane@example.com", [])
