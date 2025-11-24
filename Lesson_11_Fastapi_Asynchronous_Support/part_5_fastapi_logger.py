from fastapi import FastAPI, Depends
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

async def logger(message: str):
    logging.info(message)

@app.get("/data")
async def read_data(dep=Depends(logger("Fetching data..."))):
    await asyncio.sleep(2)  # Simulating data fetching
    return {"data": "Sample Data"}
