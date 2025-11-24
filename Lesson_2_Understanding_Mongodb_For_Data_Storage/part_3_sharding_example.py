# Sharding example (conceptual, this won't run as-is)
db.admin.command('shardCollection', 'social_media_db.users', key={'_id': 'hashed'})

# This will allow MongoDB to distribute the documents across multiple shards
