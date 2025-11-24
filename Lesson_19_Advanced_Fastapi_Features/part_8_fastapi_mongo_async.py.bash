pip install motor
from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# MongoDB connection string
mongo_uri = "mongodb://localhost:27017"
client = AsyncIOMotorClient(mongo_uri)
db = client.mydatabase

async def get_db():
    return db

@app.get("/items/{item_id}")
async def read_item(item_id: int, database = Depends(get_db)):
    document = await database.items.find_one({"id": item_id})
    return document if document else {"message": "Item not found!"}
