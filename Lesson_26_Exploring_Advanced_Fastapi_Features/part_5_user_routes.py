from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def get_users():
    return [{"username": "john_doe"}, {"username": "jane_doe"}]

app.include_router(router, prefix="/api/v1")
