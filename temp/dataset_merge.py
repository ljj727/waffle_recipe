from waffle_hub.dataset import Dataset
from pathlib import Path

root_dir = Path("/home/ljj/waffle/datasets/Laycom")
dirs = [str(p.name) for p in root_dir.glob("*")]
print(dirs)

Dataset.merge(
    name= 'Laycom_v1.0.0',
    root_dir = None,
    src_names = dirs,
    src_root_dirs = [
        "/home/ljj/waffle/datasets/Laycom",
    ]*len(dirs),
    task = 'object_detection'
)