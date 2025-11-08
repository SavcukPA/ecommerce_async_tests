from httpx import Request, Response
import logging

logger = logging.getLogger("HTTP_CLIENT")


def log_request_event_hook(request: Request):
    logger.info(f"Отправка запроса: method - {request.method}, url - {request.url}")


def log_response_event_hook(response: Response):
    logger.info(
        f"Статус код: {response.status_code} {response.reason_phrase}, url - {response.url}"
    )
