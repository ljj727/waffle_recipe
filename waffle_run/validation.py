
from waffle_hub.hub import Hub
from waffle_hub.dataset import Dataset
import argparse

parser = argparse.ArgumentParser(description='Waffle Training.')
parser.add_argument('--gpu', type=str, default=0, help='GPU number to use.')

parser.add_argument('--dataset_name', type=str, default="FireDataset_Aihub_v1.1.0", help='Number of image channels')
parser.add_argument('--model_name', type=str, default='FireDet_v2.0.0', help='Dataset file path.')

args = parser.parse_args()

dataset = Dataset.load(name=args.dataset_name)

dataset.split(
  train_ratio = 0.001,
  val_ratio = 0.001,
  test_ratio = 0.998,
)

hub = Hub.load(name=args.model_name)

# hub.export(device=1)
# hub.inference(source='/home/ljj/waffle/datasets/iwest/exports/YOLO/test/images', device='0', draw=True)



# from ultralytics import YOLO

# model = YOLO(model="/home/ljj/best.pt")


# model.predict(source="/home/ljj/waffle/datasets/smoke/exports/YOLO/test/images/0411_서부발전_연기_지상3", save=True, iou=0.01, conf=0.1)

hub.evaluate(dataset=dataset, batch_size=64)