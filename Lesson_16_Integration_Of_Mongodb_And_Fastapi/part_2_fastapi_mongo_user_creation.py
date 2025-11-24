from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.mydatabase  # Replace 'mydatabase' with your database name
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    user_collection = database.users  # Replace with your collection name
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}
