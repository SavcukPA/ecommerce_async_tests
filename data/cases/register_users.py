import re

from utils import regex_patterns as r_p
from services.auth.models.user_register import User
from utils.generators import generators
from utils.models import ErrorResponseModel, ErrorDetail
from random import randint

fake_en = generators.faker_en
fake_ru = generators.faker_ru

valid_fake_name_en = fake_en.first_name()
valid_fake_name_ru = fake_ru.first_name()
valid_fake_last_name_en = fake_en.last_name()
valid_fake_last_name_ru = fake_ru.last_name()


case_1 = {
    "data": {
        "first_name": "",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: пустое поле имя",
        "ids": "first_name 0 symbols",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at least 2 characters",
        "type": "string_too_short",
    },
}
case_2 = {
    "data": {
        "first_name": generators.get_random_str(len_str=1, use_latin=True),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина имени 1 символ",
        "ids": "first_name 1 symbol",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at least 2 characters",
        "type": "string_too_short",
    },
}

case_3 = {
    "data": {
        "first_name": generators.get_random_str(
            len_str=2, use_latin=True, case_type=generators.case_types.TITLE
        ),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина имени 2 символ ",
        "ids": "first_name 2 symbol",
        "case_type": "positive",
    },
}

case_4 = {
    "data": {
        "first_name": generators.get_random_str(
            len_str=3, use_cyrillic=True, case_type=generators.case_types.TITLE
        ),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина имени 3 символа",
        "ids": "first_name 3 symbol",
        "case_type": "positive",
    },
}

case_5 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: случайное валидное имя",
        "ids": "random valid first_name",
        "case_type": "positive",
    },
}

case_6 = {
    "data": {
        "first_name": generators.get_random_str(
            len_str=255, use_cyrillic=True, case_type=generators.case_types.TITLE
        ),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина имя 255 символов",
        "ids": "first_name 255 symbol",
        "case_type": "positive",
    },
}

case_7 = {
    "data": {
        "first_name": generators.get_random_str(
            len_str=256, use_latin=True, case_type=generators.case_types.TITLE
        ),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина имя 256 символов",
        "ids": "first_name 256 symbol",
        "case_type": "positive",
    },
}

case_8 = {
    "data": {
        "first_name": generators.get_random_str(
            len_str=257, use_cyrillic=True, case_type=generators.case_types.TITLE
        ),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина имя 257 символов",
        "ids": "first_name 257 symbol",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at most 256 characters",
        "type": "string_too_long",
    },
}

case_9 = {
    "data": {
        "first_name": f"{fake_en.first_name()} {fake_en.first_name()}",
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: двойное имя, разделитель пробел",
        "ids": "double first_name delimiter space",
        "case_type": "positive",
    },
}

case_10 = {
    "data": {
        "first_name": f"{fake_ru.first_name()}-{fake_ru.first_name()}",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: двойное имя, разделитель дефис",
        "ids": "double first_name delimiter hyphen",
        "case_type": "positive",
    },
}

case_11 = {
    "data": {
        "first_name": f"-{fake_ru.first_name()}",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: дефис в начале имени",
        "ids": "hyphen at the beginning of a name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}


case_12 = {
    "data": {
        "first_name": f"{fake_ru.first_name()}-",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: дефис в конце имени",
        "ids": "hyphen at the ending of a name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_13 = {
    "data": {
        "first_name": f" {valid_fake_name_en}",
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: пробел в начале имени",
        "ids": "space at the beginning of a name",
        "case_type": "positive",
    },
    "expected_value": {"first_name": valid_fake_name_en},
}

case_14 = {
    "data": {
        "first_name": f"{valid_fake_name_ru} ",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: пробел в конце имени",
        "ids": "space at the ending of a name",
        "case_type": "positive",
    },
    "expected_value": {"first_name": valid_fake_name_ru},
}

case_15 = {
    "data": {
        "first_name": f"{generators.get_random_str(use_special=True)}",
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: спец символы в имени",
        "ids": "special symbols in to first_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_16 = {
    "data": {
        "first_name": f"{generators.get_random_str(use_special=True)}{randint(1,11)}",
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: спец символы и числа в имени",
        "ids": "special symbols and numbers in to first_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_17 = {
    "data": {
        "first_name": f"{fake_en.first_name()}{randint(1,11)}",
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: строка с числами",
        "ids": "string and numbers in to first_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_18 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": "",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: пустое поле фамилия",
        "ids": "last_name 0 symbols",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at least 2 characters",
        "type": "string_too_short",
    },
}
case_19 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": generators.get_random_str(len_str=1, use_cyrillic=True),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина фамилии 1 символ",
        "ids": "last_name 1 symbol",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at least 1 characters",
        "type": "string_too_short",
    },
}

case_20 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": generators.get_random_str(len_str=2, use_latin=True),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина фамилии 2 символа ",
        "ids": "last_name 2 symbol",
        "case_type": "positive",
    },
}

case_21 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": generators.get_random_str(
            len_str=3, use_cyrillic=True, case_type=generators.case_types.TITLE
        ),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина фамилии 3 символа ",
        "ids": "last_name 3 symbols",
        "case_type": "positive",
    },
}

case_22 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": generators.get_random_str(
            len_str=255, use_latin=True, case_type=generators.case_types.TITLE
        ),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина фамилии 255 символов ",
        "ids": "last_name 255 symbols",
        "case_type": "positive",
    },
}

case_23 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": generators.get_random_str(
            len_str=256, use_cyrillic=True, case_type=generators.case_types.TITLE
        ),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина фамилии 256 символа ",
        "ids": "last_name 256 symbols",
        "case_type": "positive",
    },
}

case_24 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": generators.get_random_str(
            len_str=257, use_latin=True, case_type=generators.case_types.TITLE
        ),
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина фамилии 257 символов",
        "ids": "last_name 257 symbols",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at most 256 characters",
        "type": "string_too_long",
    },
}

case_25 = {
    "data": {
        "first_name": f"{fake_ru.first_name()}",
        "last_name": f"{fake_ru.last_name()} {fake_ru.last_name()}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: двойная фамилия, разделитель пробел",
        "ids": "double last_name delimiter space",
        "case_type": "positive",
    },
}

case_26 = {
    "data": {
        "first_name": f"{fake_en.first_name()}",
        "last_name": f"{fake_en.last_name()}-{fake_en.last_name()}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: двойная фамилия, разделитель дефис",
        "ids": "double last_name delimiter hyphen",
        "case_type": "positive",
    },
}

case_27 = {
    "data": {
        "first_name": f"{fake_ru.first_name()}",
        "last_name": f"-{fake_ru.last_name()}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: дефис в начале фамилии",
        "ids": "hyphen at the beginning of a last_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_28 = {
    "data": {
        "first_name": f"{fake_en.first_name()}",
        "last_name": f"{fake_en.last_name()}-",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: дефис в конце фамилии",
        "ids": "hyphen at the ending of a last_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_29 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": f" {valid_fake_last_name_ru}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: пробел в начале фамилии",
        "ids": "space at the beginning of a last_name",
        "case_type": "positive",
    },
    "expected_value": {"last_name": valid_fake_last_name_ru},
}

case_30 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": f"{valid_fake_last_name_ru} ",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: пробел в конце фамилии",
        "ids": "space at the ending of a last_name",
        "case_type": "positive",
    },
    "expected_value": {"last_name": valid_fake_last_name_ru},
}

case_31 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": f"{generators.get_random_str(len_str=randint(5,10),use_special=True)}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: спец символы в фамилии",
        "ids": "special symbols in to last_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_32 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": f"{generators.get_random_str(len_str=randint(5,10),use_special=True)}{randint(1,10)}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: спец символы и числа в фамилии",
        "ids": "special symbols and numbers in to last_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_33 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": f"{generators.get_random_str(len_str=randint(5,10),use_latin=True)}{randint(1,10)}",
        "password": fake_en.password(),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация пользователя: спец символы и числа в фамилии",
        "ids": "special symbols and numbers in to last_name",
        "case_type": "negative",
    },
    "error_data": {"detail": "Invalid First Name or Last Name."},
}

case_34 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": re.sub(r_p.email_remove_after_at, "", fake_en.email()),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: некорректный email (отсутствует домен)",
        "ids": "not str before at (@)",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "value is not a valid email address: There must be something before the @-sign.",
        "type": "value_error",
    },
}

case_35 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": re.sub(r_p.email_remove_after_at, "@", fake_en.email()),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: Обрезка email после символа @",
        "ids": "not str after at (@)",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "value is not a valid email address: There must be something after the @-sign.",
        "type": "value_error",
    },
}

case_36 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": re.sub(r_p.email_remove_high_domain, "", fake_en.email()),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: удаление домена верхнего уровня из email (com, ru)",
        "ids": "remove high domain in to email (com, ru)",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "value is not a valid email address: The part after the @-sign is not valid. It should have a period.",
        "type": "value_error",
    },
}

case_37 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(),
        "email": re.sub(r_p.email_remove_before_at, "a", fake_en.email()),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: один символ перед @",
        "ids": "1 symbol before at (@)",
        "case_type": "negative",
    },
}

case_38 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(),
        "email": f"{generators.get_random_str(len_str=65, use_latin=True)}@example.com",
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина email превышает допустимое кол-во символов",
        "ids": "invalid maximum len email",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "value is not a valid email address: "
        "The email address is too long before the @-sign (1 character too many).",
        "type": "value_error",
    },
}

case_39 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": generators.get_random_str(len_str=4, use_latin=True),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина пароля 4 символа",
        "ids": "len password 4 symbol",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at least 5 characters",
        "type": "string_too_short",
    },
}

case_40 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(length=5),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина пароля 5 символов",
        "ids": "len password 5 symbols",
        "case_type": "positive",
    },
}

case_41 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(length=6),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина пароля 6 символов",
        "ids": "len password 6 symbols",
        "case_type": "positive",
    },
}

case_42 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(length=1023),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина пароля 1023 символа",
        "ids": "len password 1023 symbols",
        "case_type": "positive",
    },
}

case_43 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": fake_en.password(length=1024),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 201,
        "pydantic_model": User,
        "title": "Регистрация пользователя: длина пароля 1024 символа",
        "ids": "len password 1024 symbols",
        "case_type": "positive",
    },
}

case_44 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": fake_en.password(length=1025),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: длина пароля 1025 символов",
        "ids": "len password 1025 symbols",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "String should have at most 1024 characters",
        "type": "string_too_long",
    },
}

case_45 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": generators.get_random_str(
            len_str=randint(5, 10), use_cyrillic=True
        ),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: пароль содержит только латиницу",
        "ids": "password latin char",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "Password must contain at least one digit or special character",
        "type": "value_error",
    },
}

case_46 = {
    "data": {
        "first_name": fake_ru.first_name(),
        "last_name": fake_ru.last_name(),
        "password": generators.get_random_str(
            len_str=randint(5, 10), use_cyrillic=True
        ),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: пароль содержит только кириллицу",
        "ids": "password cyrillic char",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "Password must contain at least one digit or special character",
        "type": "value_error",
    },
}

case_47 = {
    "data": {
        "first_name": fake_en.first_name(),
        "last_name": fake_en.last_name(),
        "password": str(randint(10000, 1000000000)),
        "email": fake_en.email(),
    },
    "metadata": {
        "expected_status_code": 422,
        "pydantic_model": ErrorResponseModel,
        "title": "Регистрация пользователя: пароль содержит только цифры",
        "ids": "password numbers",
        "case_type": "negative",
    },
    "error_data": {
        "msg": "Password must contain at least one digit or special character",
        "type": "value_error",
    },
}


positive_test_cases = (
    case_3,
    case_4,
    case_5,
    case_6,
    case_9,
    case_10,
    case_13,
    case_14,
    case_20,
    case_21,
    case_22,
    case_23,
    case_25,
    case_26,
    case_29,
    case_30,
    case_40,
    case_41,
    case_42,
    case_43,
)
positive_test_cases_ids = [case["metadata"]["ids"] for case in positive_test_cases]


negative_test_cases = (
    case_1,
    case_2,
    case_7,
    case_8,
    case_11,
    case_12,
    case_15,
    case_16,
    case_17,
    case_18,
    case_19,
    case_24,
    case_27,
    case_28,
    case_31,
    case_32,
    case_33,
    case_34,
    case_35,
    case_36,
    case_37,
    case_38,
    case_39,
    case_44,
    case_45,
    case_46,
    case_47,
)

negative_test_cases_ids = [case["metadata"]["ids"] for case in negative_test_cases]

case_48 = {
    "metadata": {
        "expected_status_code": 400,
        "pydantic_model": ErrorDetail,
        "title": "Регистрация уже существующего пользователя",
        "ids": "user already exists",
        "case_type": "negative",
    },
    "error_data": {"detail": "REGISTER_USER_ALREADY_EXISTS"},
}

specific_cases = {
    "tests_register_already_exists": case_48,
}
