import cv2
import numpy as np

# 동영상 파일 경로
input_video_path = '/home/ljj/demo/video/Falldown_230720.mp4'

# 출력 동영상 파일 경로
output_video_path = 'output_video.mp4'

# 시작 시간과 종료 시간 설정 (단위: 초)
start_time = 11*60+44
end_time = 12*60 + 10

#동영상 파일 열기
cap = cv2.VideoCapture(input_video_path)

# 동영상 파일의 속성 가져오기
frame_width = int(cap.get(3))  # 동영상 가로 해상도
frame_height = int(cap.get(4)) # 동영상 세로 해상도
frame_rate = int(cap.get(5))   # 동영상 프레임 레이트

# 동영상 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 저장할 동영상 코덱 설정
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

# 시작 시간까지 건너뛰기
cap.set(cv2.CAP_PROP_POS_FRAMES, int(start_time * frame_rate))

# 지정한 범위의 프레임을 자르고 저장
while cap.isOpened():
    ret, frame = cap.read()
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # 현재 시간(초)
    # cv2.imshow("img", frame)
    # cv2.waitKey(1)
    
    if ret and current_time <= end_time:
        out.write(frame)
    else:
        break

# 파일 닫기
cap.release()
out.release()

print("동영상 자르기 완료.")
