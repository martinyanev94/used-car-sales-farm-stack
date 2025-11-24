from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/joke")
async def get_joke():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://official-joke-api.appspot.com/random_joke")
            response.raise_for_status()  # Raise an error for bad responses
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail="Joke API is unreachable")
    joke = response.json()
    return {"setup": joke["setup"], "punchline": joke["punchline"]}
