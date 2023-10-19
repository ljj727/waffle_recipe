import cv2
import os
import glob

video_lst = [
    # '/home/ljj/workspace/DeepStream-Yolo/NG1.mp4',
            #  '/home/ljj/workspace/DeepStream-Yolo/NG2.mp4',
            #  '/home/ljj/workspace/DeepStream-Yolo/NG3.mp4',
            #  '/home/ljj/workspace/DeepStream-Yolo/NG4.mp4',
            #  '/home/ljj/workspace/DeepStream-Yolo/NG5.mp4',
             '/home/ljj/workspace/DeepStream-Yolo/NG6.mp4',]#, '/home/ljj/data/iwest/서부발전/청수/220715_Cheongsu_all.mp4', '/home/ljj/data/iwest/서부발전/화성/220715_Hwaseong_all.mp4'] 
# video_lst = glob.glob('/home/ljj/data/valid/*.mp4')

# video_lst = glob.glob(video_lst)
for i, path in enumerate(video_lst):
    output_images_folder = f'/home/ljj/data/Background/bg2/5'
    os.makedirs(output_images_folder, exist_ok=True)

    cap = cv2.VideoCapture(path)

    frame_count = 0
    n_frames_interval = 10
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    target_time_seconds = 0

    target_frame =  int(target_time_seconds * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
    num = 0 
    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % n_frames_interval == 0:
                # 이미지 파일명 생성
                image_filename = f"{frame_count:04d}.jpg"

                # 이미지 파일 저장 경로
                image_path = os.path.join(output_images_folder, image_filename)

                # 이미지 저장
                cv2.imwrite(image_path, frame)

                print(f"Saving {image_filename}")

            frame_count += 1
        except:
            pass

    

    

    print("Image extraction complete.")