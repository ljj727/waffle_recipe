import glob
from pathlib import Path
import cv2
import shutil
import os

path = '/home/ljj/waffle/datasets/HelmetDataset_v1.0.0/exports/YOLO/train/'

images = glob.glob(f"{path}/**/*.png", recursive=True)


print(len(images))
remove_num = 0
for image in images:
    p = Path(image)
    img = cv2.imread(image)
    h, w = img.shape[:2]
    if h < 40 or w < 50:
        remove_num += 1
        os.remove(p)
    

print(remove_num)


