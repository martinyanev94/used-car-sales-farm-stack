import aioredis

redis = await aioredis.from_url("redis://localhost")

async def get_user_from_cache(username: str):
    user = await redis.get(username)
    if user:
        return user.decode('utf-8')
    return None

async def cache_user(username: str, user_data):
    await redis.set(username, user_data)
