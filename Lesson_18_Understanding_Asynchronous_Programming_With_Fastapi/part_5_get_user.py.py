from fastapi import HTTPException

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user_collection = database.users
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": user['name'], "email": user['email']}
