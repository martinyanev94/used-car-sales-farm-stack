# Start the first instance
mongod --replSet "myReplicaSet" --port 27017 --dbpath /data/db1
# Start the second instance
mongod --replSet "myReplicaSet" --port 27018 --dbpath /data/db2
# Start the third instance
mongod --replSet "myReplicaSet" --port 27019 --dbpath /data/db3
rs.initiate()
