from fastapi import Depends, HTTPException, status

def verify_user(token: str):
    if token != "validtoken":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@app.get("/secure-data/")
async def secure_data(token: str = Depends(verify_user)):
    return {"data": "This is secured data!"}
