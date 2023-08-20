from ultralytics import YOLO
import glob



model = YOLO(model='/home/ljj/workspace/best_people.pt')
# model.val(data="/home/ljj/waffle/datasets/test_car_ison/exports/YOLO/data.yaml")
# img_list = glob.glob("/home/ljj/waffle/datasets/test_iwest_fire_kisa/raw/**/*.jpg", recursive=True)


# print(len(img_list))
model.predict(source="/home/ljj/workspace/deeps/DeepStream-Yolo/output_video.mp4", save=True, device=0, conf=0.15)
