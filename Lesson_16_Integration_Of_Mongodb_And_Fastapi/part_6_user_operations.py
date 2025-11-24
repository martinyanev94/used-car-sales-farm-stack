@app.patch("/users/{user_id}")
async def update_user(user_id: str, user: User):
    user_collection = database.users
    update_result = await user_collection.update_one({"_id": user_id}, {"$set": user.dict()})
    if update_result.modified_count == 1:
        return {"msg": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    user_collection = database.users
    delete_result = await user_collection.delete_one({"_id": user_id})
    if delete_result.deleted_count == 1:
        return {"msg": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
