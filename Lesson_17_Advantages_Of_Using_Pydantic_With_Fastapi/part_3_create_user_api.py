from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

app = FastAPI()
client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.mydatabase

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    user_collection = database.users
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}
