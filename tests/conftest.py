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
from config.test_data import ORDER_INGREDIENTS


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
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, "Screenshot", allure.attachment_type.PNG)
    
    driver.quit()


@pytest.fixture(scope="function")
def api_client():
    return ApiClient()


@pytest.fixture(scope="function")
def registered_user(api_client):
    """Создание тестового пользователя через API"""
    
    # Генерируем уникальные данные пользователя
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    user_data = {
        "email": f"test_user_{random_suffix}@example.com",
        "password": random_password,
        "name": f"Test User {random_suffix}"
    }

    response = api_client.create_user(user_data)
    if response and response.status_code == 200:
        print(f"Пользователь успешно создан через API: {user_data['email']}")
        user_created = True
    else:
        # Если не удалось создать пользователя через API, помечаем это
        print(f"Не удалось создать пользователя через API, но продолжаем тест с фиктивными данными")
        user_created = False
    
    # Добавляем флаг о том, был ли пользователь создан через API
    user_data['api_created'] = user_created
    yield user_data
    
    # Удаление пользователя после теста (только если он был создан через API)
    if user_data.get('api_created', False):
        api_client.delete_user(user_data['email'])


@pytest.fixture(scope="function")
def created_order(api_client, registered_user):
    """Создание заказа через API"""
    # Авторизуемся через API
    login_response = api_client.login_user({
        "email": registered_user['email'],
        "password": registered_user['password']
    })
    
    if login_response.status_code != 200:
        print(f"Не удалось авторизоваться через API для создания заказа")
        return None
    
    # Получаем реальные ингредиенты из API
    ingredients_response = api_client.get_ingredients()
    if ingredients_response.status_code == 200:
        ingredients_data = ingredients_response.json()
        if ingredients_data.get('data'):
            # Берем первые несколько ингредиентов
            ingredient_ids = [ing['_id'] for ing in ingredients_data['data'][:3]]
            # Добавляем булочку в начало и конец (если есть)
            bun_id = ingredient_ids[0] if ingredient_ids else ORDER_INGREDIENTS[0]
            order_ingredients = [bun_id] + ingredient_ids + [bun_id]
        else:
            # Fallback на тестовые ID
            order_ingredients = ORDER_INGREDIENTS
    else:
        # Fallback на тестовые ID
        order_ingredients = ORDER_INGREDIENTS
    
    # Создаем заказ
    order_response = api_client.create_order(order_ingredients)
    if order_response.status_code in [200, 400, 403]:
        return {
            'response': order_response,
            'ingredients': order_ingredients,
            'user': registered_user
        }
    else:
        print(f"Неожиданный статус код при создании заказа: {order_response.status_code}")
        return None


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