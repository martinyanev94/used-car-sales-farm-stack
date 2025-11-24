from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def log_message(message: str):
    print(f"Logging message: {message}")

@app.get("/long-task-with-log")
async def long_task_with_log(background_tasks: BackgroundTasks):
    background_tasks.add_task(log_message, "Long task started")
    await asyncio.sleep(5)
    return {"message": "Task completed!"}
