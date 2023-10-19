
from waffle_hub.dataset import Dataset


name="PeopleDataset_FalldownNG_v1.0.0"
dataset = Dataset.load(name=name)

dataset.draw_annotations()
# dataset.split(
#   train_ratio = 0.99,
#   val_ratio = 0.01,
# )
# dataset.export("ULTRALYTICS")