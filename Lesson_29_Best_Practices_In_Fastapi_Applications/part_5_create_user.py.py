from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
@router.post("/users/")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Here you would call your user service to handle the actual creation logic
    return {"username": user.username, "email": user.email}
