from fastapi import Cookie

async def get_session(session_id: str = Cookie(None)):
    if session_id != "session_id_1":
        return {"error": "Invalid session"}
    return {"user": "session user"}

@app.get("/session", response_model=dict)
async def read_session_info(session: dict = Depends(get_session)):
    return session
