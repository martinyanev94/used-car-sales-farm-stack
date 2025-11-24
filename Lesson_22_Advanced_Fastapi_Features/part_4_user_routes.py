from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import User

async def get_current_user(db: Session = Depends(get_db), user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/{user_id}")
async def read_user(user: User = Depends(get_current_user)):
    return user
