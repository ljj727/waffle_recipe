from waffle_hub.dataset import Dataset

name="PeopleDataset_v3.0.0"

dataset = Dataset.load(name=name)

dataset.split(
  train_ratio = 0.99,
  val_ratio = 0.01,
)

dataset.export('ULTRALYTICS')