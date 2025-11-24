from fastapi import FastAPI

app = FastAPI()

@app.get("/echo/{message}")
async def echo(message: str):
    return {"message": message}
