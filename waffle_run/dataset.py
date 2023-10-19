
# from waffle_hub.dataset import Dataset

# root_path ='/home/ljj/waffle/result/out_8_com'
# name="PeopleDataset_valid_v1.0.5"
# dataset = Dataset.from_coco(
#         name=name,
#         task = "object_detection",
#         coco_file = f'{root_path}/coco.json',
#         coco_root_dir = f'{root_path}/images',
#         )
# dataset = Dataset.load(name)
# dataset.extract_by_categories("FireDataset_KISA_v2.0.1", category_ids=[3,4])
# dataset.draw_annotations()
# dataset.split(
#   train_ratio = 0.99,
#   val_ratio = 0.01,
# )
# dataset.export("ULTRALYTICS")
from waffle_hub.dataset import Dataset

root_path ='/home/ljj/data/people/valid_result'
name="PeopleDataset_FalldownNG_v1.0.0"
dataset = Dataset.from_coco(
        name=name,
        task = "object_detection",
        coco_file=f'{root_path}/coco.json',
        coco_root_dir= f'{root_path}/images'
        )
# dataset = Dataset.load(name)
# dataset.extract_by_categories("FireDataset_KISA_v2.0.1", category_ids=[3,4])
# dataset.draw_annotations()
# dataset.split(
#   train_ratio = 0.99,
#   val_ratio = 0.01,
# )
# dataset.export("ULTRALYTICS")