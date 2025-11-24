@app.post("/items/")
async def create_item(item: Item):
    items.append(item.dict())
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(items):
        if existing_item['id'] == item_id:
            items[idx] = item.dict()
            return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global items
    items = [item for item in items if item['id'] != item_id]
    return {"message": "Item deleted successfully"}
