from ultralytics import YOLO
import glob



model = YOLO(model='/home/ljj/waffle/hubs/HanlimDet_v1.0.0/weights/best_ckpt.pt')
model.predict(source="/home/ljj/workspace/waffle_factory/output_video_raw.mp4", save=True, show=True)
# model.val(data="/home/ljj/waffle/datasets/test_car_ison/exports/YOLO/data.yaml")
# img_list = glob.glob("/home/ljj/waffle/datasets/test_iwest_fire_kisa/raw/**/*.jpg", recursive=True)


# print(len(img_list))
# model.val(source="/home/ljj/workspace/waffle_factory/output_images1", save=True, device=1, conf=0.15)
