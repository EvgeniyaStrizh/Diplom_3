from selenium.webdriver.common.by import By


class OrderLocators:
    # Локаторы для конструктора
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "constructor-area")
    CONSTRUCTOR_AREA_ALT = (By.XPATH, "//div[contains(@class, 'constructor')]")
    CONSTRUCTOR_AREA_ALT2 = (By.XPATH, "//div[contains(@class, 'Constructor')]")
    CONSTRUCTOR_AREA_ALT3 = (By.XPATH, "//div[contains(@class, 'burger-constructor')]")
    CONSTRUCTOR_AREA_ALT4 = (By.XPATH, "//div[contains(@class, 'BurgerConstructor')]")
    
    # Локаторы для кнопки заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'заказ') or contains(text(), 'Оформить') or contains(text(), 'Оформить заказ') or contains(@class, 'order') or contains(@class, 'button')]")
    ORDER_BUTTON_ALT = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_BUTTON_ALT2 = (By.XPATH, "//button[contains(text(), 'заказ')]")
    ORDER_BUTTON_ALT3 = (By.XPATH, "//button[contains(@class, 'order')]")
    ORDER_BUTTON_ALT4 = (By.XPATH, "//button[contains(@class, 'Order')]")
    
    # Локаторы для модального окна заказа
    ORDER_MODAL = (By.CLASS_NAME, "modal")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'order-number')]")
