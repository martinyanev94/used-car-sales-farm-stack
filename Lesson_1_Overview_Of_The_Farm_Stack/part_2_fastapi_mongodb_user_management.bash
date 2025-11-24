pip install motor
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId
from typing import List

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.user_db

class User(BaseModel):
    name: str
    email: str

@app.post("/users/", response_model=User)
async def create_user(user: User):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

@app.get("/users/", response_model=List[User])
async def get_users():
    users = []
    async for user in db.users.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users
{
    "name": "John Doe",
    "email": "john@example.com"
}
