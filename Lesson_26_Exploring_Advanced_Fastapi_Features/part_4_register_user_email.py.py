from fastapi import BackgroundTasks

def send_welcome_email(email: str):
    print(f"Sending email to {email}")

@app.post("/register/")
async def register_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_welcome_email, email)
    return {"message": "User registered successfully."}
