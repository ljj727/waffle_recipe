from pycocotools.coco import COCO
import os
from pathlib import Path
from tqdm import tqdm
import json

# data_dir = '/home/ljj/data/superb/KISA-DATASET'

data_dir = '/home/ljj/data/people/valid_result'
annotation_file = os.path.join(data_dir, 'coco.json')

coco = COCO(annotation_file)

# output_dir = f"{data_dir}/draw_image"
# os.makedirs(output_dir, exist_ok=True)
num=0

coco_copy = coco.dataset
images = coco.dataset['images']
new_annos = []
new_images = []
for i, img in tqdm(enumerate(images)):
    file_path = f"{data_dir}/images/{img['file_name']}"
    file_path = file_path[:-4] + '.jpg'

    anns_ids = coco.getAnnIds(imgIds=img['id'])
    anns = coco.loadAnns(anns_ids)
    if os.path.isfile(file_path):
        filename = Path(file_path).name
        img['file_name'] = filename
        new_images.append(img)
        new_annos += anns
        num+=1

coco_copy['images'] = new_images
coco_copy['annotations'] = new_annos


# 모든 이미지에 대한 주석 그리기
print(num)

with open(f"{data_dir}/coco_new.json", "w", encoding="utf-8") as outfile:
    json.dump(coco.dataset, outfile, ensure_ascii=False)