from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Logger(BaseModel):

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class HttpClient(BaseModel):
    host: str
    timeout: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    http_client: HttpClient
    logger: Logger


settings = Settings()