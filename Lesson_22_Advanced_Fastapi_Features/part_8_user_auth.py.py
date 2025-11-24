from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement logic to decode the JWT and fetch the user
    # For simplicity, we will mock this part now
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "fakeuser"}

@app.get("/users/me")
async def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
