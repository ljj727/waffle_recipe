import ffmpeg

input_file = '/home/ljj/workspace/waffle_factory/runs/detect/result/open_event/open_van_event_.webm'
output_file = '/home/ljj/workspace/waffle_factory/runs/detect/result/open_event/open_van_event.mp4'

ffmpeg.input(input_file).output(output_file, vcodec='libx264').run()
# new_width = 1960
# new_height = 1080

# ffmpeg.input(input_file).output(output_file, vf=f'scale={new_width}:{new_height}').run(overwrite_output=True)

# print("해상도 변경 완료.")

print("변환 완료.")
