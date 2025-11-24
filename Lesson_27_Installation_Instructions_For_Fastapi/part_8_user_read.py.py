from fastapi import HTTPException

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id not in users_db:  # Assume you have a fictitious database of users
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]
