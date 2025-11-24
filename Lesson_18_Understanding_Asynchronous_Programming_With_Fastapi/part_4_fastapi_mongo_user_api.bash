pip install motor
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()
client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.testdb  # Replace with your database name

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user_collection = database.users
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user is not None:
        return {"name": user['name'], "email": user['email']}
    return {"error": "User not found"}
