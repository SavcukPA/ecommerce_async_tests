import time
import logging

from pprint import pprint

import allure
from requests import Response
from config import settings
from utils.base_helper_func import decode_jwt_token, extract_secure_token

logger = logging.getLogger(__name__)


@allure.step("Проверка времени истечения токена")
def token_lifetime(decode_token):
    """
    Проверяет, что время жизни JWT-токена соответствует значению,
    указанному в settings.token.exp.

    Допускается отклонение назад до 20 секунд.

    Параметры:
        decode_token (dict): декодированный JWT-токен с ключом "exp".
    """
    expected_min = settings.token.exp - 20
    expected_max = settings.token.exp

    exp = decode_token["exp"]
    now = int(time.time())
    lifetime = exp - now

    if not (expected_min <= lifetime <= expected_max):
        logger.error(
            f"Некорректное время жизни токена: "
            f"{expected_min} <= {lifetime} <= {expected_max}"
        )

    assert expected_min <= lifetime <= expected_max, (
        f"Время жизни токена {lifetime} выходит за допустимый диапазон "
        f"{expected_min} <= {lifetime}<= {expected_max}"
    )


@allure.step("Проверка соответствия UUID пользователя в токене")
def user_uuid_at_token(user_payload, payload):
    """
    Проверяет, что ID пользователя корректно записан в JWT-токене.

    Функция сравнивает значение `id` из данных профиля пользователя
    (user_payload) со значением `sub` в полезной нагрузке токена (payload).
    Согласно стандарту JWT, поле `sub` должно содержать идентификатор субъекта,
    то есть ID (UUID) пользователя, которому выдан токен.

    Параметры:
        user_payload (dict):
            Данные пользователя, содержащие ключ "id".

        payload (dict):
            Декодированная полезная нагрузка JWT-токена,
            содержащая поле "sub".

    Исключения:
        AssertionError — если UUID пользователя не совпадает с UUID,
        указанным в токене.
    """
    user_id = user_payload["id"]
    token_sub = payload["sub"]

    if user_id != token_sub:
        logger.error(
            f"Несовпадение UUID пользователя: user_payload['id']={user_id} != payload['sub']={token_sub}"
        )

    assert user_id == token_sub, (
        f"UUID пользователя не совпадает с sub в токене: "
        f"user_payload['id']={user_id} != payload['sub']={token_sub}"
    )


@allure.step("Проверка успешной авторизации пользователя")
def positive_login_assertions(user_data: dict, response: Response):
    """
    Проверяет корректность данных авторизации пользователя.

    Проверяются:
        - JWT-токен успешно извлекается из заголовков ответа
        - Время жизни токена (exp) соответствует настройкам
        - UUID пользователя совпадает с sub в токене

    Args:
        user_data (dict): словарь с данными пользователя, например:
            {
                "id": "uuid",
                "email": "user@example.com",
                "password": "secure_password"
            }
        response (Response): объект ответа от запроса логина

    Raises:
        AssertionError: если какое-либо из условий проверки не выполняется
    """
    # извлечение токена
    token = extract_secure_token(headers=response.headers)
    # декодирование токена
    decode_token = decode_jwt_token(token=token["token"])
    # проверка времени истечения токена
    token_lifetime(decode_token=decode_token)
    # проверка нахождения uuid пользователя в токене
    user_uuid_at_token(user_payload=user_data, payload=decode_token)
