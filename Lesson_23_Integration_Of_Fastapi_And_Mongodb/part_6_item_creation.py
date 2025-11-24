class Category(BaseModel):
    name: str

class Item(BaseModel):
    name: str
    description: str
    price: float
    category: Category

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_dict = item.dict()
    result = await db.items.insert_one(item_dict)
    item_dict["id"] = str(result.inserted_id)
    return item_dict
