import glob
from pathlib import Path
import shutil
from tqdm import tqdm
import os

# 두 폴더의 경로 설정

data_dir = '/home/ljj/data/people/PeopleDataset_else_COCO_v1.0.0'
folder2_path = '/home/ljj/data/people/PeopleDataset_else_COCO_v1.0.0/draw_image'
folder1_path = '/home/ljj/data/people/PeopleDataset_else_COCO_v1.0.0/images'

else_folder = '/home/ljj/data/people/PeopleDataset_else_COCO_v1.0.0/images2'

files1 = glob.glob(folder1_path+'/**/*.jpg', recursive=True)

num = 0
# print(files1)
for file in tqdm(files1):
    subfile = file.replace(folder1_path, '')
    # dup_file = folder2_path + subfile
    # if os.path.isfile(dup_file):
    raw_file = folder2_path + subfile
    if not os.path.isfile(raw_file):
        save_path = Path(else_folder+subfile)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(file, (else_folder+ subfile)) 
        num +=1

print(num)
