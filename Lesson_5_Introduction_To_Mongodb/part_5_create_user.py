@app.post("/users/")
async def create_user(user: User):
    user_data = user.dict()
    users_collection.insert_one(user_data)
    return {"message": "User created successfully", "user": user_data}
