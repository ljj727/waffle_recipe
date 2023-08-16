from ultralytics import YOLO
import glob



model = YOLO(model='/home/ljj/waffle/hubs/v1.2.0/FireDet/v1.2.2/55.pt')
# model.val(data="/home/ljj/waffle/datasets/test_car_ison/exports/YOLO/data.yaml")
# img_list = glob.glob("/home/ljj/waffle/datasets/test_iwest_fire_kisa/raw/**/*.jpg", recursive=True)


# print(len(img_list))
model.predict(source="/home/ljj/workspace/waffle_factory/output_images1", save=True, device=1, conf=0.15)
