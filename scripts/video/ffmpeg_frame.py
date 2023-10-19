import ffmpeg

# 입력 동영상 파일 경로
input_video_path = '/home/ljj/workspace/autocare_docker/url1/1_speed60.mp4'

# 출력 동영상 파일 경로
output_video_path = '/home/ljj/workspace/autocare_docker/url1/1_speed60_30.mp4'



# 입력 동영상 파일 경로

# 원하는 프레임 속도 설정
target_frame_rate = 30

# FFmpeg 명령어를 사용하여 동영상 프레임 수 조절
ffmpeg.input(input_video_path).output(output_video_path, r=target_frame_rate).run()

print("프레임 수가 조절된 동영상이 생성되었습니다.")