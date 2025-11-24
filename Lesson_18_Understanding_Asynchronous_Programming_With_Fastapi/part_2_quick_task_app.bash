uvicorn main:app --reload
@app.get("/quick-task/")
async def quick_task():
    return {"message": "This task is quick!"}
