from fastapi import HTTPException

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    user_collection = database.users
    user = await user_collection.find_one({"_id": user_id})
    if user is not None:
        return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}
    raise HTTPException(status_code=404, detail="User not found")
