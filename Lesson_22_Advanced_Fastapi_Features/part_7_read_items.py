@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    items = ["item1", "item2", "item3", "item4"] 
    return items[skip : skip + limit]
