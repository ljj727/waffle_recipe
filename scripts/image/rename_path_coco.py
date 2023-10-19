import os
from pycocotools.coco import COCO
from pathlib import Path
import shutil
import json
import tqdm

path = '/home/ljj/data/ison/data/1025_2'
tmp = '1025_2'

annotation_file = os.path.join(path, 'coco_new.json')

coco = COCO(annotation_file)
num = 0

folder = f"{path}/image_new"
os.makedirs(folder, exist_ok=True)
for i, img in tqdm.tqdm(enumerate(coco.imgs.values())):
    suffix = Path(img['file_name']).suffix
    file_path = f"{path}/images/{img['file_name']}"
    # if i % 2000 ==0:
    #     folder = f"{path}/image_new/{i+2}"
    #     # os.makedirs(folder, exist_ok=True)
    #     num=i+2
    copy_name = f"{folder}/{tmp}_{i}{suffix}"
    shutil.copy(file_path, copy_name)
    img['file_name'] = f"{tmp}_{i}{suffix}"

with open(f"{path}/coco_new4.json", "w", encoding="utf-8") as outfile:
    json.dump(coco.dataset, outfile, ensure_ascii=False)