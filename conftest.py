import pytest
import logging

from clients.event_hooks import log_request_event_hook, log_response_event_hook
from config import settings
from httpx import AsyncClient


def pytest_configure(config):
    """Стандартная конфигурация pytest"""

    logging.basicConfig(
        level=settings.logger.log_level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


@pytest.fixture(scope="function")
async def client():

    async with AsyncClient(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.url,
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook],
        },
    ) as client:
        yield client
