import logging
import secrets
from datetime import time
from typing import Optional

from pydantic_settings import BaseSettings
from pydantic.fields import Field
from pydantic.main import BaseModel


class MiddleWareBase(BaseModel):
    host: str
    port: int
    password: str


class DbStruct(MiddleWareBase):
    user: str
    pool_size: int = 30
    max_overflow: int = 100

class Settings(BaseSettings):
    ENV: str = "dev"

    CORS_HOSTS: list[str] = ["*"]

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    LOGGING_LEVEL: int = logging.INFO

    PROJECT_NAME: str = "power-bot"

    # Mysql
    # DB_MYSQL: DbStruct
    # DB_NAME: str = ""

    BOT_APPID:int
    BOT_TOKEN:str


    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()  # type: ignore
