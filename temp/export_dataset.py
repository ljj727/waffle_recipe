from waffle_hub.dataset import Dataset

name="Laycom_v1.0.0"

dataset = Dataset.load(name=name)

dataset.split(
  train_ratio = 0.90,
  val_ratio = 0.10,
)

dataset.export('ULTRALYTICS')