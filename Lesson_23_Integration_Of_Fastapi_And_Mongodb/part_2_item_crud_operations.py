@app.get("/items/", response_model=List[Item])
async def read_items():
    items = []
    async for item in db.items.find():
        item["_id"] = str(item["_id"])  # Convert ObjectId to string
        items.append(item)
    return items
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    item_dict = item.dict()
    await db.items.replace_one({"_id": item_id}, item_dict)
    item_dict["_id"] = item_id
    return item_dict
