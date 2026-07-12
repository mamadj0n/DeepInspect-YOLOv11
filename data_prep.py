import json
import shutil
import logging
from pathlib import Path
from typing import Dict, List
import cv2
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from config import DATA_ROOT, OUTPUT_ROOT
from utils import mask_to_bboxes, bbox_to_yolo, validate_bbox, get_defect_type

# تنظیم لاگر
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MVTecDefectDatasetBuilder:
    def __init__(self, data_root: Path, output_root: Path):
        self.data_root = data_root
        self.output_root = output_root
        self.defect_to_id: Dict[str, int] = {}
        self.id_to_defect: Dict[int, str] = {}
        self.metadata: Dict[str, Dict] = {}
        self.class_counts: Dict[str, int] = {}
        self.total_images = 0
        self.total_bboxes = 0
        self.corrupted = []
        self.records = []

    def _get_defect_id(self, defect: str) -> int:
        if defect not in self.defect_to_id:
            new_id = len(self.defect_to_id)
            self.defect_to_id[defect] = new_id
            self.id_to_defect[new_id] = defect
        return self.defect_to_id[defect]

    def _process_category(self, category: str):
        cat_path = self.data_root / category
        test_path = cat_path / 'test'
        gt_path = cat_path / 'ground_truth'
        
        if not test_path.exists() or not gt_path.exists():
            logger.warning(f"دسته {category} ناقص است، رد می‌شود.")
            return

        for defect_dir in test_path.iterdir():
            if not defect_dir.is_dir() or defect_dir.name == 'good':
                continue
            defect_type = get_defect_type(defect_dir.name)
            gt_defect_path = gt_path / defect_dir.name
            if not gt_defect_path.exists():
                continue

            for img_path in defect_dir.glob("*"):
                if img_path.suffix.lower() not in ['.png', '.jpg', '.jpeg']:
                    continue
                
                mask_path = gt_defect_path / (img_path.stem + ".png")
                if not mask_path.exists():
                    mask_path = gt_defect_path / (img_path.stem + "_mask.png")
                if not mask_path.exists():
                    continue

                img = cv2.imread(str(img_path))
                if img is None:
                    self.corrupted.append(str(img_path))
                    continue
                h, w = img.shape[:2]

                pixel_bboxes = mask_to_bboxes(str(mask_path))
                if not pixel_bboxes:
                    continue

                yolo_bboxes = []
                for pbbox in pixel_bboxes:
                    xc, yc, bw, bh = bbox_to_yolo(pbbox, w, h)
                    if validate_bbox(xc, yc, bw, bh):
                        yolo_bboxes.append((xc, yc, bw, bh))
                if not yolo_bboxes:
                    continue

                defect_id = self._get_defect_id(defect_type)
                self.class_counts[defect_type] = self.class_counts.get(defect_type, 0) + 1
                self.total_bboxes += len(yolo_bboxes)

                self.metadata[str(img_path)] = {
                    'object': category,
                    'defect': defect_type,
                    'defect_id': defect_id
                }

                self.records.append({
                    'image_path': str(img_path),
                    'defect_id': defect_id,
                    'bboxes': yolo_bboxes,
                    'image_width': w,
                    'image_height': h
                })
                self.total_images += 1

    def build(self):
        logger.info("🚀 شروع اسکن دیتاست MVTec...")
        self.output_root.mkdir(parents=True, exist_ok=True)
        categories = [d for d in self.data_root.iterdir() if d.is_dir() and not d.name.startswith('.')]
        
        for cat in tqdm(categories, desc="پردازش دسته‌ها"):
            self._process_category(cat.name)

        with open(self.output_root / 'metadata.json', 'w') as f:
            json.dump(self.metadata, f, indent=2)

        with open(self.output_root / 'defect_class_mapping.json', 'w') as f:
            json.dump(self.defect_to_id, f, indent=2)

        return self.records

def split_and_write_yolo_stratified(records: List[Dict], output_root: Path, split_ratio=0.8):
    labels = [rec['defect_id'] for rec in records]
    train_records, val_records = train_test_split(
        records, train_size=split_ratio, random_state=42, stratify=labels
    )

    for split, recs in [('train', train_records), ('val', val_records)]:
        img_dir = output_root / 'images' / split
        label_dir = output_root / 'labels' / split
        img_dir.mkdir(parents=True, exist_ok=True)
        label_dir.mkdir(parents=True, exist_ok=True)

        for rec in tqdm(recs, desc=f"نوشتن {split}"):
            src_img = Path(rec['image_path'])
            dst_img = img_dir / src_img.name
            
            if dst_img.exists():
                dst_img = img_dir / f"{src_img.parent.parent.name}_{src_img.parent.name}_{src_img.name}"
            shutil.copy2(str(src_img), str(dst_img))

            label_file = label_dir / (dst_img.stem + ".txt")
            with open(label_file, 'w') as f:
                for xc, yc, bw, bh in rec['bboxes']:
                    f.write(f"{rec['defect_id']} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

    return len(train_records), len(val_records)

def generate_dataset_yaml(output_root: Path, defect_to_id: Dict[str, int]):
    nc = len(defect_to_id)
    names = [None] * nc
    for defect, idx in defect_to_id.items():
        names[idx] = defect

    yaml_content = f"""
path: {str(output_root.absolute())}
train: images/train
val: images/val

nc: {nc}
names: {names}
"""
    (output_root / 'dataset.yaml').write_text(yaml_content.strip())

if __name__ == "__main__":
    builder = MVTecDefectDatasetBuilder(DATA_ROOT, OUTPUT_ROOT)
    records = builder.build()

    train_count, val_count = split_and_write_yolo_stratified(records, OUTPUT_ROOT, split_ratio=0.8)
    generate_dataset_yaml(OUTPUT_ROOT, builder.defect_to_id)

    logger.info("✅ فاز آماده‌سازی دیتاست با موفقیت کامل شد!")
