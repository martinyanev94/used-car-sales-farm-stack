from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/external")
async def fetch_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/delay/3")
    return {"data": response.json()}
