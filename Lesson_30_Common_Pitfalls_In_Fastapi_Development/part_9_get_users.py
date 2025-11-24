@app.get("/users/", response_model=List[User])
async def get_users():
    """
    Retrieve a list of users.
    
    Returns a list of users if found, otherwise an empty list.
    """
    # Logic to get users
