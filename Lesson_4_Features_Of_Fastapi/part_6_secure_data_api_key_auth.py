from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

API_KEY = "my_secret_api_key"

async def api_key_auth(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/secure-data/")
async def secure_data(api_key: str = Depends(api_key_auth)):
    return {"message": "This is protected data"}
