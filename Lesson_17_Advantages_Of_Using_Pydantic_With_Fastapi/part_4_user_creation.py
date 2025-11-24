from typing import List

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class User(BaseModel):
    name: str
    email: str
    addresses: List[Address]

@app.post("/users/")
async def create_user(user: User):
    user_collection = database.users
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}
