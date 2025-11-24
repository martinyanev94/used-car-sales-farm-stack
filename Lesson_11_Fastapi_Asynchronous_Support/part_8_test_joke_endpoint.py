import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.mark.asyncio
async def test_get_joke():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/joke")
        assert response.status_code == 200
        assert "setup" in response.json()
        assert "punchline" in response.json()
