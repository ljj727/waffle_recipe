import os
import glob
from pathlib import Path

path = '/home/ljj/data/ison/1024data/1024/*'

images = glob.glob(path)
print(images[0])

# 원본 파일 경로
for image in images:
    old_file_path = Path(image)
    


    new_file_name = str(old_file_path.parent / ('1024'+old_file_path.name[4:]))
    print(old_file_path , new_file_name)

# 파일 이름 변경
    os.rename(old_file_path, new_file_name)