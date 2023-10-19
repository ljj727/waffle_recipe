
import glob
from pathlib import Path
import shutil
from tqdm import tqdm
import os

# 두 폴더의 경로 설정
folder1_path = '/home/ljj/data/superb/KISA-DATASET/KISA/KISA-DATASET'
folder2_path = '/home/ljj/data/superb/raw/images'

files1 = glob.glob(folder1_path+'/**/*.jpg', recursive=True)

num = 0
directories = []
# print(files1)
for file in tqdm(files1):
    subfile = Path(file.replace(folder1_path, ''))
    directories.append(str(subfile.parent))
    # dup_file = folder2_path + subfile
    # if os.path.isdir(dup_file):
    #     print(dup_file)
a = set(directories)
print(len(a))

for d in list(a):
    dup_dir = folder2_path+d
    if os.path.isdir(dup_dir):
        print(dup_dir)
        shutil.rmtree(dup_dir)


print(num)