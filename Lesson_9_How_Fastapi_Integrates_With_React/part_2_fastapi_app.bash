pip install fastapi uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

# Sample data
items = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Cherry", "price": 0.2}
]

@app.get("/items/")
async def read_items():
    return items
uvicorn main:app --reload
