class UserService:
    def __init__(self, db: FakeDatabase):
        self.db = db

    def get_user(self, user_id: str):
        return self.db.get_user(user_id)

user_service = UserService(fake_database)

@app.get("/users/{user_id}", response_model=dict)
async def read_user(user_id: str, service: UserService = Depends(lambda: user_service)):
    user = service.get_user(user_id)
    if user is None:
        return {"error": "User not found."}
    return user
