from fastapi import FastAPI, HTTPException

@app.post("/users/")
async def create_user(user: User):
    user_collection = database.users
    user_dict = user.dict()
    
    # Simulated example for checking an existing user logic
    existing_user = await user_collection.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")
    
    result = await user_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}
