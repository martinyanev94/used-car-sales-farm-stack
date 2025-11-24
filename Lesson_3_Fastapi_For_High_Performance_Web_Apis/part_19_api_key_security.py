from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "expected_api_key":
        raise HTTPException(status_code=403, detail="Could not validate API KEY")

@app.get("/secure-data/")
async def read_secure_data(api_key: str = Depends(get_api_key)):
    return {"data": "This is protected data"}
