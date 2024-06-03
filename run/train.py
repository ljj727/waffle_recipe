from ultralytics import YOLO
# from src.callbacks import CustomCallback

def run_train():
    try:
        model = YOLO("yolov8s.pt", task="detect")
        model.train(
            cfg='/home/ljj/waffle/ultralytics/custom_detect.yaml',
            data='/home/ljj/waffle/datasets/SKT/skt_v2/exports/ULTRALYTICS/data.yaml', 
            # callbacks=CustomCallback
        )
    except Exception as e:
        print(e)
        raise e
