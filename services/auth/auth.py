import logging

import allure

from clients.base_client import BaseClient
from services.auth.endpoints import Endpoints

from faker import Faker

from services.auth.models.user_register import User
from services.auth.payloads import Payloads
from utils.helper import ResponseType

fake = Faker()

logger = logging.getLogger(__name__)


class Auth(BaseClient):

    __endpoints = Endpoints

    def __init__(self, client):
        super().__init__(client=client)
        self.payloads = Payloads

    @allure.step("Регистрация нового пользователя")
    async def register(
        self,
        payload: dict,
        expected_code=201,
        pydantic_model=User,
    ) -> dict | User:
        """
        Регистрация нового пользователя

        Args:
            payload: dict данные пользователя
            pydantic_model: Pydantic model для валидации
            expected_code: статус код ответа от сервера

        Returns:
            dict: Ответ API с данными пользователя

        Raises:
            AssertionError: Если статус код не 201
        """
        try:
            response = await self.post(
                url=f"{self.host}{self.__endpoints.register}",
                json=payload,
            )
            return await self.basic_assert(
                response=response,
                expected_code=expected_code,
                pydantic_model=pydantic_model,
            )

        except Exception as e:
            logger.error(f"User registration failed: {e}")
            raise

    @allure.step("Авторизация пользователя")
    async def login(self, payload: dict, expected_code=204):
        try:
            logger.debug(f"Login payload: {payload}")
            logger.debug(f"Login headers: {self.headers.form_urlencoded}")
            logger.debug(f"Full URL: {self.host}{self.__endpoints.login}")
            response = await self.post(
                url=f"{self.host}{self.__endpoints.login}",
                data=payload,
                headers=self.headers.form_urlencoded,
            )
            await self.basic_assert(
                response=response,
                expected_code=expected_code,
            )
            return response
        except Exception as e:
            logger.error(f"User login failed: {e}")
            raise

    @allure.step("Регистрация нового пользователя")
    async def register_random_user(
        self,
        expected_code=201,
        pydantic_model=User,
    ) -> dict | User:
        """
        Регистрация случайного нового пользователя.
        Используется для генерации данных.

        Args:
            pydantic_model: Pydantic-модель для валидации.
            expected_code: Статус-код ответа от сервера.
        Returns:
            dict: Ответ API с данными пользователя.

        Raises:
            AssertionError: Если статус-код не равен 201.
        """
        try:
            response = await self.post(
                url=f"{self.host}{self.__endpoints.register}",
                json=self.payloads.random_user,
            )
            response = await self.basic_assert(
                response=response,
                expected_code=expected_code,
                pydantic_model=pydantic_model,
                response_type=ResponseType.JSON,
            )
            response["password"] = self.payloads.random_user["password"]
            return response

        except Exception as e:
            logger.error(f"User registration failed: {e}")
            raise
