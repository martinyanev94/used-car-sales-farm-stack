class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address
@app.post("/users/")
async def create_user(user: User):
    return {"message": "User created successfully!", "user": user}
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere",
        "zip_code": "12345"
    }
}
