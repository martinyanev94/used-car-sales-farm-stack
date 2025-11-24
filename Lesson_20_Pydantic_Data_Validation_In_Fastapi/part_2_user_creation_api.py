from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/users/")
async def create_user(user: User):
    return {"message": "User created successfully!", "user": user}
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
{
    "id": 1,
    "name": "John Doe",
    "email": "not-an-email"
}
