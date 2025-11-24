from motor.motor_asyncio import AsyncIOMotorClient

async def create_user_and_post(user_data, post_data):
    async with client.start_session() as session:
        async with session.start_transaction():
            user = await db.users.insert_one(user_data, session=session)
            post = await db.posts.insert_one({**post_data, "user_id": user.inserted_id}, session=session)
            return user.inserted_id, post.inserted_id
