from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/fast")
async def fast_endpoint():
    return {"message": "This is a fast endpoint"}

@app.get("/slow")
async def slow_endpoint():
    time.sleep(2)
    return {"message": "This endpoint is slow!"}
