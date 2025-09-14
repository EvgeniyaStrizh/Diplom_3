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
    
    # Альтернативные локаторы для более надежного поиска
    PROFILE_TAB_ALT = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    PROFILE_FORM_ALT = (By.XPATH, "//form")
    PROFILE_FORM_ALT2 = (By.XPATH, "//div[contains(@class, 'profile')]")
    
    ORDER_HISTORY_TAB_ALT = (By.XPATH, "//a[contains(text(), 'История') or contains(text(), 'заказов')]")
    ORDER_HISTORY_LIST_ALT = (By.XPATH, "//div[contains(@class, 'order')]")
    ORDER_HISTORY_LIST_ALT2 = (By.XPATH, "//ul[contains(@class, 'order')]")
    
    LOGOUT_BUTTON_ALT = (By.XPATH, "//button[contains(text(), 'Выход')]")
    LOGOUT_BUTTON_ALT2 = (By.XPATH, "//button[contains(@class, 'logout')]")
    
    CONSTRUCTOR_LINK_ALT = (By.XPATH, "//a[contains(text(), 'Конструктор')]")
    CONSTRUCTOR_LINK_ALT2 = (By.XPATH, "//a[contains(@href, 'constructor') or contains(@href, '/')]")
    
    ORDER_FEED_LINK_ALT = (By.XPATH, "//a[contains(text(), 'Лента') or contains(text(), 'заказов')]")
    ORDER_FEED_LINK_ALT2 = (By.XPATH, "//a[contains(@href, 'feed')]")