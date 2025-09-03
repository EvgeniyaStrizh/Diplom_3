from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Профиль
    PROFILE_TAB = (By.XPATH, "//a[text()='Профиль']")
    PROFILE_FORM = (By.XPATH, "//form[contains(@class, 'profile-form')]")
    
    # История заказов
    ORDER_HISTORY_TAB = (By.XPATH, "//a[text()='История заказов']")
    ORDER_HISTORY_LIST = (By.XPATH, "//div[contains(@class, 'order-history')]")
    
    # Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Навигация
    CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, "//a[text()='Лента заказов']")
