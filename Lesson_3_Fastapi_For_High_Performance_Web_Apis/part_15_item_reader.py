from fastapi import HTTPException

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 42:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
