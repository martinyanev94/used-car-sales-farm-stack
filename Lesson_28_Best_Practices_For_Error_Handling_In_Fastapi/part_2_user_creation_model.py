from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully!"}
