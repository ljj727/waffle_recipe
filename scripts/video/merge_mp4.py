from moviepy.editor import VideoFileClip, concatenate_videoclips
import glob

path = "/home/ljj/workspace/autocare_docker/url1/1"

videos= glob.glob(f"{path}/*.mp4")


# file1_path = "/home/ljj/workspace/autocare_docker/url1/1_start_30.mp4"
# file2_path = "/home/ljj/workspace/autocare_docker/url1/1_speed60_30.mp4"

# 비디오 클립을 로드합니다.
# clip1 = VideoFileClip(file1_path)
# clip2 = VideoFileClip(file2_path)
clips = [VideoFileClip(video) for video in videos]

# 비디오 클립을 가로로 나란히 합칩니다.
final_clip = concatenate_videoclips(clips, method="compose")

# 결과를 저장할 MP4 파일의 경로
output_path = "/home/ljj/workspace/autocare_docker/url1/output.mp4"

# 합친 비디오를 저장합니다.
final_clip.write_videofile(output_path, codec="libx264")