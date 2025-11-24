from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
user_collection = db['users']

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users/")
async def create_user(user: User):
    user_data = user.dict()
    user_collection.insert_one(user_data)
    return {"message": "User created successfully!", "user": user_data}
