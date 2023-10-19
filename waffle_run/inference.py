
from waffle_hub.hub import Hub
import argparse

parser = argparse.ArgumentParser(description='Waffle Training.')
parser.add_argument('--gpu', type=str, default=0, help='GPU number to use.')
parser.add_argument('--conf', type=float, default=0.15, help='GPU number to use.')
parser.add_argument('--model_name', type=str, default='PeopleDet_v1.4.2', help='Waffle Model Hub Name.')
parser.add_argument('--source', type=str, default='/home/ljj/data/Background/bg2', help='Dataset file path.')

args = parser.parse_args()

hub = Hub.load(name=args.model_name)

hub.inference(source=args.source, device=args.gpu, draw=True, confidence_threshold=args.conf)