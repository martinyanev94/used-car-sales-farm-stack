from pydantic import BaseModel

class Settings(BaseModel):
    api_key: str = "default_secret_key"

settings = Settings()

def get_settings():
    return settings

@app.get("/config")
async def read_config(config: Settings = Depends(get_settings)):
    return {"API Key": config.api_key}
