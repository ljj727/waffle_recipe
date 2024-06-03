from configs import PreProcConfig
from wafflow.gdd.al import GDino

def run_smart_labeling():
    GDino(PreProcConfig).gdd_to_wd()

