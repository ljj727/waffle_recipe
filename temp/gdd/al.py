import tqdm
import cv2

from pathlib import Path
from groundingdino.util.inference import Model
from waffle_hub.dataset import Dataset
from waffle_utils.file import io, search


class GDino:
    def __init__(self, config):
        self.config = config
        self.interval = config.INTERVAL

        config_file = "wafflow/gdd/GroundingDino_SwinT_OGC.py"
        checkpoint_path = "wafflow/gdd/groundingdino_swint_ogc.pth"

        self.text_prompts = [prompt.lower() for prompt in config.TEXT_PROMPTS]
        self.text_prompt = " . ".join(self.text_prompts) + " ."

        class_names = config.CLASS_NAMES
        class2id = {name: i for i, name in enumerate(class_names)}
        id2class = {i: name for name, i in class2id.items()}

        self.box_threshold = config.BOX_THRESHOLD
        self.text_threshold = config.TEXT_THRESHOLD

        # device
        self.device = "cpu" if config.DEVICE == "cpu" else f"cuda:{config.DEVICE}"
        # device = "cpu"

        # directory
        self.source_dir = Path(config.LOCAL_DATA_PATH)

        # load model
        self.model = Model(config_file, checkpoint_path, self.device)

        # coco format
        self.coco = {
            "categories": [
                {"id": i + 1, "name": c, "supercategory": "object"} for i, c in id2class.items()
            ],
            "images": [],
            "annotations": [],
        }
        self.image_id = 1
        self.annotation_id = 1

        self.set_data()
    
    def set_data(self):
        if self.config.DATA_TYPE == "video":
            self.videos = search.get_video_files(self.source_dir)
        elif self.config.DATA_TYPE == "image":
            self.image_files = search.get_image_files(self.source_dir)
        
    def video_to_wd(self):
        for video in self.videos:
            video_path = Path(video)
            cap = cv2.VideoCapture(str(video_path))
            print(f"video: {video_path}")
            frame_dir = Path(self.config.LOCAL_DATA_PATH, video_path.stem)
            io.make_directory(frame_dir)
            frame_id = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                if frame_id % self.interval == 0:
                    frame_path = frame_dir / f"{frame_id:06d}.jpg"
                    save_check = self.gdd(frame, frame_path)
                    if save_check:
                        cv2.imwrite(str(frame_path), frame)
                        print(f"save_{frame_path}")
                frame_id += 1
            cap.release()

        io.save_json(self.coco, self.source_dir / "coco.json", create_directory=True)

        # Dataset.from_coco(
        #     name=self.config.NEW_DATASET_NAME,
        #     task="object_detection",
        #     coco_file=self.source_dir / "coco.json",
        #     coco_root_dir=self.source_dir,
        #     root_dir=self.config.WAFFLE_DATASET_ROOT_DIR,
        # )

    def image_to_wd(self):
        pass

    def gdd(self, image, path):
        h, w, _ = image.shape
        detections, phrases = self.model.predict_with_caption(
            image=image,
            caption=self.text_prompt,
            box_threshold=self.box_threshold,
            text_threshold=self.text_threshold
        )
        if len(detections) == 0:
            return None
        
        file_name = Path(path).relative_to(self.source_dir)
        self.coco["images"].append(
            {
                "id": int(self.image_id),
                "file_name": str(file_name),
                "width": int(w),
                "height": int(h),
            }
        )
        boxes = detections.xyxy
        labels = phrases
        scores = detections.confidence

        for box, label_id, score in zip(boxes, labels, scores):
            self.coco["annotations"].append(
                {
                    "id": self.annotation_id,
                    "image_id": self.image_id,
                    "category_id": 1,
                    "bbox": box.tolist(),
                    "score": float(score), ## TODO: fix score issue (CVAT) 진짜 모르겠음
                }
            )
            self.annotation_id += 1
        self.image_id += 1

        return True
    
    def gdd_to_wd(self):
        if self.config.DATA_TYPE == "video":
            self.video_to_wd()
        elif self.config.DATA_TYPE == "image":
            self.image_to_wd()