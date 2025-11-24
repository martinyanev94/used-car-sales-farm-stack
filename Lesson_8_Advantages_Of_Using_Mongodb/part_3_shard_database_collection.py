# Sharding an existing collection
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce_database']

# Enable sharding for the database
client.admin.command('enableSharding', 'ecommerce_database')

# Shard the 'products' collection based on the 'product_id'
client.admin.command('shardCollection', 'ecommerce_database.products', key={'product_id': 1})
