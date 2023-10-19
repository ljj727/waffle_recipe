from pycocotools.coco import COCO
import os
from pathlib import Path
from tqdm import tqdm
import shutil

data_dir = '/home/ljj/waffle/result/out_6'
annotation_file = os.path.join(data_dir, 'coco_new.json')

coco = COCO(annotation_file)

# output_dir = f"{data_dir}/draw_image"
# os.makedirs(output_dir, exist_ok=True)
num = 0

imgs = coco.imgs
for img in imgs.values():
    file_path = f"{data_dir}/images/{img['file_name']}"
    if os.path.isfile(file_path): # 1. Check Image File

        anns_ids = coco.getAnnIds(imgIds=img['id'])
        anns = coco.loadAnns(anns_ids)

        if len(anns) == 0:   # 2. Check Annotation info
            print("No Annotations Image")
            os.remove(file_path)
            num+=1

print('delete image num:', num)
