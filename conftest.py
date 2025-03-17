import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # Добавляет опцию командной строки --browser для выбора браузера.
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def driver(request):
    # Фикстура для инициализации WebDriver с поддержкой Chrome и Firefox.
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
