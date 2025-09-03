from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заказы
    ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'order-item')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'order-number')]")
    
    # Счетчики
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'total-orders')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'today-orders')]")
    
    # Статусы заказов
    IN_PROGRESS_ORDERS = (By.XPATH, "//div[contains(@class, 'in-progress')]")
    DONE_ORDERS = (By.XPATH, "//div[contains(@class, 'done')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.CLASS_NAME, "modal")
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'order-details')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'close-button')]")
