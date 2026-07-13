import streamlit as st
import os
import urllib.request
import torch
import logging
import time
import cv2
import numpy as np
from PIL import Image
import tempfile
from pathlib import Path
import json
from typing import List, Dict
from ultralytics import YOLO

# ==========================================
# غیرفعال کردن weights_only برای کل برنامه
# ==========================================
torch.serialization.weights_only_default = False

# ==========================================
# تنظیمات logging
# ==========================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ==========================================
# دانلود مدل
# ==========================================
def ensure_model_exists():
    model_path = "best.pt"
    if not os.path.exists(model_path):
        with st.spinner("📥 Downloading model... Please wait..."):
            url = "https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt"
            try:
                urllib.request.urlretrieve(url, model_path)
                st.success("✅ Model downloaded successfully!")
            except Exception as e:
                st.error(f"❌ Download failed: {e}")
                st.stop()

ensure_model_exists()

# ==========================================
# کلاس DefectInference
# ==========================================
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
            
            # رنگ‌های مختلف برای انواع مختلف defects
            color = (0, 0, 255) if defect in ['crack', 'broken', 'scratch'] else (0, 255, 0)
            
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
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # محاسبه تعداد کل فریم‌ها
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # ریست به ابتدا
        
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
            
            # به‌روزرسانی پیشرفت
            progress = frame_count / total_frames if total_frames > 0 else 0
            progress_bar.progress(min(progress, 1.0))
            status_text.text(f"Processing: {frame_count}/{total_frames} frames")
            
        cap.release()
        out.release()
        progress_bar.empty()
        status_text.empty()
        
        return str(output_video_path)

# ==========================================
# تنظیمات صفحه Streamlit
# ==========================================
st.set_page_config(
    page_title="AI Defect Detection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# استایل‌های CSS
# ==========================================
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        font-size: 3rem;
        margin: 0;
    }
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 0.75rem;
        border: none;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# هدر
# ==========================================
st.markdown("""
    <div class="main-header">
        <h1>🔍 AI Defect Detection</h1>
        <p>Industrial Defect Detection using YOLO</p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# نوار کناری (تنظیمات)
# ==========================================
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    st.markdown("### Model Parameters")
    model_path = "best.pt"
    
    conf_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.25,
        step=0.05,
        help="Minimum confidence score for detections"
    )
    
    iou_threshold = st.slider(
        "IoU Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.45,
        step=0.05,
        help="Intersection over Union threshold"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Stats")
    
    # بارگذاری مدل با کلاس DefectInference
    try:
        if 'detector' not in st.session_state:
            with st.spinner("🔄 Loading model..."):
                st.session_state.detector = DefectInference(
                    model_path=model_path,
                    conf_threshold=conf_threshold,
                    iou_threshold=iou_threshold
                )
        
        detector = st.session_state.detector
        st.success("✅ Model loaded successfully!")
        st.info(f"📌 Model: {model_path}")
        st.info(f"📋 Classes: {len(detector.id_to_defect)}")
        
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

# ==========================================
# تب‌های اصلی
# ==========================================
tab1, tab2, tab3 = st.tabs(["🖼️ Single Image", "📂 Batch Processing", "🎥 Video Analysis"])

# ==========================================
# تب ۱: تصویر تکی
# ==========================================
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=['jpg', 'jpeg', 'png', 'bmp', 'tiff'],
            key="single_image"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Input Image", use_column_width=True)
            
            # ذخیره تصویر موقت
            temp_img = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
            image.save(temp_img.name)
            temp_img_path = temp_img.name
    
    with col2:
        st.markdown("### 📥 Detection Result")
        if uploaded_file is not None:
            if st.button("🔍 Detect Defects", key="detect_single"):
                try:
                    with st.spinner("Detecting defects..."):
                        # به‌روزرسانی تنظیمات مدل
                        detector.conf_threshold = conf_threshold
                        detector.iou_threshold = iou_threshold
                        
                        # پردازش تصویر
                        result = detector.predict_image(temp_img_path, save_result=True, output_dir="predictions")
                        
                        if result['annotated_image']:
                            annotated_img = cv2.imread(result['annotated_image'])
                            annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
                            st.image(annotated_img, caption="Detection Result", use_column_width=True)
                        
                        # نمایش اطلاعات
                        if result['predictions']:
                            st.markdown(f"### ✅ Found {result['num_detections']} defects")
                            st.markdown(f"⏱️ Inference Time: {result['inference_time_ms']:.2f} ms")
                            
                            with st.expander("📋 Detection Details"):
                                st.json(result['predictions'])
                            
                            # نمایش جدول
                            df_data = []
                            for d in result['predictions']:
                                df_data.append({
                                    'Defect': d['defect'],
                                    'Confidence': f"{d['confidence']:.2%}",
                                    'BBox': f"[{d['bbox'][0]}, {d['bbox'][1]}, {d['bbox'][2]}, {d['bbox'][3]}]"
                                })
                            st.dataframe(df_data, use_container_width=True)
                        else:
                            st.info("✅ No defects detected!")
                            
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.info("👈 Please upload an image first")

# ==========================================
# تب ۲: پردازش دسته‌ای
# ==========================================
with tab2:
    st.markdown("### 📤 Upload Multiple Images")
    uploaded_files = st.file_uploader(
        "Choose images...",
        type=['jpg', 'jpeg', 'png', 'bmp', 'tiff'],
        accept_multiple_files=True,
        key="batch_images"
    )
    
    if uploaded_files:
        st.info(f"📎 {len(uploaded_files)} images uploaded")
        
        if st.button("🔍 Process Batch", key="detect_batch"):
            try:
                # به‌روزرسانی تنظیمات مدل
                detector.conf_threshold = conf_threshold
                detector.iou_threshold = iou_threshold
                
                results = []
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, file in enumerate(uploaded_files):
                    status_text.text(f"Processing {idx+1}/{len(uploaded_files)}: {file.name}")
                    
                    # ذخیره تصویر موقت
                    temp_img = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
                    image = Image.open(file)
                    image.save(temp_img.name)
                    
                    # پردازش
                    result = detector.predict_image(temp_img.name, save_result=True, output_dir="predictions")
                    results.append({
                        'name': file.name,
                        'result': result
                    })
                    
                    # پاک کردن فایل موقت
                    os.unlink(temp_img.name)
                    
                    progress_bar.progress((idx + 1) / len(uploaded_files))
                
                progress_bar.empty()
                status_text.empty()
                
                # نمایش نتایج در گالری
                cols = st.columns(3)
                for idx, item in enumerate(results):
                    with cols[idx % 3]:
                        if item['result']['annotated_image']:
                            annotated_img = cv2.imread(item['result']['annotated_image'])
                            annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
                            st.image(annotated_img, caption=f"{item['name']} ({item['result']['num_detections']} defects)", use_column_width=True)
                
                # نمایش خلاصه
                st.markdown("### 📊 Summary")
                summary_data = []
                for item in results:
                    summary_data.append({
                        'Image': item['name'],
                        'Defects Found': item['result']['num_detections'],
                        'Inference Time': f"{item['result']['inference_time_ms']:.2f} ms"
                    })
                st.dataframe(summary_data, use_container_width=True)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ==========================================
# تب ۳: پردازش ویدیو
# ==========================================
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📤 Upload Video")
        video_file = st.file_uploader(
            "Choose a video...",
            type=['mp4', 'avi', 'mov', 'mkv', 'webm'],
            key="video_file"
        )
        
        if video_file is not None:
            temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
            temp_video.write(video_file.read())
            video_path = temp_video.name
            st.video(video_path)
    
    with col2:
        st.markdown("### 📥 Processed Video")
        if video_file is not None:
            if st.button("🎥 Process Video", key="detect_video"):
                try:
                    # به‌روزرسانی تنظیمات مدل
                    detector.conf_threshold = conf_threshold
                    detector.iou_threshold = iou_threshold
                    
                    with st.spinner("Processing video... This may take a while."):
                        output_path = detector.predict_video(video_path, output_dir="predictions")
                    
                    st.success("✅ Video processed successfully!")
                    
                    # نمایش ویدیو
                    with open(output_path, 'rb') as f:
                        video_bytes = f.read()
                    st.video(video_bytes)
                    
                    # پاک کردن فایل‌های موقت
                    os.unlink(video_path)
                    
                except Exception as e:
                    st.error(f"❌ Error processing video: {str(e)}")
        else:
            st.info("👈 Please upload a video first")

# ==========================================
# فوتر
# ==========================================
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em; padding: 1rem 0;">
        Built with ❤️ using YOLO and Streamlit | Powered by Streamlit Cluod | MODSO
    </div>
""", unsafe_allow_html=True)
