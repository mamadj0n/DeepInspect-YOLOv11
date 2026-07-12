from pathlib import Path

# ==========================================
# Paths Configuration
# ==========================================
# مسیرها را برای اجرای لوکال تنظیم کنید
DATA_ROOT = Path("./dataset/mvtec-ad")
OUTPUT_ROOT = Path("./yolo_dataset_defect_only")

# ==========================================
# Defect Mapping Configuration
# ==========================================
DEFECT_MERGE_MAP = {
    'broken_large': 'broken',
    'broken_small': 'broken',
    'cut_lead': 'cut',
    'cut_inner_insulation': 'cut',
    'missing_wire': 'missing',
    'missing_cable': 'missing',
    'poke_insulation': 'poke',
    'bent_lead': 'bent',
    'bent_wire': 'bent',
    'faulty_imprint': 'print',
    'metal_contamination': 'contamination',
    'glue_strip': 'glue',
    'squeezed_teeth': 'squeezed',
    'split_teeth': 'split',
    'broken_teeth': 'broken',
    'fabric_border': 'fabric',
    'fabric_interior': 'fabric',
    'manipulated_front': 'manipulated',
    'scratch_head': 'scratch',
    'scratch_neck': 'scratch',
    'scratch_side': 'scratch',
    'thread_side': 'thread',
    'thread_top': 'thread',
    'pill_type': 'type',
    'gray_stroke': 'stroke',
    'color': 'color',
}

# ==========================================
# YOLO Training Configuration
# ==========================================
TRAIN_CONFIG = {
    'data': str(OUTPUT_ROOT / "dataset.yaml"),
    'model': "yolo11m.pt",
    'epochs': 75,
    'patience': 50,
    'batch': 24, 
    'imgsz': 640,
    'workers': 4,
    'device': 0, # بسته به سخت‌افزار لوکال تنظیم شود
    'amp': True,
    'cache': True,  
    'project': "mvtec_defect_detection",
    'name': "yolov11m_phase3",
    'exist_ok': True,
    'pretrained': True,
    'optimizer': "auto",
    'cos_lr': True,
    'label_smoothing': 0.0,
    'dropout': 0.0,
    'seed': 42,
    'plots': True,
    'save': True,
    'resume': False
}

# ==========================================
# Evaluation Configuration
# ==========================================
EVAL_MODEL_PATH = "runs/detect/mvtec_defect_detection/yolov11m_phase3/weights/best.pt"
