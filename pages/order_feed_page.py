import allure
import re
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{self.base_url}feed"

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.navigate_to_url(self.url)

    @allure.step("Кликнуть на заказ")
    def click_order(self, index=0):
        orders = self.find_elements(OrderFeedLocators.ORDER_ITEM)
        assert orders, "Заказы должны быть найдены"
        assert index < len(orders), f"Индекс {index} выходит за границы списка заказов (доступно: {len(orders)})"
        orders[index].click()

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_opened(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получить детали заказа")
    def get_order_details(self):
        return self.get_text(OrderFeedLocators.ORDER_DETAILS)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element(OrderFeedLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        element = self.find_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        text = element.text
        # Извлекаем число из текста
        numbers = re.findall(r'\d+', text)
        assert numbers, "Не удалось найти число в счетчике общего количества заказов"
        return numbers[0]

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        text = element.text
        # Извлекаем число из текста
        numbers = re.findall(r'\d+', text)
        assert numbers, "Не удалось найти число в счетчике заказов за сегодня"
        return numbers[0]

    @allure.step("Проверить наличие заказов в работе")
    def get_in_progress_orders(self):
        return self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)

    @allure.step("Проверить наличие выполненных заказов")
    def get_done_orders(self):
        return self.find_elements(OrderFeedLocators.DONE_ORDERS)

    @allure.step("Получить список заказов")
    def get_orders_list(self):
        """Получить список всех заказов на странице"""
        return self.find_elements(OrderFeedLocators.ORDER_ITEM)

    @allure.step("Проверить отображение заказа пользователя")
    def is_user_order_displayed(self, order_number):
        orders = self.find_elements(OrderFeedLocators.ORDER_NUMBER)
        order_numbers = [order.text for order in orders]
        return order_number in order_numbers
