import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    project_path: str = os.path.abspath(os.getcwd())

    project_name: str
    debug: bool
    host: str
    port: str

    api_v1_str: str
    api_secret_key: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()
