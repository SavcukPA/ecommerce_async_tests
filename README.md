# ecommerce-async-tests

**ecommerce-async-tests** — демонстрация асинхронных API-тестов для проекта [fastapi_ecommerce_api](https://github.com/kolenkoal/fastapi_ecommerce_api).  

Проект реализован на Python 3.12 с использованием **pytest**, **pytest-asyncio** и **allure** для отчётности.

---

## 📦 Требования

- Python >= 3.12.4
- Poetry >= 1.5 (или любая версия, поддерживающая pyproject.toml)
- 
### Основные зависимости

- `pydantic-settings` (2.11.0 ≤ версия < 3.0.0)
- `allure-pytest` (2.15.0 ≤ версия < 3.0.0)
- `pytest-asyncio` (1.2.0 ≤ версия < 2.0.0)
- `faker` (37.12.0 ≤ версия < 38.0.0)
- `email-validator` (2.3.0 ≤ версия < 3.0.0)
- `pyyaml` (6.0.3 ≤ версия < 7.0.0)
- `validators` (0.35.0 ≤ версия < 0.36.0)
- `pyjwt` (2.10.1 ≤ версия < 3.0.0)

---
### Предустановка

#### Allure
  - 1 Установка scoop (power shell)
```bash
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
  - 2 Устновка allure
```bash
  scoop install allure
```
  - 3 Установка Java
```bash
  scoop install temurin25-jdk
```

▶️[Видео: Установка Allure на Windows](https://www.youtube.com/watch?v=MUKkN3h2OCM)

#### Docker

- 1 Выбрать OS
- 2 Запустить файл установки
  
▶️[Видео: Установка Docker Desktop на Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

#### Fastapu-ecommerce-api
[project fastapi_ecommerce_api](https://github.com/kolenkoal/fastapi_ecommerce_api)
- 1 Прочитать Readme
- 2 Выполнить устновку по инстуркции

### Устновка из архива

Есть подготовленный архив с проектом. Внёс нужные измениния и всё работает сразу.

- 1 Скачайть архив 📥[encomerce.zip](https://disk.yandex.ru/d/3yxsZPytNxn8dg)
- 2 Разархивировать в любое удобное место
- 3 Открыть командную строку в корневой директории проекта
- 4 Выолнить команду
``` bash
docker-compose up -d --build
```
- 5 Открыть Docker Desktop
- 6 Запустить контейнеры
![Poetry dependencies](readme_images/docker.jpg)




## ⚡ Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/SavcukPA/ecommerce_async_tests.git
cd ecommerce_async_tests
```
2. Устанавливаем poetry и зависимости:
```bash
pip install poetry
poetry install
```

3. Проверяем установленные зависимости:
```bash
poetry show --tree
или
poetry show
```
![Poetry dependencies](readme_images/poetry_dep.jpg)


### Запуск тестов
- 1 Ввести в терминале
```
pytest -sv tests
```
### После запуска тестов
- 1 Сгенерируются две папки
  - 1 allure-results / папка с результатами тесового прогона
  - 2 allure-report / папка с отчетами
- 2 Открыть папку allure-report и открыть файл index.html (в браузере)
![Allure derictories](readme_images/allure_dir.jpg)
## Ожидаемый результат отображения отчета index.html
![Allure main page](readme_images/allure_main_page.jpg)
![Allure tests run page](readme_images/tests_run_page.jpg)

## Структура проекта

```
ecommerce_async_tests/
│
├── allure-report/
├── allure-results/
│
├── assertions/
│   └── auth/
│       ├── login.py
│       └── register.py
│       
│
├── clients/
│   ├── base_client.py
│   ├── event_hooks.py
│   └── headers.py
│   
│
├── data/
│   ├── cases/
│       └── register_users.py
│   
│
├── fixtures/
│   └── auth.py
│   
│
├── logs/
│   ├── error.log
│   └── test.log
│
├── readme_images/
│   ├── allure_dir.jpg
│   ├── allure_main_page.jpg
│   ├── docker.jpg
│   ├── poetry_dep.jpg
│   └── tests_run_page.jpg
│
├── services/
│   └── auth/
│       ├── models/
│       │   └── user_register.py
│       ├── auth.py
│       ├── endpoints.py
│       └── payloads.py
│       
│
├── tests/
│   └── api_tests/
│       └── auth_tests/
│           ├── user_login_tests.py
│           └── user_register_tests.py
│
├── utils/
│   ├── base_helper_func.py
│   ├── generators.py
│   ├── helper.py
│   ├── hooks.py
│   ├── models.py
│   ├── paths.py
│   ├── regex_patterns.py
│   └── setup_logger.py
│
├── .env
├── .gitignore
├── config.py
├── conftest.py
├── ex.py
├── logging_config.yaml
├── poetry.lock
├── pyproject.toml
└── pytest.ini
```

- **allure/:** Директория содержащая отчеты allure
    - **allure-report** Директория со сгенерированными отчетами allure
    - **allure-results** Директория с результатами отчета, используется для генерации allure отчетов

