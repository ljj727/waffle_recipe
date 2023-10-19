from ultralytics import YOLO
try:
    model = YOLO("yolov8s.pt", task="detect")
    model.train(
        data="/home/ljj/waffle/datasets/PeopleDataset_else_v1.0.0/exports/ULTRALYTICS/data.yaml",
        epochs=100,
        batch=4,
        imgsz=[640, 640],
        lr0=0.01,
        lrf=0.01,
        device="0",
        workers=16,
        seed=0,
        verbose=True,
        project="PeopleDet",
        name="v1.4.0",
        **{}
    )
except Exception as e:
    print(e)
    raise e