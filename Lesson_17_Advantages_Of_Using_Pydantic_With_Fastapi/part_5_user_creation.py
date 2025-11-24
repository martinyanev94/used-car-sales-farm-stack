from datetime import datetime
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    email: str
    registered_at: datetime = Field(default_factory=datetime.now)

@app.post("/users/")
async def create_user(user: User):
    user_collection = database.users
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}
