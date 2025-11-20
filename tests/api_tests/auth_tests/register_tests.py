import allure
import pytest
import data
import assertions

import services
from utils.generators import generators


class TestsUserRegister:

    @allure.epic("Пользовательские операции")
    @allure.feature("Регистрация пользователя")
    @allure.story("Позитивные сценарии регистрации пользователя")
    @allure.parent_suite("API Тесты")
    @allure.suite("Тесты регистрации пользователя")
    @allure.sub_suite("Позитивные кейсы")
    @allure.label("owner", "QA Team")
    @pytest.mark.critical
    @pytest.mark.register
    @pytest.mark.parametrize(
        "user_test_cases", data.positive_test_cases, ids=data.positive_test_cases_ids
    )
    async def tests_user_register_positive(self, client, user_test_cases):
        allure.dynamic.title(user_test_cases["metadata"]["title"])
        auth = services.Auth(client=client)
        response = await auth.register(
            payload=user_test_cases["data"],
            expected_code=user_test_cases["metadata"]["expected_status_code"],
            pydantic_model=user_test_cases["metadata"]["pydantic_model"],
        )
        assertions.register.positive_register_assertions(
            test_case=user_test_cases, response=response
        )

    @allure.epic("Пользовательские операции")
    @allure.feature("Регистрация пользователя")
    @allure.story("Негативные сценарии регистрации пользователя")
    @allure.parent_suite("API Тесты")
    @allure.suite("Тесты регистрации пользователя")
    @allure.sub_suite("Негативные кейсы")
    @allure.label("owner", "QA Team")
    @pytest.mark.critical
    @pytest.mark.register
    @pytest.mark.parametrize(
        "user_test_cases", data.negative_test_cases, ids=data.negative_test_cases_ids
    )
    async def tests_user_register_negative(self, client, user_test_cases):
        allure.dynamic.title(user_test_cases["metadata"]["title"])
        auth = services.Auth(client=client)
        response = await auth.register(
            payload=user_test_cases["data"],
            expected_code=user_test_cases["metadata"]["expected_status_code"],
            pydantic_model=user_test_cases["metadata"]["pydantic_model"],
        )
        assertions.register.negative_register_assertion(
            response=response, test_case=user_test_cases
        )

    @allure.epic("Пользовательские операции")
    @allure.feature("Регистрация пользователя")
    @allure.story("Негативные сценарии регистрации пользователя")
    @allure.parent_suite("API Тесты")
    @allure.suite("Тесты регистрации пользователя")
    @allure.sub_suite("Негативные кейсы")
    @allure.title("Регистрация уже существующего пользователя")
    @allure.label("owner", "QA Team")
    @pytest.mark.critical
    @pytest.mark.register
    @pytest.mark.auth
    async def tests_register_already_exists(self, client, user_register):
        auth = services.Auth(
            client=client,
        )
        user_register.pop("id", None)
        user_register["password"] = generators.faker_en.password(length=32)
        response = await auth.register(
            payload=user_register,
            expected_code=data.specific_cases["tests_register_already_exists"][
                "metadata"
            ]["expected_status_code"],
            pydantic_model=data.specific_cases["tests_register_already_exists"][
                "metadata"
            ]["pydantic_model"],
        )
        assertions.register.negative_register_assertion(
            response=response,
            test_case=data.specific_cases["tests_register_already_exists"],
        )
