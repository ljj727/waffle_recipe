import os

class WaffleConfig:
    WAFFLE_HUB_ROOT_DIR: str = os.getenv("WAFFLE_HUB_ROOT_DIR", "hubs")
    WAFFLE_DATASET_ROOT_DIR: str = os.getenv("WAFFLE_HUB_ROOT_DIR", "datasets")
