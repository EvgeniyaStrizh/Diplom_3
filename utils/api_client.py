import requests
import json


class ApiClient:
    def __init__(self):
        self.base_url = "https://stellarburgers.nomoreparties.site/api"
        self.session = requests.Session()
        self.access_token = None

    def create_user(self, user_data):
        """Создание пользователя"""
        url = f"{self.base_url}/auth/register"
        response = self.session.post(url, json=user_data)
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('accessToken')
        return response

    def login_user(self, user_data):
        """Авторизация пользователя"""
        url = f"{self.base_url}/auth/login"
        response = self.session.post(url, json=user_data)
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('accessToken')
        return response

    def delete_user(self, email):
        """Удаление пользователя"""
        if self.access_token:
            url = f"{self.base_url}/auth/user"
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = self.session.delete(url, headers=headers)
            return response
        return None

    def get_user_info(self):
        """Получение информации о пользователе"""
        if self.access_token:
            url = f"{self.base_url}/auth/user"
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = self.session.get(url, headers=headers)
            return response
        return None

    def create_order(self, ingredients):
        """Создание заказа"""
        if self.access_token:
            url = f"{self.base_url}/orders"
            headers = {'Authorization': f'Bearer {self.access_token}'}
            data = {'ingredients': ingredients}
            response = self.session.post(url, json=data, headers=headers)
            return response
        return None

    def get_orders(self):
        """Получение заказов пользователя"""
        if self.access_token:
            url = f"{self.base_url}/orders"
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = self.session.get(url, headers=headers)
            return response
        return None
