@app.delete("/users/{email}")
async def delete_user(email: str):
    result = users_collection.delete_one({"email": email})
    if result.deleted_count > 0:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}
