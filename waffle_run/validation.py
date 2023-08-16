
from waffle_hub.hub import Hub
from waffle_hub.dataset import Dataset
import argparse

parser = argparse.ArgumentParser(description='Waffle Training.')
parser.add_argument('--gpu', type=str, default=0, help='GPU number to use.')

parser.add_argument('--dataset_name', type=str, default="IwestDataset_v1.1", help='Number of image channels')
parser.add_argument('--model_name', type=str, default='Iwest_FireDet_v1.0.1', help='Dataset file path.')

args = parser.parse_args()

dataset = Dataset.load(name=args.dataset_name)

hub = Hub.load(name=args.model_name)

# hub.export(device=1)
# hub.inference(source='/home/ljj/waffle/datasets/iwest/exports/YOLO/test/images', device='0', draw=True)



# from ultralytics import YOLO

# model = YOLO(model="/home/ljj/best.pt")


# model.predict(source="/home/ljj/waffle/datasets/smoke/exports/YOLO/test/images/0411_서부발전_연기_지상3", save=True, iou=0.01, conf=0.1)

hub.evaluate(dataset=dataset, draw=True)