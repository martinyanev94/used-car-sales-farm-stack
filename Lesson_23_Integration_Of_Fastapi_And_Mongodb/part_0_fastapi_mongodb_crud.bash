pip install fastapi[all] motor
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.my_database   # replace with your database name

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_dict = item.dict()
    result = await db.items.insert_one(item_dict)
    item_dict["id"] = str(result.inserted_id)
    return item_dict
