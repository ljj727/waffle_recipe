import glob
from pathlib import Path
import shutil
from tqdm import tqdm

# 두 폴더의 경로 설정


folder1_path = '/home/ljj/data/people/valid_result/draw_image'
folder2_path = '/home/ljj/data/people/valid_result/images'

# folder1_path = '/home/ljj/waffle/result/out_6/draw_image'
# folder2_path = '/home/ljj/data/valid_result/out_6/images'


else_folder = '/home/ljj/data/people/valid_result/images1'

files1 = glob.glob(folder1_path+'/**/*.jpg', recursive=True)

num = 0
import os
# print(files1)
for file in tqdm(files1):
    subfile = file.replace(folder1_path, '')
    # dup_file = folder2_path + subfile
    # if os.path.isfile(dup_file):
    raw_file = folder2_path + subfile
    # if os.path.isfile(dup_file):
    save_path = Path(else_folder+subfile)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(raw_file, (else_folder+ subfile)) 
    num +=1

print(num)
