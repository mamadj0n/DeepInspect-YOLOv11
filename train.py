import warnings
from ultralytics import YOLO
from config import TRAIN_CONFIG

warnings.filterwarnings('ignore')

def main():
    print("🚀 Initializing YOLOv11 Model for Industrial Defect Detection...")
    model = YOLO(TRAIN_CONFIG['model'])
    
    print("📈 Starting Training Process...")
    results = model.train(**TRAIN_CONFIG)
    
    print("✅ Training Completed Successfully!")

if __name__ == "__main__":
    main()
