from fastapi import FastAPI, Depends

app = FastAPI()

def get_current_user():
    return {"user_id": 1, "name": "Alice"}

@app.get("/users/me")
async def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
