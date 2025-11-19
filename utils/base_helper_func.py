import re

import allure
import jwt
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


@allure.step("Декодирование JWT токена")
def decode_jwt_token(token: str) -> Dict[str, Any]:
    """
    Декодирование JWT токена без проверки подписи
    (только для чтения payload)
    """
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except jwt.InvalidTokenError as e:
        logger.error(f"Invalid token: {e}")
        return {}


@allure.step("Извлечение JWT токена")
def extract_secure_token(headers: dict) -> dict:
    """Извлекает JWT-токен из заголовка `Set-Cookie` и возвращает его
    вместе с параметрами безопасности.

    Функция анализирует заголовок `Set-Cookie`, ищет cookie
    `ecommerce_token`, извлекает значение токена и определяет
    установлены ли флаги безопасности: HttpOnly, Secure, SameSite и Max-Age.

    Args:
        headers (dict): Заголовки ответа сервера (`response.headers`),
            содержащие ключ `set-cookie`.

    Returns:
        dict: Словарь вида:
            {
                "token": str,  # Извлечённый JWT токен
                "security": {
                    "http_only": bool,
                    "secure": bool,
                    "samesite": bool,
                    "max_age": bool
                },
                "full_cookie": str  # Полное содержимое cookie
            }

    Raises:
        ValueError: Если cookie `ecommerce_token` отсутствует.
    """
    logger.info("Извлечение токена из headers")
    cookies = headers.get("set-cookie", "")

    token_match = re.search(r"ecommerce_token=([^;]+)", cookies)
    if not token_match:
        raise ValueError("Token not found")

    token = token_match.group(1)

    security_checks = {
        "http_only": "HttpOnly" in cookies,
        "secure": "Secure" in cookies,
        "samesite": "SameSite" in cookies,
        "max_age": "Max-Age=3600" in cookies,
    }
    logger.info(f'"token": {token}')
    logger.info(f'"security": {security_checks}')
    logger.info(f'"full_cookie": {cookies}')
    return {"token": token, "security": security_checks, "full_cookie": cookies}
