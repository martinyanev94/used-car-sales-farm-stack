from fastapi import FastAPI
from loguru import logger

app = FastAPI()

logger.add("file.log", rotation="1 MB")  # Automatically rotate logs when they exceed 1 MB

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}
