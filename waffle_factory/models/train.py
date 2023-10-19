import os
import sys
sys.path.append(os.getcwd())
from waffle_factory.utils.callbacks import clearml_logs
from ultralytics import YOLO

def trainer():
    model = YOLO("yolov8m-cls.pt", task="classify")
    model.callbacks = clearml_logs()
    model.train(
        data="/home/ljj/waffle/datasets/HelmetDataset_v1.0.0/exports/YOLO",
        epochs=400,
        batch=256,
        imgsz=224,
        lr0=0.01,
        lrf=0.01,
        device="0",
        workers=16,
        seed=0,
        verbose=True,
        project="",
        name="v1.0.0",
        **{}
    )

if __name__ == "__main__":
    trainer()
