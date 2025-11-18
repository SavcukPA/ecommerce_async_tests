import logging
from pprint import pformat

import allure
import validators

from utils.models import ErrorDetail, ErrorResponseModel

logger = logging.getLogger(__name__)


@allure.step("Проверка позитивной регистрации пользователя")
def positive_register_assertions(test_case: dict, response: dict):
    """
    Проверка данных регистрации пользователя для позитивных кейсов.

    Args:
        test_case (dict): словарь с кейсом, включая данные пользователя и ожидаемые значения.
        response (dict): ответ сервера с данными зарегистрированного пользователя.

    Raises:
        AssertionError: если какое-либо поле не совпадает с ожидаемым.
    """
    expected_value = test_case.get("expected_value")
    if expected_value:
        for key, value in expected_value.items():
            test_case["data"][key] = value

    # Проверка first_name
    if test_case["data"]["first_name"] != response["first_name"]:
        logger.error(
            f"User first_name mismatch: EX={test_case['data']['first_name']}, AC={response['first_name']}"
        )
    assert (
        test_case["data"]["first_name"] == response["first_name"]
    ), f"User first_name mismatch: EX={test_case['data']['first_name']}, AC={response['first_name']}"

    # Проверка last_name
    if test_case["data"]["last_name"] != response["last_name"]:
        logger.error(
            f"User last_name mismatch: EX={test_case['data']['last_name']}, AC={response['last_name']}"
        )
    assert (
        test_case["data"]["last_name"] == response["last_name"]
    ), f"User last_name mismatch: EX={test_case['data']['last_name']}, AC={response['last_name']}"

    # Проверка email
    if test_case["data"]["email"] != response["email"]:
        logger.error(
            f"User email mismatch: EX={test_case['data']['email']}, AC={response['email']}"
        )
    assert (
        test_case["data"]["email"] == response["email"]
    ), f"User email mismatch: EX={test_case['data']['email']}, AC={response['email']}"

    # Проверка UUID
    if not validators.uuid(response["id"]):
        logger.error(f"User 'id' is not a valid UUID: {response['id']}")
    assert validators.uuid(
        response["id"]
    ), f"User 'id' is not a valid UUID: {response['id']}"


@allure.step("Проверка негативной регистрации пользователя")
def negative_register_assertion(test_case: dict, response: dict):
    """
    Проверка данных регистрации пользователя для негативных кейсов.

    Args:
        test_case (dict): словарь с кейсом, включая metadata и ожидаемые ошибки.
        response (dict): ответ сервера с ошибкой регистрации.

    Raises:
        AssertionError: если сообщение об ошибке или тип не совпадают с ожидаемым.
    """
    pydantic_model = test_case["metadata"]["pydantic_model"]

    if pydantic_model is ErrorResponseModel:
        ex_error_msg = test_case["error_data"]["msg"]
        ac_error_msg = response["detail"][0]["msg"]
        ex_error_type = test_case["error_data"]["type"]
        ac_error_type = response["detail"][0]["type"]

        if ex_error_msg != ac_error_msg:
            logger.error(
                f"Server error msg mismatch: EX={ex_error_msg}, AC={ac_error_msg}"
            )
        assert (
            ex_error_msg == ac_error_msg
        ), f"Server error msg mismatch: EX={ex_error_msg}, AC={ac_error_msg}"

        if ex_error_type != ac_error_type:
            logger.error(
                f"Server error type mismatch: EX={ex_error_type}, AC={ac_error_type}"
            )
        assert (
            ex_error_type == ac_error_type
        ), f"Server error type mismatch: EX={ex_error_type}, AC={ac_error_type}"

    elif pydantic_model is ErrorDetail:
        ex_error_data = test_case["error_data"]["detail"]
        ac_error_data = response["detail"]

        logger.info("Проверка ошибки от сервера:")
        logger.info(f"EX_error: {pformat(ex_error_data)}")
        logger.info(f"AC_error: {pformat(ac_error_data)}")

        if ex_error_data != ac_error_data:
            logger.error(
                f"Server error detail mismatch: EX={pformat(ex_error_data)}, AC={pformat(ac_error_data)}"
            )
        assert (
            ex_error_data == ac_error_data
        ), f"Server error detail mismatch: EX={pformat(ex_error_data)}, AC={pformat(ac_error_data)}"
