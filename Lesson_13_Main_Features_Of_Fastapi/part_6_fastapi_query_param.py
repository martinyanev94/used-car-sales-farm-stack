from fastapi import Depends

def query_param(q: str = None):
    return q

@app.get("/items/")
async def read_items(query: str = Depends(query_param)):
    return {"query": query}
