pip install pymongo
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client.get_database('mydatabase')
users_collection = db.get_collection('users')
