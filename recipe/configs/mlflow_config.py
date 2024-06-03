import os

class ModelConfig:
    WAFFLE_HUB_ROOT_DIR: str = os.getenv("WAFFLE_HUB_ROOT_DIR", "hubs")
    WAFFLE_DATASET_ROOT_DIR: str = os.getenv("WAFFLE_HUB_ROOT_DIR", "datasets")


    # # Minio
    # # MINIO_HOST: str = "s3"
    # MINIO_HOST: str = "0.0.0.0"  # for local
    # MINIO_PORT: int = 9000
    # MINIO_ROOT_USER: str = "minio"
    # MINIO_ROOT_PASSWORD: str = "init123!!"
    # MINIO_DIR: str = "minio"
    # MINIO_DATA_BUCKET: str = "data"


__all__ = ["Config"]