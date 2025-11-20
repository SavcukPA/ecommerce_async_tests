import allure
import pytest
import services
from assertions.auth.login import positive_login_assertions


class TestsAuthorization:
    @allure.epic("Пользовательские операции")
    @allure.feature("Авторизация пользователя")
    @allure.story("Позитивные сценарии авторизации пользователя")
    @allure.parent_suite("API Тесты")
    @allure.suite("Тесты авторизации пользователя")
    @allure.sub_suite("Позитивные кейсы")
    @allure.title("Авторизация пользователя")
    @allure.label("owner", "QA Team")
    @pytest.mark.critical
    @pytest.mark.api
    @pytest.mark.auth
    @pytest.mark.login
    async def tests_login_user(self, client, user_register):

        payload = {
            "email": user_register["email"],
            "password": user_register["password"],
        }
        auth = services.Auth(client=client)
        response = await auth.login(payload=payload)
        positive_login_assertions(response=response, user_data=user_register)
