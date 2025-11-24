@app.put("/users/{email}")
async def update_user(email: str, user: User):
    updated_user = users_collection.find_one_and_update(
        {"email": email},
        {"$set": user.dict()},
        return_document=True
    )
    if updated_user:
        return {"message": "User updated successfully", "user": updated_user}
    return {"error": "User not found"}
