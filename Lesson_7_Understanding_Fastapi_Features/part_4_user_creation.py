from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users/")
async def create_user(user: User):
    return {"username": user.username, "email": user.email, "age": user.age}
