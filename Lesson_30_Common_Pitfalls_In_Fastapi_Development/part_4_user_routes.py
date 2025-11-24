@app.get("/users/")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users
from sqlalchemy.ext.asyncio import AsyncSession

@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await db.execute(select(User))
    return users.scalars().all()
