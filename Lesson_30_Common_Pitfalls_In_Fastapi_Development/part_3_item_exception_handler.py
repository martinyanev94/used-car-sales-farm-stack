from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

class ItemNotFound(Exception):
    pass

@app.exception_handler(ItemNotFound)
async def item_not_found_exception_handler(request, exc: ItemNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 3:  # Let's say only item_id 3 exists
        raise ItemNotFound(f"Item with id {item_id} not found!")
    return {"item_id": item_id, "name": "Example Item"}
