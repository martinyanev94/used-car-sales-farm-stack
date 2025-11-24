from fastapi import FastAPI
from typing import Dict
import time

app = FastAPI()
cache: Dict[str, dict] = {}

@app.get("/data")
async def read_data(item_id: str):
    if item_id in cache:
        return cache[item_id]
    
    # Simulate a slow database call with sleep
    time.sleep(2)  # Simulate a delay
    data = {"item_id": item_id, "value": "expensive data"}
    cache[item_id] = data
    return data
