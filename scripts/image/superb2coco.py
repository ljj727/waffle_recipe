from waffle_utils.file import io
from pycocotools.coco import COCO
import glob
import json
import datetime

test_coco = '/home/ljj/data/people/PeopleDataset_AIHUB_Metro_v1.0.0/coco.json'
coco = COCO(test_coco)
save_img_path = '/home/ljj/data/superb/asdf'



img_path = '/home/ljj/data/superb/Western_Power'
label_path = '/home/ljj/data/superb/Western_Power 2023-05-18 13_24_57'

superb_project_path = f"{label_path}/project.json"
superb_project = io.load_json(superb_project_path)

superb_cats = {}

cats_id = 1

data_type = superb_project['data_type']

categories = []
images = []
annotations = []


#superb to coco category
for cats in superb_project['object_tracking']['object_classes']:
    category = cats['name']
    # if category != 'person' and category != 'object':
    superb_cats[category] = cats_id
    category_info ={
        "id": cats_id,
        "supercategory": 'object',
        "name": category
    }

    categories.append(category_info)
    cats_id += 1

#superb to coco images

superb_metas = glob.glob(f"{label_path}/meta/**/*.json", recursive=True)
annotation_id = 0
image_id = 0

for meta_path in superb_metas:
    ids = []
    meta = io.load_json(meta_path)
    anno_data = io.load_json(f"{label_path}/{meta['label_path'][0]}")
    if meta['image_info'] and anno_data.get('objects'):
        for filename in meta['frames']:
            subfilename = f"{meta['data_key']}/{filename}"
            file_path = f"{img_path}/{subfilename}"
            save_path = f"{save_img_path}/{subfilename}"
            ids.append(image_id)
            image_id += 1
            # io.copy_file(file_path, save_path, create_directory=True)
            image_info = {
                'id': image_id,
                'file_name': subfilename,
                'width': meta['image_info']['width'],
                'height': meta['image_info']['height'],
                'original_file_name': filename,
                'date_captured' : datetime.datetime.now().isoformat(),
            }
            images.append(image_info)
    
        for anns in anno_data['objects']:
            class_name = anns['class_name']
            # if class_name !='person':
            for frame in anns['frames']:
                coord = frame['annotation']['coord']

                annotation_info = {
                    'id' : annotation_id,
                    'image_id': ids[frame['num']]+1,
                    "bbox": [coord['x'], coord['y'], coord['width'], coord['height']],
                    'area': 0,
                    'iscrowd': 0,
                    "category_id": superb_cats[class_name]
                }
                annotation_id += 1
                annotations.append(annotation_info)
            # else:
            #     print(class_name)
        
coco.dataset['categories'] = categories        
coco.dataset['images'] = images        
coco.dataset['annotations'] = annotations        
with open(f"{img_path}/coco.json", "w", encoding="utf-8") as outfile:
    json.dump(coco.dataset, outfile, ensure_ascii=False)



        






