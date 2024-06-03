import os
from dotenv import load_dotenv

env = os.getenv("ENV", "dev")
load_dotenv(f".env.{env}")

class DatasetConfig:
    TITLE: str = "Waffle Recipe"
    DESCRIPTION: str = "Waffle Dataset & Model Reproduce Recipe"

    GITHUB_URL: str = ""
    GITHUB_ACCESS_KEY: str = ""

    MINIO_HOST: str = "0.0.0.0"
    MINIO_PORT: int = 9000
    MINIO_ROOT_USER: str = "snuailab"
    MINIO_ROOT_PASSWORD: str = "init123!!"
    MINIO_DATA_BUCKET: str = "data"


__all__ = ["DatasetConfig"]