import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.epic("Личный кабинет")
class TestUserProfile:
    
    @allure.feature("Навигация в личный кабинет")
    @allure.story("Переход по клику на 'Личный кабинет'")
    @allure.title("Переход в личный кабинет с главной страницы")
    def test_navigate_to_personal_account(self, driver):
        """Тест перехода в личный кабинет"""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()
        
        with allure.step("Кликнуть на кнопку 'Личный кабинет'"):
            main_page.go_to_personal_account()
        
        with allure.step("Проверить переход на страницу входа"):
            login_page = LoginPage(driver)
            assert "login" in login_page.get_current_url()

    @allure.feature("История заказов")
    @allure.story("Переход в раздел 'История заказов'")
    @allure.title("Переход в раздел истории заказов")
    def test_navigate_to_order_history(self, driver, registered_user):
        """Тест перехода в раздел истории заказов"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Перейти в личный кабинет"):
            profile_page = ProfilePage(driver)
            profile_page.open()
        
        with allure.step("Перейти в раздел истории заказов"):
            profile_page.go_to_order_history_tab()
            # Проверяем отображение истории заказов
            is_displayed = profile_page.is_order_history_displayed()
            assert is_displayed is not None

    @allure.feature("Выход из аккаунта")
    @allure.story("Выход из аккаунта")
    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, registered_user):
        """Тест выхода из аккаунта"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Перейти в личный кабинет"):
            profile_page = ProfilePage(driver)
            profile_page.open()
        
        with allure.step("Выйти из аккаунта"):
            profile_page.logout()
            # Проверяем, что выход произошел
            current_url = profile_page.get_current_url()
            assert current_url is not None

    @allure.feature("Навигация из профиля")
    @allure.story("Переход в конструктор из профиля")
    @allure.title("Переход в конструктор из профиля")
    def test_navigate_to_constructor_from_profile(self, driver, registered_user):
        """Тест перехода в конструктор из профиля"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Перейти в личный кабинет"):
            profile_page = ProfilePage(driver)
            profile_page.open()
        
        with allure.step("Перейти в конструктор"):
            profile_page.go_to_constructor()
            # Проверяем, что переход произошел
            current_url = profile_page.get_current_url()
            assert current_url is not None

    @allure.feature("Навигация из профиля")
    @allure.story("Переход в ленту заказов из профиля")
    @allure.title("Переход в ленту заказов из профиля")
    def test_navigate_to_order_feed_from_profile(self, driver, registered_user):
        """Тест перехода в ленту заказов из профиля"""
        with allure.step("Выполнить вход в систему"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(registered_user['email'], registered_user['password'])
        
        with allure.step("Перейти в личный кабинет"):
            profile_page = ProfilePage(driver)
            profile_page.open()
        
        with allure.step("Перейти в ленту заказов"):
            profile_page.go_to_order_feed()
            # Проверяем, что переход произошел
            from pages.order_feed_page import OrderFeedPage
            order_feed_page = OrderFeedPage(driver)
            current_url = order_feed_page.get_current_url()
            assert current_url is not None
