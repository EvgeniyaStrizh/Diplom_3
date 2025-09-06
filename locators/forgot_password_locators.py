from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    BACK_TO_LOGIN_LINK = (By.XPATH, "//a[text()='Вспомнили пароль?']")
    
    # Альтернативные локаторы для более надежного поиска
    EMAIL_FIELD_ALT = (By.XPATH, "//input[@type='email']")
    EMAIL_FIELD_ALT2 = (By.XPATH, "//input[contains(@placeholder, 'email') or contains(@placeholder, 'Email')]")
    RESTORE_BUTTON_ALT = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    RESTORE_BUTTON_ALT2 = (By.XPATH, "//button[@type='submit']")
    PASSWORD_FIELD_ALT = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BUTTON_ALT = (By.XPATH, "//div[contains(@class, 'input__icon') or contains(@class, 'icon')]")
    SHOW_PASSWORD_BUTTON_ALT2 = (By.XPATH, "//button[contains(@class, 'input__icon')]")
    BACK_TO_LOGIN_LINK_ALT = (By.XPATH, "//a[contains(text(), 'Вспомнили') or contains(text(), 'пароль')]")
    BACK_TO_LOGIN_LINK_ALT2 = (By.XPATH, "//a[contains(@href, 'login')]")