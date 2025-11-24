from fastapi import FastAPI, Depends
from time import time

app = FastAPI()
cache = {}

@app.get("/cached-data")
async def get_cached_data():
    if "data" in cache and time() - cache["timestamp"] < 60:
        return cache["data"]
    else:
        data = await fetch_data()  # Assume fetch_data() fetches from a slow source
        cache["data"] = data
        cache["timestamp"] = time()
        return data
