from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    print(f"Request: {request.method} {request.url} | Status Code: {response.status_code}")
    return response
