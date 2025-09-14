import allure
import re
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_site()

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_element(BaseLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_element(BaseLocators.ORDER_FEED_BUTTON)

    @allure.step("Перейти в личный кабинет")
    def go_to_personal_account(self):
        self.click_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        # Находим ингредиенты
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        
        # Проверяем, что ингредиенты найдены
        assert ingredients, "Ингредиенты должны быть найдены на странице"
        
        # Проверяем корректность индекса
        assert index < len(ingredients), f"Индекс {index} выходит за границы списка ингредиентов (доступно: {len(ingredients)})"
        
        # Кликаем на ингредиент по индексу
        ingredients[index].click()

    @allure.step("Проверить открытие модального окна ингредиента")
    def is_ingredient_modal_opened(self):
        # Проверяем основные локаторы модального окна
        modal_visible = self.is_element_visible(MainPageLocators.INGREDIENT_MODAL, timeout=3)
        overlay_visible = self.is_element_visible(MainPageLocators.MODAL_OVERLAY, timeout=3)
        content_visible = self.is_element_visible(MainPageLocators.MODAL_CONTENT, timeout=3)
        
        # Ищем любые элементы с классом modal
        all_modals = self.find_elements_by_class(MainPageLocators.MODAL_CLASS_NAME)
        visible_modals = self.get_visible_elements(all_modals)
        
        # Ищем элементы с высоким z-index
        high_z_elements = self.find_elements(MainPageLocators.HIGH_Z_INDEX_ELEMENTS)
        visible_high_z = self.get_visible_elements(high_z_elements)
        
        # Ищем элементы с role="dialog" или aria-modal="true"
        dialog_elements = self.find_elements(MainPageLocators.DIALOG_ELEMENTS)
        visible_dialogs = self.get_visible_elements(dialog_elements)
        
        # Ищем любые элементы, которые могут быть модальными окнами
        all_possible_modals = self.find_elements(MainPageLocators.POSSIBLE_MODAL_ELEMENTS)
        visible_possible_modals = self.get_visible_elements(all_possible_modals)
        
        return (modal_visible or overlay_visible or content_visible or 
                len(visible_modals) > 0 or len(visible_high_z) > 0 or 
                len(visible_dialogs) > 0 or len(visible_possible_modals) > 0)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name_in_modal(self):
        return self.get_text(MainPageLocators.INGREDIENT_NAME)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        # Кликаем по кнопке закрытия
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверить закрытие модального окна")
    def is_modal_closed(self):
        return not self.is_ingredient_modal_opened()

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, index=0):
        # Находим ингредиенты
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        
        assert ingredients and index < len(ingredients), "Ингредиенты должны быть найдены и индекс должен быть корректным"
        
        # Находим область конструктора
        constructor_area = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
        
        # Перетаскиваем ингредиент в конструктор
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredients[index], constructor_area).perform()

    @allure.step("Проверить увеличение счетчика ингредиента")
    def is_ingredient_counter_increased(self, index=0):
        counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER)
        assert counters, "Счетчики ингредиентов должны быть найдены"
        assert index < len(counters), f"Индекс {index} выходит за границы списка счетчиков (доступно: {len(counters)})"
        
        return counters[index].text != "0"

    @allure.step("Оформить заказ")
    def place_order(self):
        # Находим кнопку заказа
        order_button = self.find_element(MainPageLocators.ORDER_BUTTON)
        order_button.click()

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_opened(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)
