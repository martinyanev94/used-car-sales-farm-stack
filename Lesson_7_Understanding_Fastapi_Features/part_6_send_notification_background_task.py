from fastapi import BackgroundTasks

def send_email(email: str):
    # Simulate email sending
    print(f"Sending email to {email}")

@app.post("/send-notification/")
async def send_notification(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(send_email, email)
    return {"message": "Notification scheduled."}
