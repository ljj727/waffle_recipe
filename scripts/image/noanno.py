from pycocotools.coco import COCO
import os
from pathlib import Path
from tqdm import tqdm
import cv2


data_dir = '/home/ljj/data/people/valid_result'
annotation_file = os.path.join(data_dir, 'coco.json')

coco = COCO(annotation_file)

num = 0

imgs = coco.imgs
imgs = coco.dataset['images']
annotations=[]
a=0
for img in imgs:
    file_path = f"{data_dir}/images/{img['file_name']}"
    file_path = file_path[:-4] + '.jpg'
    if os.path.isfile(file_path): # 1. Check Image File

        anns_ids = coco.getAnnIds(imgIds=img['id'])
        anns = coco.loadAnns(anns_ids)
        a=0
        for i, ann in enumerate(anns):
            x1 = ann['bbox'][0]
            y1 = ann['bbox'][1]
            x2 = ann['bbox'][2] + ann['bbox'][0]
            y2 = ann['bbox'][3] + ann['bbox'][1]
            cond1 = (x1 > 600 and y2 < 400 and len(anns) == 1) # Single
            cond2 = ((x2 < 120 or x1 > 1820) and len(anns) == 1)
            cond3 = ((y1 < 200 or (x1>600 and y2 > 400)) and len(anns) == 2)
            cond4 = (y2>500)
            if cond4:
                a = 1
                # img = cv2.imread(file_path)
                # cv2.rectangle(img,[int(ann['bbox'][0]), int(ann['bbox'][1])] ,[int(ann['bbox'][0]+ann['bbox'][2]), int(ann['bbox'][1]+ann['bbox'][3])],(255,0,0),5 )
            else:
                annotations.append(ann)

        if a ==1:
            num+=1
            # cv2.imshow('img', img)
            # cv2.waitKey(0)
            # os.remove(file_path)
        # if len(anns) == 0:   # 2. Check Annotation info
        #     # print("No Annotations Image")
        #     print(file_path)
        #     # os.remove(file_path)
        #     num+=1

print('delete image num:', num)
coco.dataset['annotations'] = annotations

import json
with open(f"{data_dir}/coco_new2.json", "w", encoding="utf-8") as outfile:
    json.dump(coco.dataset, outfile, ensure_ascii=False)