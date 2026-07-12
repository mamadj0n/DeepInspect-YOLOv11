import os
import glob
import json
import pandas as pd
from ultralytics import YOLO

# وارد کردن متغیرها از فایل تنظیمات
from config import DATA_ROOT, EVAL_MODEL_PATH

class MVTecEvaluator:
    """
    A professional evaluation module for YOLO-based defect detection on the MVTec AD dataset.
    """
    def __init__(self, model_path: str, dataset_root: str, conf_threshold: float = 0.5):
        self.dataset_root = dataset_root
        self.conf_threshold = conf_threshold
        
        print(f"[*] Loading model from {model_path}...")
        self.model = YOLO(model_path)
        self.results_data = []

    def evaluate(self):
        """Scans the dataset, runs batched inference, and extracts rich metadata."""
        print(f"[*] Starting evaluation with Confidence Threshold: {self.conf_threshold}")
        
        # در اینجا فرض بر این است که ساختار پوشه دیتای خام ارزیابی می‌شود
        categories = [d for d in os.listdir(self.dataset_root) if os.path.isdir(os.path.join(self.dataset_root, d))]

        for category in categories:
            test_dir = os.path.join(self.dataset_root, category, "test")
            if not os.path.exists(test_dir):
                continue
                
            print(f"📦 Processing: {category}")
            defect_types = [d for d in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, d))]
            
            for defect_type in defect_types:
                folder_path = os.path.join(test_dir, defect_type)
                image_paths = glob.glob(os.path.join(folder_path, "*.[jp][pn][g]"))
                
                if not image_paths:
                    continue
                
                # Batched inference for performance
                results = self.model.predict(image_paths, conf=self.conf_threshold, verbose=False)
                
                for img_path, res in zip(image_paths, results):
                    self._process_single_result(category, defect_type, img_path, res)

        print("[*] Evaluation loop completed.")

    def _process_single_result(self, category, actual_defect, img_path, res):
        """Extracts and formats bounding boxes, confidence, and status from a single prediction."""
        actual_status = "Healthy" if actual_defect == "good" else "Defective"
        num_boxes = len(res.boxes)
        predicted_status = "Healthy" if num_boxes == 0 else "Defective"
        
        predictions = []
        predicted_defects = set()
        
        for box in res.boxes:
            label = res.names[int(box.cls[0])]
            conf = float(box.conf[0])
            bbox = box.xyxy[0].tolist()
            
            predicted_defects.add(label)
            predictions.append({
                "label": label,
                "conf": round(conf, 4),
                "bbox": [round(coord, 2) for coord in bbox]
            })
            
        predictions = sorted(predictions, key=lambda x: x['conf'], reverse=True)
        
        if actual_status == "Healthy":
            defect_match = (predicted_status == "Healthy")
        else:
            defect_match = actual_defect in predicted_defects

        self.results_data.append({
            "Image": os.path.basename(img_path),
            "Category": category,
            "Actual_Status": actual_status,
            "Predicted_Status": predicted_status,
            "Actual_Defect": actual_defect,
            "Predicted_Defects": ", ".join(predicted_defects) if predicted_defects else "None",
            "Detection_Correct": actual_status == predicted_status,
            "Classification_Correct": defect_match,
            "Inference_Time_ms": round(res.speed.get('inference', 0.0), 2),
            "Predictions_JSON": json.dumps(predictions) 
        })

    def calculate_metrics(self):
        """Calculates TP, FP, TN, FN, Precision, Recall, and F1-Score."""
        df = pd.DataFrame(self.results_data)
        if df.empty:
            print("[!] No data to calculate metrics.")
            return None

        TP = ((df['Actual_Status'] == 'Defective') & (df['Predicted_Status'] == 'Defective')).sum()
        TN = ((df['Actual_Status'] == 'Healthy') & (df['Predicted_Status'] == 'Healthy')).sum()
        FP = ((df['Actual_Status'] == 'Healthy') & (df['Predicted_Status'] == 'Defective')).sum()
        FN = ((df['Actual_Status'] == 'Defective') & (df['Predicted_Status'] == 'Healthy')).sum()

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        print("\n" + "="*40)
        print("📊 OVERALL DETECTION METRICS (Binary)")
        print("="*40)
        print(f"True Positives (TP)  : {TP}")
        print(f"True Negatives (TN)  : {TN}")
        print(f"False Positives (FP) : {FP} ⚠️ (Healthy flagged as Defective)")
        print(f"False Negatives (FN) : {FN} 🚨 (Defect missed!)")
        print("-" * 40)
        print(f"Precision            : {precision:.4f}")
        print(f"Recall               : {recall:.4f}")
        print(f"F1-Score             : {f1:.4f}")
        
        class_acc = df['Classification_Correct'].mean() * 100
        print(f"\n🎯 Defect Classification Accuracy: {class_acc:.2f}%\n")
        
        return df

    def save_reports(self, csv_path="evaluation_report.csv"):
        """Saves the rich dataset to a CSV file."""
        if not self.results_data:
            print("[!] No data to save.")
            return

        df = pd.DataFrame(self.results_data)
        df.to_csv(csv_path, index=False)
        print(f"💾 Report saved successfully to {csv_path}")


if __name__ == "__main__":
    evaluator = MVTecEvaluator(
        model_path=EVAL_MODEL_PATH, 
        dataset_root=str(DATA_ROOT), 
        conf_threshold=0.5
    )
    
    evaluator.evaluate()
    df_results = evaluator.calculate_metrics()
    
    if df_results is not None:
        evaluator.save_reports("final_evaluation_report.csv")
