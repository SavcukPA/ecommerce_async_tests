import logging
import allure

from enum import Enum
from httpx import Response

logger = logging.getLogger(__name__)


class ResponseType(Enum):

    JSON = "json"
    PYDANTIC_MODEL = "pydantic_model"


class Helper:

    @staticmethod
    async def basic_assert(
        response: Response,
        expected_code: int = 200,
        pydantic_model=None,
        response_type: ResponseType = ResponseType.JSON,
    ):
        """
        Метод для валидации HTTP-ответов в тестах API.

        Выполняет базовые проверки ответа и возвращает данные в указанном формате.
        Интегрирован с Allure-отчетами и системой логирования.

        Parameters:
        -----------
        response : Response
            HTTP-ответ от клиента (httpx.Response/requests.Response)

        expected_code : int, optional
            Ожидаемый HTTP статус-код (по умолчанию 200)

        pydantic_model : BaseModel, optional
            Pydantic-модель для валидации структуры JSON-ответа.
            Если передан, выполняется проверка соответствия ответа модели.

        response_type : ResponseType, optional
            Тип возвращаемых данных (по умолчанию ResponseType.JSON):
            - ResponseType.JSON: возвращает распарсенный JSON как словарь/список
            - ResponseType.PYDANTIC_MODEL: возвращает инстанс Pydantic-модели
            - Другие типы: возвращает исходный объект response

        Returns:
        --------
            Данные в формате, указанном в response_type:
            - dict/list для ResponseType.JSON
            - BaseModel для ResponseType.PYDANTIC_MODEL
            - Response для других типов

        Raises:
        -------
        AssertionError
            - Если фактический статус-код не совпадает с ожидаемым
            - Если ответ не соответствует Pydantic-модели (при её указании)
        """
        actual_code = response.status_code
        reason = response.reason_phrase or "No reason phrase"

        if actual_code != expected_code:
            error_msg = (
                f"Status code assertion failed.\n"
                f"Expected status code: {expected_code}\n"
                f"Actual: {actual_code} {reason}\n"
                f"URL: {response.url}\n"
                f"Method: {response.request.method}\n"
                f"Response text: {response.text}..."
            )

            allure.attach(
                body=response.text,
                name=f"Response Body {actual_code}",
                attachment_type=allure.attachment_type.TEXT,
            )
            logger.error(error_msg)
            raise AssertionError(error_msg)

        logger.info(f"Status code check passed: {actual_code} for {response.url}")

        if response.status_code == 204:
            logger.info("Empty response (204), returning raw response")
            return response

        if pydantic_model:
            pydantic_model.model_validate(response.json())

        if response_type == ResponseType.PYDANTIC_MODEL:
            return pydantic_model(**response.json())
        elif response_type == ResponseType.JSON:
            return response.json()
        else:
            return response
