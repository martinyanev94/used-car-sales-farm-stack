@app.get("/custom_greet/")
def custom_greet(name: str, message: str = "Welcome"):
    return {"greeting": f"{message}, {name}!"}
{
    "greeting": "Hello, Bob!"
}
{
    "greeting": "Welcome, Bob!"
}
