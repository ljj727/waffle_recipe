from ultralytics import YOLO

# model = YOLO(model="/home/ljj/waffle/hubs/HelmetCls_v1.0.2/weights/best_ckpt.pt", task='classifier')


# model.predict(source="/home/ljj/waffle/datasets/HelmetDataset_v1.0.0/exports/YOLO/val/wear/0a92ce9e-9e39-4abe-9f27-662ca05db55c.jpg", save=True, batch=1)
model = YOLO("/home/ljj/data/falldown/falldown_clean/best.pt", task="classify")
model.val(data='/home/ljj/data/falldown/falldown_clean/data.yaml')