from pymongo import MongoClient
from fastapi import Depends

client = MongoClient("mongodb://localhost:27017")
db = client.my_database

def get_db():
    return db

@app.get("/users/")
async def read_users(db=Depends(get_db)):
    users = db.users.find()
    return list(users)
