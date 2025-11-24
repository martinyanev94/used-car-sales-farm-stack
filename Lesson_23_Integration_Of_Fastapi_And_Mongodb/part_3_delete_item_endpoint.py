@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await db.items.delete_one({"_id": item_id})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    else:
        return {"message": "Item not found"}
