@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10):
    items = []
    cursor = db.items.find().skip(skip).limit(limit)
    async for item in cursor:
        item["_id"] = str(item["_id"])
        items.append(item)
    return items
