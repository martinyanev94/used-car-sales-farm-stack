from fastapi import Depends

class Database:
    def __init__(self):
        self.connection = "Database Connection Established"

def get_database():
    db = Database()
    try:
        yield db
    finally:
        # Here you would close the connection
        pass

@app.get("/items/")
async def read_items(db: Database = Depends(get_database)):
    return {"db_connection": db.connection}
