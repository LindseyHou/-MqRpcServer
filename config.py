from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    # mongodb config
    db_host: str = "localhost"
    db_port: int = 27017
    db_name: str = "firefighting-production"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
