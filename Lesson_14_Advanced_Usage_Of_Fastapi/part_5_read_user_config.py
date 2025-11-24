@app.get("/users/{user_id}/config")
async def read_user_config(user_id: str, user: dict = Depends(read_user), config: Settings = Depends(get_settings)):
    return {"user": user, "API Key": config.api_key}
