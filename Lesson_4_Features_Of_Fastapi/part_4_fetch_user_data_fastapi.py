import asyncio
from fastapi import FastAPI

app = FastAPI()

async def fetch_user_data(user_id: int):
    # Simulating a database call with asyncio.sleep
    await asyncio.sleep(2)  # Simulate some I/O delay
    return {"user_id": user_id, "name": "John Doe"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user_data = await fetch_user_data(user_id)
    return user_data
