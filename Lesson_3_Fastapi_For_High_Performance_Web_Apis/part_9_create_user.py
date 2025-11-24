@app.post("/users/")
async def create_user(user: User):
    return {"user": user}
