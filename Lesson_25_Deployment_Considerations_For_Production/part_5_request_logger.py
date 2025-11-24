import logging
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger = logging.getLogger("mylogger")
    logger.info(f"Path: {request.url.path} | Method: {request.method}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response
