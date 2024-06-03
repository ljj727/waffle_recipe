from configs import PreProcConfig
from wafflow.core.dataset import create_dataset

def run_dataset():
    create_dataset(PreProcConfig)