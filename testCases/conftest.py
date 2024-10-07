import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        ops = webdriver.ChromeOptions()
        ops.add_argument('--headless')
        ops.add_argument('--disable-gpu')
        ops.add_argument('--disable-notifications')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), options=ops))
        driver.maximize_window()
        yield driver
        driver.quit()
    elif browser == 'firefox':
        ops = webdriver.FirefoxOptions()
        ops.add_argument('--headless')
        ops.add_argument('--disable-notifications')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", default="false")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_results_summary(prefix, summary, *args):
    prefix.extend([
        ("Tester", "Rudra.Singh"),
        ("Project Name", "Scrive Document Signature"),
    ])

@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
