
from waffle_hub.dataset import Dataset
dataset = Dataset.from_yolo(
  name = "PeopleDataset_v1.0.0",
  task = "object_detection",
  yolo_root_dir= "/home/ljj/dataset/people/v1.1.0",
  yaml_path= "/home/ljj/dataset/people/v1.1.0/data.yaml"
)
# dataset.split(
#   train_ratio = 0.8,
#   val_ratio = 0.1,
#   test_ratio = 0.1
# )
# dataset =Dataset.load(name='PeopleDet_5')
dataset.export("COCO")
