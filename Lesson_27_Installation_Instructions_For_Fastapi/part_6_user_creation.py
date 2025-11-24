from pydantic import BaseModel
class User(BaseModel):
    name: str
    email: str
    age: int
@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!"}
{
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}
{
    "message": "User Alice created!"
}
