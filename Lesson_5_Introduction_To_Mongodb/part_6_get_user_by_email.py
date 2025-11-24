@app.get("/users/{email}")
async def read_user(email: str):
    user = users_collection.find_one({"email": email})
    if user:
        return user
    return {"error": "User not found"}
