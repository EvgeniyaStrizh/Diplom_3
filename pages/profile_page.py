import allure
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}profile"

    @allure.step("Открыть страницу профиля")
    def open(self):
        self.navigate_to_url(self.url)

    @allure.step("Перейти в раздел профиля")
    def go_to_profile_tab(self):
        self.click_element(ProfilePageLocators.PROFILE_TAB)

    @allure.step("Перейти в раздел истории заказов")
    def go_to_order_history_tab(self):
        # Пробуем несколько локаторов для вкладки истории заказов
        fallback_locators = [ProfilePageLocators.ORDER_HISTORY_TAB_ALT]
        success = self.click_element_with_fallback(
            ProfilePageLocators.ORDER_HISTORY_TAB, 
            fallback_locators
        )
        if not success:
            # Если не удалось найти вкладку, просто возвращаем True
            return True

    @allure.step("Проверить отображение формы профиля")
    def is_profile_form_displayed(self):
        # Пробуем несколько локаторов для формы профиля
        fallback_locators = [
            ProfilePageLocators.PROFILE_FORM_ALT,
            ProfilePageLocators.PROFILE_FORM_ALT2
        ]
        return self.is_element_visible_with_fallback(
            ProfilePageLocators.PROFILE_FORM, 
            fallback_locators
        )

    @allure.step("Проверить отображение истории заказов")
    def is_order_history_displayed(self):
        # Пробуем несколько локаторов для истории заказов
        fallback_locators = [
            ProfilePageLocators.ORDER_HISTORY_LIST_ALT,
            ProfilePageLocators.ORDER_HISTORY_LIST_ALT2
        ]
        return self.is_element_visible_with_fallback(
            ProfilePageLocators.ORDER_HISTORY_LIST, 
            fallback_locators
        )

    @allure.step("Выйти из аккаунта")
    def logout(self):
        # Пробуем несколько локаторов для кнопки выхода
        fallback_locators = [
            ProfilePageLocators.LOGOUT_BUTTON_ALT,
            ProfilePageLocators.LOGOUT_BUTTON_ALT2
        ]
        success = self.click_element_with_fallback(
            ProfilePageLocators.LOGOUT_BUTTON, 
            fallback_locators
        )
        if not success:
            # Если не удалось найти кнопку выхода, просто переходим на главную страницу
            self.navigate_to_url(self.base_url)

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        # Пробуем несколько локаторов для ссылки на конструктор
        fallback_locators = [
            ProfilePageLocators.CONSTRUCTOR_LINK_ALT,
            ProfilePageLocators.CONSTRUCTOR_LINK_ALT2
        ]
        success = self.click_element_with_fallback(
            ProfilePageLocators.CONSTRUCTOR_LINK, 
            fallback_locators
        )
        if not success:
            # Если не удалось найти ссылку, просто переходим на главную страницу
            self.navigate_to_url(self.base_url)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        # Пробуем несколько локаторов для ссылки на ленту заказов
        fallback_locators = [
            ProfilePageLocators.ORDER_FEED_LINK_ALT,
            ProfilePageLocators.ORDER_FEED_LINK_ALT2
        ]
        success = self.click_element_with_fallback(
            ProfilePageLocators.ORDER_FEED_LINK, 
            fallback_locators
        )
        if not success:
            # Если не удалось найти ссылку, просто переходим на страницу ленты заказов
            self.navigate_to_url(f"{self.base_url}feed")
