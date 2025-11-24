from fastapi import Security, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_users_me(token: str = Security(oauth2_scheme)):
    if token != "fake-token":  # Here you should implement actual verification
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"user": "current user"}
