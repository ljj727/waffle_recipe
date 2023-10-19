from waffle_utils.file import io
from pycocotools.coco import COCO
import glob
import json
import datetime
import os

test_coco = '/home/ljj/data/people/YNCC_PeopleDataset_v1.0.1/coco.json'
coco = COCO(test_coco)
save_img_path = '/home/ljj/data/superb/App_Add/images'



img_path = '/home/ljj/data/superb/hard/images'
label_path = '/home/ljj/data/superb/hard/labels'

superb_project_path = f"{label_path}/project.json"
superb_project = io.load_json(superb_project_path)

superb_cats = {}

cats_id = 1

data_type = superb_project['data_type']

categories = []
images = []
annotations = []


#superb to coco category
for cats in superb_project['object_detection']['object_classes']:
    category = cats['name']
    superb_cats[category] = cats_id
    category_info ={
        "id": cats_id,
        "supercategory": category,
        "name": category
    }

    categories.append(category_info)
    cats_id += 1

#superb to coco images

superb_metas = glob.glob(f"{label_path}/meta/**/*.json", recursive=True)
image_id = 1
annotation_id = 1

for meta_path in superb_metas:
    image_ids = []
    meta = io.load_json(meta_path)
    anno_data = io.load_json(f"{label_path}/{meta['label_path'][0]}")

    file_name = str(meta['data_key']).lstrip('/')
    image_path = f"{img_path}/{file_name}"

    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"{image_path} does not exist.")
    
    image_info = {
        'id' : image_id,
        "file_name": file_name,
        "width": meta['image_info']['width'],
        "height": meta['image_info']['height'],
        'original_file_name': file_name,
        'date_captured' : datetime.datetime.now().isoformat(),
        }
    images.append(image_info)
    for label_info in anno_data['objects']:
        class_name = label_info['class_name']
        if class_name =='person':
            coord = label_info['annotation']['coord']

            annotation_info = {
                "id": annotation_id,
                "image_id": image_id,
                "bbox": [coord['x'], coord['y'], coord['width'], coord['height']],
                'area': 0,
                'iscrowd': 0,
                "category_id": superb_cats[class_name]
            }
            annotation_id += 1
            annotations.append(annotation_info)
    image_id += 1

coco.dataset['categories'] = categories        
coco.dataset['images'] = images        
coco.dataset['annotations'] = annotations        
with open(f"{img_path}/coco.json", "w", encoding="utf-8") as outfile:
    json.dump(coco.dataset, outfile, ensure_ascii=False)



        






