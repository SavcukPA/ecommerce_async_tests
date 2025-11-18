# ecommerce-async-tests

**ecommerce-async-tests** — демонстрация асинхронных API-тестов для проекта [fastapi_ecommerce_api](https://github.com/kolenkoal/fastapi_ecommerce_api).  

Проект реализован на Python 3.12 с использованием **pytest**, **pytest-asyncio** и **allure** для отчётности.

---

## 📦 Требования

- Python >= 3.12.4
- Poetry >= 1.5 (или любая версия, поддерживающая pyproject.toml)

### Предустановка

#### Allure
  - 1 Устновка scoop (power shell)
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
  
▶️[Видео: Установка Dockerr Desctope на Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

#### Fastapu-ecommerce-api


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

## ⚡ Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/SavcukPA/ecommerce_async_tests.git
cd ecommerce_async_tests
```
2. Устанавливаем poetry и зависимости:
```python
pip install poetry
poetry install
```

3. Проверяем устновленные зависимости:
```python
poetry show --tree
или
poetry show
```
![Poetry dependencies](readme_images/poetry_dep.jpg)


