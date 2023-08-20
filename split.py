import cv2
import os

 

# 입력 비디오 파일 경로
input_video_path = '/home/ljj/workspace/waffle_factory/sample1.mp4'

 

# 출력 이미지 저장 폴더 경로
output_images_folder = 'out2'
os.makedirs(output_images_folder, exist_ok=True)

 

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(input_video_path)

 

frame_count = 0
n_frames_interval = 1  # N 프레임 간격 설정
# 비디오의 초당 프레임 수 및 전체 프레임 수 얻기
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

 

# target_time_seconds = 15

 

# 특정 시간으로 이동
target_frame =  16777# int(target_time_seconds * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)

 

 

num = 0 
while cap.isOpened():
    try:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % n_frames_interval == 0:
            # 이미지 파일명 생성
            image_filename = f"background_{frame_count:04d}.png"

            # 이미지 파일 저장 경로
            image_path = os.path.join(output_images_folder, image_filename)

            # 이미지 저장
            cv2.imwrite(image_path, frame)

            print(f"Saving {image_filename}")

        frame_count += 1
    except:
        pass

 

 

print("Image extraction complete.")