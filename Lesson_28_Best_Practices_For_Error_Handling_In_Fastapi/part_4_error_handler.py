from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error has occurred. Please try again later."},
    )
