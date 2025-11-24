from fastapi import HTTPException

@app.delete("/users/{email}")
async def delete_user(email: str):
    try:
        result = users_collection.delete_one({"email": email})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
