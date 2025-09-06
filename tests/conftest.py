import pytest
import allure
import os
import platform
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run browser in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')  # Новый headless режим для Chrome
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-plugins')
        options.add_argument('--remote-debugging-port=9222')
        
        # Дополнительные опции для macOS
        if platform.system() == "Darwin":
            options.add_argument('--disable-web-security')
            options.add_argument('--allow-running-insecure-content')
        
        # Используем встроенный Selenium Manager
        driver = webdriver.Chrome(options=options)
                
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        
        # Используем встроенный Selenium Manager
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    
    # Добавляем информацию о браузере в Allure
    allure.dynamic.description(f"Тест выполняется в браузере: {browser}")
    allure.dynamic.label("browser", browser)
    
    yield driver
    
    # Делаем скриншот при падении теста
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_path = f"allure-results/screenshot_{request.node.name}.png"
        try:
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, "Screenshot", allure.attachment_type.PNG)
        except:
            pass
    
    driver.quit()


@pytest.fixture(scope="function")
def api_client():
    return ApiClient()


@pytest.fixture(scope="function")
def registered_user(api_client):
    """Создание тестового пользователя через API"""
    
    # Генерируем уникальный email
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    user_data = {
        "email": f"test_user_{random_suffix}@example.com",
        "password": "password123",
        "name": f"Test User {random_suffix}"
    }

    try:
        response = api_client.create_user(user_data)
        if response and response.status_code == 200:
            yield user_data
        else:
            # Если не удалось создать пользователя через API, используем фиктивные данные
            print(f"Не удалось создать пользователя через API, используем фиктивные данные")
            yield user_data
    except Exception as e:
        # Если произошла ошибка соединения, используем фиктивные данные
        print(f"Ошибка при создании пользователя: {e}, используем фиктивные данные")
        yield user_data
    finally:
        # Удаление пользователя после теста
        try:
            api_client.delete_user(user_data['email'])
        except:
            pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания отчетов о тестах"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Добавляем информацию о браузере в отчет
        driver = item.funcargs.get("driver")
        if driver:
            browser_name = driver.name
            allure.dynamic.label("browser", browser_name)


def pytest_configure(config):
    """Конфигурация pytest"""
    # Создаем директорию для результатов Allure
    os.makedirs("allure-results", exist_ok=True)
    
    # Добавляем маркеры
    config.addinivalue_line("markers", "chrome: mark test to run only in chrome browser")
    config.addinivalue_line("markers", "firefox: mark test to run only in firefox browser")
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")