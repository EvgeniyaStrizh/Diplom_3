import allure
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}profile"

    @allure.step("Открыть страницу профиля")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Перейти в раздел профиля")
    def go_to_profile_tab(self):
        self.click_element(ProfilePageLocators.PROFILE_TAB)

    @allure.step("Перейти в раздел истории заказов")
    def go_to_order_history_tab(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)

    @allure.step("Проверить отображение формы профиля")
    def is_profile_form_displayed(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_FORM)

    @allure.step("Проверить отображение истории заказов")
    def is_order_history_displayed(self):
        return self.is_element_visible(ProfilePageLocators.ORDER_HISTORY_LIST)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_element(ProfilePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_element(ProfilePageLocators.ORDER_FEED_LINK)
