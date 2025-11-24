from fastapi import Security, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Logic to authenticate user and return an access token
    return {"access_token": form_data.username, "token_type": "bearer"}
@router.get("/users/me", response_model=User)
async def read_users_me(token: str = Security(oauth2_scheme)):
    # Logic to get the current user's details
    return {"username": "authenticated_user"}
