from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class DVCConfig(BaseSettings):
    TITLE: str = "Waffle Recipe"
    DESCRIPTION: str = "Waffle Dataset Recipe"

    SettingsConfigDict(env_file=".env")
    S3_URL: str
    S3_ACCESS_KEY_ID: str
    S3_SECRET_ACCESS_KEY: str
    S3_BUCKET: str

    GITHUB_URL: str
    GITHUB_ACCESS_KEY_ID: str
    GITHUB_SECRET_ACCESS_KEY: str

@lru_cache
def get_settings() -> DVCConfig:
    return DVCConfig()

dvc_settings = get_settings()