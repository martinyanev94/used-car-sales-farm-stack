from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/async-data")
async def read_async_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()
