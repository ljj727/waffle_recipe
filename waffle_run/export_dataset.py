from waffle_hub.dataset import Dataset

name="VihicleDataset_v1.0.0"

dataset = Dataset.load(name=name)

dataset.split(
  train_ratio = 0.9,
  val_ratio = 0.1,
)

dataset.export('YOLO')