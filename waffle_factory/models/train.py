import os
import sys
sys.path.append(os.getcwd())
from waffle_factory.utils.callbacks import clearml_logs
from ultralytics import YOLO

def trainer():
    model = YOLO("yolov8m.pt", task="detect")
    model.callbacks = clearml_logs()
    model.train(
        data="/home/ljj/waffle/datasets//Iwest_SmokeDataset_v1.0.0/exports/YOLO/data.yaml",
        epochs=200,
        batch=64,
        imgsz=640,
        lr0=0.01,
        lrf=0.01,
        device="0",
        workers=16,
        seed=0,
        verbose=True,
        project="SmokeDet",
        name="v1.0.0",
        **{}
    )

if __name__ == "__main__":
    trainer()
