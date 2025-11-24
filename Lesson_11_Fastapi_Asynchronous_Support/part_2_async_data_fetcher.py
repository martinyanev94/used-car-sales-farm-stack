from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-data")
async def fetch_data():
    await asyncio.sleep(3)  # Simulating a long I/O-bound operation
    return {"message": "Data fetched successfully!"}
