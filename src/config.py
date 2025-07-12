from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Настройка среды
    MODE: Literal["TEST", "LOCAL", "DEV", "PROD"] = Field(default="LOCAL")

    # Настройки сервера
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)
    ROOT_PATH: str = Field(default="")

    # Настройки откуда будут браться данные переменных окружения
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()