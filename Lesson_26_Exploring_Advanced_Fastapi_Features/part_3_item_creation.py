from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}
