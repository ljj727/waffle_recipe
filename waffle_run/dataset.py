
from waffle_hub.dataset import Dataset
name="AihubCityload_Vihicle_v1.1.0"

dataset = Dataset.from_coco(
        name=name,
        task = "object_detection",
        coco_file= '/home/ljj/dataset/AihubCityload_Vihicle_v1.1.0/coco.json',
        coco_root_dir= '/home/ljj/dataset/AihubCityload_Vihicle_v1.1.0/images',
        )
# dataset = Dataset.load(name)
# dataset.split(
#   train_ratio = 0.9,
#   val_ratio = 0.1,
# )
