import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mydatabase

async def create_user(user_data):
    result = await db.users.insert_one(user_data)
    return str(result.inserted_id)
