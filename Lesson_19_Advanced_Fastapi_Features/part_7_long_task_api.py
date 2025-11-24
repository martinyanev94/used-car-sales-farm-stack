from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/long-task")
async def long_task():
    await asyncio.sleep(5)  # Simulating a long task
    return {"message": "Task completed!"}
