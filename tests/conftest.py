import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
