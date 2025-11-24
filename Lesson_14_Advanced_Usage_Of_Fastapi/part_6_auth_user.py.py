from fastapi import Security, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"user": "current user"}

@app.get("/users/me", response_model=dict)
async def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
