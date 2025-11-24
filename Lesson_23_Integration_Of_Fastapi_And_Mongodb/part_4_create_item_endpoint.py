from fastapi import HTTPException

@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    if await db.items.find_one({"name": item.name}):
        raise HTTPException(status_code=400, detail="Item already exists")
    item_dict = item.dict()
    result = await db.items.insert_one(item_dict)
    item_dict["id"] = str(result.inserted_id)
    return item_dict
