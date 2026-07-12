logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DefectInference:
    def __init__(self, model_path: str, conf_threshold: float = 0.25, iou_threshold: float = 0.45):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        
        # استخراج نام کلاس‌ها مستقیماً از خود مدل
        self.id_to_defect = {i: name for i, name in enumerate(self.model.names.values())}
        logger.info(f"✅ مدل بارگذاری شد: {model_path}")

    def predict_image(self, image_path: str, save_result: bool = True, output_dir: str = "predictions") -> Dict:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"تصویر خوانده نشد: {image_path}")
        
        h, w = img.shape[:2]
        start_time = time.time()
        results = self.model(image_path, conf=self.conf_threshold, iou=self.iou_threshold, verbose=False)
        inference_time = (time.time() - start_time) * 1000  
        
        predictions = []
        for r in results:
            boxes = r.boxes
            if boxes is None: continue
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                defect_name = self.id_to_defect.get(cls_id, f"class_{cls_id}")
                
                predictions.append({
                    'defect': defect_name,
                    'confidence': conf,
                    'bbox': [x1, y1, x2 - x1, y2 - y1],
                    'class_id': cls_id
                })
        
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        
        result = {
            'image_path': image_path,
            'inference_time_ms': inference_time,
            'num_detections': len(predictions),
            'predictions': predictions
        }
        
        if save_result and predictions:
            output_path = self._draw_annotations(img, predictions, image_path, output_dir)
            result['annotated_image'] = output_path
            
        return result
    
    def _draw_annotations(self, img: np.ndarray, predictions: List[Dict], image_path: str, output_dir: str) -> str:
        os.makedirs(output_dir, exist_ok=True)
        img_copy = img.copy()
        
        for pred in predictions:
            x, y, w, h = pred['bbox']
            conf = pred['confidence']
            defect = pred['defect']
            
            color = (0, 0, 255) if defect in ['crack', 'broken'] else (0, 255, 0)
            
            cv2.rectangle(img_copy, (x, y), (x+w, y+h), color, 2)
            label = f"{defect} | {conf:.2f}"
            (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(img_copy, (x, y - text_h - 10), (x + text_w, y), color, -1)
            cv2.putText(img_copy, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        output_path = Path(output_dir) / f"annotated_{Path(image_path).name}"
        cv2.imwrite(str(output_path), img_copy)
        return str(output_path)

    def predict_video(self, video_path: str, output_dir: str = "predictions", frame_interval: int = 1) -> str:
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        os.makedirs(output_dir, exist_ok=True)
        output_video_path = Path(output_dir) / f"annotated_{Path(video_path).name}"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(str(output_video_path), fourcc, fps, (width, height))
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret: break
            
            if frame_count % frame_interval == 0:
                temp_path = Path(output_dir) / f"temp_frame.jpg"
                cv2.imwrite(str(temp_path), frame)
                result = self.predict_image(str(temp_path), save_result=False)
                
                if result['predictions']:
                    for pred in result['predictions']:
                        x, y, w, h = pred['bbox']
                        label = f"{pred['defect']}|{pred['confidence']:.2f}"
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
                
                if temp_path.exists(): temp_path.unlink()
            
            out.write(frame)
            frame_count += 1
            
        cap.release()
        out.release()
        return str(output_video_path)
