from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заказы - более гибкие локаторы
    ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'order') or contains(@class, 'Order') or contains(@class, 'order-item')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'order-number') or contains(@class, 'number') or contains(@class, 'id')]")
    
    # Счетчики - более гибкие локаторы
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'total') or contains(@class, 'all') or contains(text(), 'всего') or contains(text(), 'все')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'today') or contains(@class, 'сегодня') or contains(text(), 'сегодня') or contains(text(), 'today')]")
    
    # Статусы заказов
    IN_PROGRESS_ORDERS = (By.XPATH, "//div[contains(@class, 'in-progress')]")
    DONE_ORDERS = (By.XPATH, "//div[contains(@class, 'done')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.CLASS_NAME, "modal")
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'order-details')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'close-button')]")
    
    # Fallback локаторы для счетчиков
    TOTAL_ORDERS_FALLBACK = [
        (By.XPATH, "//p[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]"),
        (By.XPATH, "//span[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]"),
        (By.XPATH, "//div[contains(text(), 'всего') or contains(text(), 'все') or contains(text(), 'total')]")
    ]
    
    TODAY_ORDERS_FALLBACK = [
        (By.XPATH, "//p[contains(text(), 'сегодня') or contains(text(), 'today')]"),
        (By.XPATH, "//span[contains(text(), 'сегодня') or contains(text(), 'today')]"),
        (By.XPATH, "//div[contains(text(), 'сегодня') or contains(text(), 'today')]")
    ]
    
    IN_PROGRESS_ORDERS_FALLBACK = [
        (By.XPATH, "//div[contains(@class, 'in-progress') or contains(@class, 'progress') or contains(@class, 'работа')]"),
        (By.XPATH, "//div[contains(text(), 'в работе') or contains(text(), 'готовится') or contains(text(), 'готовится')]"),
        (By.XPATH, "//div[contains(@class, 'order') and contains(@class, 'active')]")
    ]