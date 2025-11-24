from fastapi import BackgroundTasks

async def send_error_notification(email: str, error_details: str):
    # Here you would implement your email-sending logic
    print(f"Sending error notification to {email}: {error_details}")

@app.post("/users/")
def create_user(user: User, background_tasks: BackgroundTasks):
    try:
        # Logic to create a user
        return {"message": f"User {user.name} created!"}
    except Exception as e:
        background_tasks.add_task(send_error_notification, user.email, str(e))
        raise HTTPException(status_code=500, detail="An error occurred while creating the user.")
