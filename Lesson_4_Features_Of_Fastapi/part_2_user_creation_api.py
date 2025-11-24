from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    return {"user_id": user.id, "name": user.name, "email": user.email}
