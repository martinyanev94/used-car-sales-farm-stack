pip install databases[postgresql] asyncpg
from fastapi import FastAPI
from databases import Database

app = FastAPI()

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/mydatabase"
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = "SELECT * FROM items WHERE id = :id"
    row = await database.fetch_one(query, values={"id": item_id})
    return row
