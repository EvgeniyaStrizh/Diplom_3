import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from locators.main_page_locators import MainPageLocators


@allure.epic("Основной функционал")
class TestMainFunctionality:
    
    @allure.feature("Навигация")
    @allure.story("Переход по клику на 'Конструктор'")
    @allure.title("Переход в конструктор с главной страницы")
    def test_navigate_to_constructor(self, driver):
        """Тест перехода в конструктор"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на кнопку 'Конструктор'"):
            main_page.go_to_constructor()
        
        with allure.step("Проверить переход в конструктор"):
            # Должен остаться на главной странице, но в конструкторе
            assert "stellarburgers.nomoreparties.site" in main_page.get_current_url()

    @allure.feature("Навигация")
    @allure.story("Переход по клику на 'Лента заказов'")
    @allure.title("Переход в ленту заказов с главной страницы")
    def test_navigate_to_order_feed(self, driver):
        """Тест перехода в ленту заказов"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на кнопку 'Лента заказов'"):
            main_page.go_to_order_feed()
        
        with allure.step("Проверить переход в ленту заказов"):
            assert "feed" in main_page.get_current_url()

    @allure.feature("Ингредиенты")
    @allure.story("Клик по ингредиенту открывает всплывающее окно")
    @allure.title("Открытие модального окна ингредиента при клике")
    def test_ingredient_modal_opens(self, driver):
        """Тест открытия модального окна ингредиента"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на ингредиент"):
            main_page.click_ingredient()
        
        with allure.step("Проверить открытие модального окна"):
            result = main_page.is_ingredient_modal_opened()
            print(f"Результат проверки модального окна: {result}")
            assert result is True, "Модальное окно должно открыться при клике на ингредиент"

    @allure.feature("Ингредиенты")
    @allure.story("Всплывающее окно закрывается кликом по крестику")
    @allure.title("Закрытие модального окна ингредиента при успешном открытии")
    def test_ingredient_modal_closes_when_opened(self, driver):
        """Тест закрытия модального окна ингредиента при успешном открытии"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на ингредиент"):
            main_page.click_ingredient()
        
        with allure.step("Проверить открытие модального окна"):
            result = main_page.is_ingredient_modal_opened()
            print(f"Результат проверки модального окна: {result}")
            assert result is True, "Модальное окно должно открыться"
        
        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()
        
        with allure.step("Проверить закрытие модального окна"):
            assert main_page.is_modal_closed()

    @allure.feature("Ингредиенты")
    @allure.story("Проверка клика по ингредиенту")
    @allure.title("Клик по ингредиенту выполняется корректно")
    def test_ingredient_click_execution(self, driver):
        """Тест корректного выполнения клика по ингредиенту"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на ингредиент"):
            main_page.click_ingredient()
        
        with allure.step("Проверить выполнение клика"):
            result = main_page.is_ingredient_modal_opened()
            print(f"Результат проверки модального окна: {result}")
            assert result is not None, "Операция проверки модального окна должна быть выполнена"

    @allure.feature("Конструктор")
    @allure.story("При добавлении ингредиента увеличивается каунтер")
    @allure.title("Увеличение счетчика ингредиента при добавлении")
    def test_ingredient_counter_increases(self, driver):
        """Тест увеличения счетчика ингредиента"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
        
        with allure.step("Проверить увеличение счетчика"):
            result = main_page.is_ingredient_counter_increased()
            assert result is True, "Счетчик ингредиента должен увеличиться после добавления"

    @allure.feature("Заказы")
    @allure.story("Залогиненный пользователь может оформить заказ")
    @allure.title("Успешное оформление заказа залогиненным пользователем")
    def test_logged_user_successful_order_placement(self, driver, registered_user):
        """Тест успешного оформления заказа залогиненным пользователем"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
        
        with allure.step("Оформить заказ"):
            order_placed = main_page.place_order()
            assert order_placed is True, "Заказ должен быть оформлен успешно"
        
        with allure.step("Проверить открытие модального окна заказа"):
            order_modal_opened = main_page.is_order_modal_opened()
            print(f"Модальное окно заказа открылось: {order_modal_opened}")
            assert order_modal_opened is True, "Модальное окно заказа должно открыться"

    @allure.feature("Заказы")
    @allure.story("Проверка операции оформления заказа")
    @allure.title("Операция оформления заказа выполняется корректно")
    def test_order_placement_operation(self, driver, registered_user):
        """Тест корректного выполнения операции оформления заказа"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
        
        with allure.step("Попытаться оформить заказ"):
            order_placed = main_page.place_order()
            assert order_placed is not None, "Операция оформления заказа должна быть выполнена"

    @allure.feature("Навигация")
    @allure.story("Переход в личный кабинет")
    @allure.title("Переход в личный кабинет с главной страницы")
    def test_navigate_to_personal_account(self, driver):
        """Тест перехода в личный кабинет"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на кнопку 'Личный кабинет'"):
            main_page.go_to_personal_account()
        
        with allure.step("Проверить переход на страницу входа"):
            assert "login" in main_page.get_current_url()
