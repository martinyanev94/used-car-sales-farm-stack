from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def perform_background_task(data):
    time.sleep(5)  # Simulating a long-running task
    print(f"Background task completed with data: {data}")

@app.post("/process")
async def process_data(data: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_background_task, data)
    return {"message": "Request received! The processing will happen in the background."}
