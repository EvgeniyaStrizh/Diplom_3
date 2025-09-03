import allure
from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}forgot-password"

    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step("Нажать кнопку восстановления")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Нажать кнопку показа/скрытия пароля")
    def click_show_password_button(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить активность поля пароля")
    def is_password_field_active(self):
        password_field = self.find_element(ForgotPasswordLocators.PASSWORD_FIELD)
        return password_field.get_attribute("type") == "text"

    @allure.step("Восстановить пароль")
    def restore_password(self, email):
        self.enter_email(email)
        self.click_restore_button()

    @allure.step("Вернуться к странице входа")
    def go_back_to_login(self):
        self.click_element(ForgotPasswordLocators.BACK_TO_LOGIN_LINK)