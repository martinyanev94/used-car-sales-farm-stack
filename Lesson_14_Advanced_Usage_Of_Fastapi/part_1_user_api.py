from fastapi import FastAPI, Depends
from typing import List

app = FastAPI()

# Mock database
class FakeDatabase:
    def __init__(self):
        self.users = {"1": {"name": "Alice"}, "2": {"name": "Bob"}}

    def get_user(self, user_id: str):
        return self.users.get(user_id)

fake_database = FakeDatabase()

def get_db():
    return fake_database

@app.get("/users/{user_id}", response_model=dict)
async def read_user(user_id: str, db: FakeDatabase = Depends(get_db)):
    user = db.get_user(user_id)
    if user is None:
        return {"error": "User not found."}
    return user
