from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    print(f"Webhook received: {payload}")
    return {"status": "success"}
