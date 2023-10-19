import ffmpeg

input_file = '/home/ljj/workspace/autocare_docker/video/van_open.mp4'
output_file = '/home/ljj/workspace/autocare_docker/video/van_open_.mp4'

# FFmpeg 명령어를 사용하여 코덱을 H.264로 변경
ffmpeg.input(input_file).output(output_file, vcodec='libx264').run()

print("코덱 변경 완료.")
