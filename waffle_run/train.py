from waffle_hub.hub import Hub
from waffle_hub.dataset import Dataset
import argparse

parser = argparse.ArgumentParser(description='Waffle Training.')
parser.add_argument('--gpu', type=str, default=0, help='GPU number to use.')
parser.add_argument('--batch_size', type=int, default=64, help='Integer value for batch size.')
parser.add_argument('--epochs', type=int, default=200, help='Integer value for batch size.')
parser.add_argument('--image_size', type=int, default=32, help='Integer value for number of points.')

parser.add_argument('--dataset_name', type=str, default="HelmetDataset_v1.0.0", help='Number of image channels')
parser.add_argument('--model_name', type=str, default='HelmetCls_v1.0.2', help='Dataset file path.')

args = parser.parse_args()

dataset = Dataset.load(name=args.dataset_name)

try:
  hub = Hub.new(
    name = args.model_name,
    task = "classification",
    model_type = "yolov8",
    model_size = "m",
    categories = dataset.get_category_names(),
  )
except:
  hub = Hub.load(name=args.model_name)

hub.train(
  dataset=dataset,
  epochs = args.epochs,
  batch_size = args.batch_size,
  image_size = args.image_size,
  device = str(args.gpu)
)
# hub.inference(
#   source=export_dir,
#   draw=True,
#   device="cpu"
# )
