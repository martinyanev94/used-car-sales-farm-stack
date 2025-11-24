import httpx

async def fetch_data_from_service_a():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.service-a.com/data")
        return response.json()

async def fetch_data_from_service_b():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.service-b.com/data")
        return response.json()

@app.get("/aggregated-data/")
async def get_aggregated_data():
    data_a, data_b = await asyncio.gather(
        fetch_data_from_service_a(),
        fetch_data_from_service_b()
    )
    return {"service_a": data_a, "service_b": data_b}
