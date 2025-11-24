from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message + "\n")

@app.get("/send-message/{message}")
async def send_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent in the background!"}
