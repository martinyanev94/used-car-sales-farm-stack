import httpx

@app.get("/user-info/{user_id}")
async def user_info(user_id: str):
    async with httpx.AsyncClient() as client:
        user_info_response = await client.get(f'http://example.com/users/{user_id}')
        orders_response = await client.get(f'http://example.com/orders/{user_id}')
        
        user_info = user_info_response.json()
        orders = orders_response.json()
    
    return {"user_info": user_info, "orders": orders}
