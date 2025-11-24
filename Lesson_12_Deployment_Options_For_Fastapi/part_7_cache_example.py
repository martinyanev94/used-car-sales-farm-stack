import redis

cache = redis.Redis(host='localhost', port=6379)

@app.get("/cached-data")
async def get_cached_data():
    cache_key = "data_key"
    cached_result = cache.get(cache_key)

    if cached_result:
        return {"data": cached_result.decode()}
    
    result = compute_data()  # Some heavy computation
    cache.set(cache_key, result)
    return {"data": result}
