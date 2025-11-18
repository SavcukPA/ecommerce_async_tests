from pprint import pformat

from httpx import Response, Request
import logging

logger = logging.getLogger("HTTP_CLIENT")


async def log_request_event_hook(request: Request):
    body = await request.aread()

    try:
        body_text = body.decode("utf-8")
    except UnicodeDecodeError:
        body_text = body.decode(
            "utf-8", errors="replace"
        )  # Заменяет невалидные символы

    logger.info(
        f"Отправка запроса: method - {request.method}, url - {request.url}, body: {body_text}"
    )


async def log_response_event_hook(response: Response):
    logger.info(
        f"HTTP Response: status code is {response.status_code} {response.reason_phrase}, url - {response.url}"
    )

    await response.aread()
    try:
        response_data = response.json()
        format_response_data = pformat(response_data)
        logger.info(f"Получен ответ от сервера: {format_response_data}")
    except Exception:
        response_text = response.text
        logger.exception(f"Ошибка ответа от сервера: {response_text[:500]}...")
