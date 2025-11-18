import pytest
from services.auth.auth import Auth


@pytest.fixture(scope="function")
async def user_register(client):
    auth = Auth(client=client)
    return await auth.register_random_user()
