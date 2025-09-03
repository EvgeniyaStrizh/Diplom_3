import allure
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}login"

    @allure.step("Открыть страницу входа")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать ссылку восстановления пароля")
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Нажать ссылку регистрации")
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Проверить наличие сообщения об ошибке")
    def is_error_message_displayed(self):
        return self.is_element_visible(LoginPageLocators.ERROR_MESSAGE)