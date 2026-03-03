import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import utils.paths as paths


@pytest.fixture(scope="session")
def chrome_options():

    prefs = {
        "download.default_directory": str(paths.download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    options = Options()
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    return options


@pytest.fixture(scope="function")
def driver(chrome_options):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot_{timestamp}",
        attachment_type=allure.attachment_type.PNG,
    )

    driver.quit()
