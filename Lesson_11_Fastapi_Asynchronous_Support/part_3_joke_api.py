from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/joke")
async def get_joke():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return {"setup": joke["setup"], "punchline": joke["punchline"]}
