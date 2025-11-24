pip install mangum
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

handler = Mangum(app)
