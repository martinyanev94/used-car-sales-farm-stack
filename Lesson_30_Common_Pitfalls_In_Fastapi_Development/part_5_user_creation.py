from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr

@app.post("/users/")
async def create_user(user: UserCreate):
    return {"username": user.username, "email": user.email}
