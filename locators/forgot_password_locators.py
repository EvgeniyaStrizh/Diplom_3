from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    BACK_TO_LOGIN_LINK = (By.XPATH, "//a[text()='Вспомнили пароль?']")