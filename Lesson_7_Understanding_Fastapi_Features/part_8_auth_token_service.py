from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate the user credentials
    if form_data.username == "user" and form_data.password == "password":
        token = jwt.encode({"sub": form_data.username}, "secret", algorithm="HS256")
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
