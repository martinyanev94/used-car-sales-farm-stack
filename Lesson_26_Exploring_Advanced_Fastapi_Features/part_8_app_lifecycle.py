@app.on_event("startup")
async def startup_event():
    print("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown")
