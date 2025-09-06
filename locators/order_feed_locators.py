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
