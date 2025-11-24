from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None    # Optional field
    price: float
    tax: float = None           # Optional field
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
