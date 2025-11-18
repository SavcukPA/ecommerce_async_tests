pytest_plugins = ("fixtures.auth",)

import os
import platform
import pytest

from clients.event_hooks import log_response_event_hook, log_request_event_hook
from config import settings
from httpx import AsyncClient
from utils.hooks import (
    generate_allure_report,
    copy_last_history,
)
from utils.setup_logger import setup_logging
from utils import paths

python_version = platform.python_version()
os_name = platform.system()

allure_results_dir = paths.allure_results_dir
allure_report_dir = paths.allure_report_dir


def pytest_configure(config):
    setup_logging(default_path=paths.logging_config_yaml_path)


def pytest_sessionfinish(session, exitstatus):
    """Вызывается после завершения всех тестов"""
    copy_last_history(
        allure_report_dir=allure_report_dir, allure_results_dir=allure_results_dir
    )
    generate_allure_report(
        path_allure_results_dir=allure_results_dir,
        path_allure_report_dir=allure_report_dir,
    )


@pytest.fixture(scope="session", autouse=True)
def generate_allure_environment():
    allure_env_path = os.path.join(
        os.getcwd(), "allure-results", "environment.properties"
    )
    os.makedirs(os.path.dirname(allure_env_path), exist_ok=True)
    with open(allure_env_path, "w", encoding="utf-8") as f:
        f.write("APP_VERSION=1.4.2\n")
        f.write(f"STAND={settings.environment.stand}\n")
        f.write(f"STAGE={settings.environment.stage}\n")
        f.write(f"API_URL={settings.http_client.host}\n")
        f.write(f"OS={os_name}\n")
        f.write(f"PYTHON_VERSION={python_version}\n")


@pytest.fixture(scope="function")
async def client():

    async with AsyncClient(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.host,
        event_hooks={
            "request": [log_request_event_hook],
            "request" "response": [log_response_event_hook],
        },
    ) as client:
        yield client
