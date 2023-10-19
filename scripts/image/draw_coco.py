from pycocotools.coco import COCO
import os
from PIL import Image, ImageDraw
from pathlib import Path
from tqdm import tqdm


data_dir = '/home/ljj/data/people/valid_result'
annotation_file = os.path.join(data_dir, 'coco_new2.json')

coco = COCO(annotation_file)

output_dir = f"{data_dir}/draw_image"
os.makedirs(output_dir, exist_ok=True)

#11000
for img_id in tqdm(coco.getImgIds()):
    try:
        cond = 0
        image_info = coco.loadImgs(img_id)[0]
        image_path = os.path.join(data_dir, 'images',  image_info['file_name'])
        image = Image.open(image_path)
        
        annotation_ids = coco.getAnnIds(imgIds=img_id)
        annotations = coco.loadAnns(annotation_ids)

        cond2 = (image_info['height'] != image.size[1]) or (image_info['width'] != image.size[0])
        if cond2:
            cond = 1
        draw = ImageDraw.Draw(image)
        for annotation in annotations:
            bbox = annotation['bbox']

            cond1 = (bbox[0] > image.size[0]) or (bbox[1] > image.size[1])
            cond3 = (bbox[0]+bbox[2]) > image.size[0] or (bbox[1]+bbox[3])> image.size[1]
            if cond1:
                cond = 1
            category = coco.loadCats(annotation['category_id'])[0]['name']
            outline_color = 'red'
            line_width = 4
            x0, y0, width, height = bbox
            x1, y1 = x0 + width, y0 + height
            draw.line([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], fill=outline_color, width=line_width)
            draw.text((x0, y0 - 20), category, fill=outline_color)
        
        if cond:
            pass
        else:
            output_path = os.path.join(output_dir, image_info['file_name'])
            path = Path(output_path).parent
            path.mkdir(parents=True, exist_ok=True)
            image.save(output_path)
    except:
        pass


print("Annotations for all images have been saved.")