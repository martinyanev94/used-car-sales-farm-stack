async def get_users_with_post(posts_count):
    users = await db.users.find({"posts": {"$size": posts_count}}).to_list(length=None)
    return users
