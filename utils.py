import cv2
import numpy as np
from typing import List, Tuple
from config import DEFECT_MERGE_MAP

def mask_to_bboxes(mask_path: str) -> List[Tuple[int, int, int, int]]:
    """تبدیل ماسک به لیست باکس‌های محصور (pixel coordinates)."""
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if mask is None:
        return []
    unique_vals = np.unique(mask)
    bboxes = []
    for val in unique_vals:
        if val == 0:
            continue
        inst_mask = (mask == val).astype(np.uint8)
        contours, _ = cv2.findContours(inst_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if len(cnt) < 3:
                continue
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 0 and h > 0:
                bboxes.append((x, y, x + w, y + h))
    return bboxes

def bbox_to_yolo(bbox_pixel, img_w, img_h):
    """تبدیل باکس پیکسلی به فرمت YOLO (xc, yc, w, h نرمال‌شده)."""
    x_min, y_min, x_max, y_max = bbox_pixel
    xc = (x_min + x_max) / (2.0 * img_w)
    yc = (y_min + y_max) / (2.0 * img_h)
    w = (x_max - x_min) / img_w
    h = (y_max - y_min) / img_h
    return max(0.0, min(1.0, xc)), max(0.0, min(1.0, yc)), max(0.0, min(1.0, w)), max(0.0, min(1.0, h))

def validate_bbox(xc, yc, w, h):
    return (0.0 < w <= 1.0) and (0.0 < h <= 1.0) and (0.0 <= xc <= 1.0) and (0.0 <= yc <= 1.0)

def get_defect_type(defect_name: str) -> str:
    """بازگرداندن نوع عیب نرمال‌شده با استفاده از نگاشت."""
    return DEFECT_MERGE_MAP.get(defect_name, defect_name)
