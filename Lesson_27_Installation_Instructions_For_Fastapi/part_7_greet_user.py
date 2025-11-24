@app.get("/greet/{name}", summary="Greet a user", description="Returns a personalized greeting for the user")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
