from typing import Any

import allure
from httpx import AsyncClient, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

from clients.headers import Headers
from config import settings
from utils.helper import Helper


class BaseClient(Helper):

    headers = Headers

    def __init__(self, client: AsyncClient):
        self.client = client
        self.host = settings.http_client.host
        self.headers = Headers

    @allure.step("Отправка GET запроса: {url}")
    async def get(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        headers: dict | None = headers.basic,
    ) -> Response:
        response = await self.client.get(url, params=params, headers=headers)
        return await self.basic_assert(response=response)

    @allure.step("Отправка POST запроса: {url}")
    async def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        headers: dict | None = headers.basic,
    ) -> Response:
        return await self.client.post(
            url, json=json, data=data, files=files, headers=headers
        )

    @allure.step("Отправка PATCH запроса: {url}")
    async def patch(
        self,
        url: URL | str,
        json: Any | None = None,
        headers: dict | None = headers.basic,
    ) -> Response:
        return await self.client.patch(url, json=json, headers=headers)

    @allure.step("Отправка DELETE запроса: {url}")
    async def delete(
        self,
        url: URL | str,
        headers: dict | None = headers.basic,
    ) -> Response:
        return await self.client.delete(url, headers=headers)
