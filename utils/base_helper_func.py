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
def extract_secure_token(headers) -> dict:
    """
    Извлекает и анализирует токен
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
