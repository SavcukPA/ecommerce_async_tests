from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Logger(BaseModel):

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Environment(BaseModel):
    stage: str
    stand: str


class HttpClient(BaseModel):
    host: str
    timeout: int


class Token(BaseModel):
    exp: int
    aud: list[str]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    token: Token
    http_client: HttpClient
    logger: Logger
    environment: Environment


settings = Settings()
