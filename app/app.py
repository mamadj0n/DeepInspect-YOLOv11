import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
import os
from pathlib import Path
import json
from ultralytics import YOLO

# ==========================================
# تنظیمات صفحه
# ==========================================
st.set_page_config(
    page_title="AI Defect Detection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# کلاس مدیریت مدل
# ==========================================
class ModelManager:
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
        return cls._instance
    
    def get_model(self, model_path='best.pt'):
        if self._model is None:
            with st.spinner("🔄 Loading model..."):
                self._model = YOLO(model_path)
        return self._model

# ==========================================
# توابع کمکی
# ==========================================
def process_image(model, image, conf_threshold, iou_threshold):
    """پردازش یک تصویر"""
    results = model(image, conf=conf_threshold, iou=iou_threshold)
    
    # استخراج نتایج
    detections = []
    if results[0].boxes is not None:
        for box in results[0].boxes:
            detections.append({
                'class': model.names[int(box.cls)],
                'confidence': float(box.conf),
                'bbox': box.xyxy.tolist()[0]
            })
    
    # رسم روی تصویر
    annotated_img = results[0].plot()
    annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
    
    return annotated_img, detections

def process_video(model, video_path, conf_threshold, iou_threshold):
    """پردازش ویدیو"""
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # ایجاد فایل موقت برای خروجی
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    output_path = temp_file.name
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    processed_frames = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # پردازش فریم
        results = model(frame, conf=conf_threshold, iou=iou_threshold)
        annotated_frame = results[0].plot()
        
        # ذخیره فریم
        out.write(annotated_frame)
        
        # به‌روزرسانی پیشرفت
        processed_frames += 1
        progress = processed_frames / frame_count
        progress_bar.progress(progress)
        status_text.text(f"Processing: {processed_frames}/{frame_count} frames")
    
    cap.release()
    out.release()
    progress_bar.empty()
    status_text.empty()
    
    return output_path

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
    .detection-info {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
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
    
    # تنظیمات مدل
    st.markdown("### Model Parameters")
    model_path = st.text_input("Model Path", value="best.pt")
    
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
    
    # بارگذاری مدل
    model_manager = ModelManager()
    try:
        model = model_manager.get_model(model_path)
        st.success("✅ Model loaded successfully!")
        st.info(f"📌 Model: {model_path}")
        st.info(f"📋 Classes: {len(model.names)}")
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
    
    with col2:
        st.markdown("### 📥 Detection Result")
        if uploaded_file is not None:
            if st.button("🔍 Detect Defects", key="detect_single"):
                # تبدیل به numpy array
                image_np = np.array(image)
                
                # پردازش
                with st.spinner("Detecting defects..."):
                    annotated_img, detections = process_image(
                        model, image_np, conf_threshold, iou_threshold
                    )
                
                # نمایش نتیجه
                st.image(annotated_img, caption="Detection Result", use_column_width=True)
                
                # نمایش اطلاعات
                if detections:
                    st.markdown(f"### ✅ Found {len(detections)} defects")
                    
                    # نمایش جزئیات
                    with st.expander("📋 Detection Details"):
                        st.json(detections)
                    
                    # نمایش جدول
                    df_data = []
                    for d in detections:
                        df_data.append({
                            'Class': d['class'],
                            'Confidence': f"{d['confidence']:.2%}",
                            'BBox': f"[{d['bbox'][0]:.0f}, {d['bbox'][1]:.0f}, {d['bbox'][2]:.0f}, {d['bbox'][3]:.0f}]"
                        })
                    st.dataframe(df_data, use_container_width=True)
                else:
                    st.info("✅ No defects detected!")
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
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, file in enumerate(uploaded_files):
                status_text.text(f"Processing {idx+1}/{len(uploaded_files)}: {file.name}")
                
                image = Image.open(file)
                image_np = np.array(image)
                annotated_img, detections = process_image(
                    model, image_np, conf_threshold, iou_threshold
                )
                
                results.append({
                    'name': file.name,
                    'image': annotated_img,
                    'detections': detections,
                    'count': len(detections)
                })
                
                progress_bar.progress((idx + 1) / len(uploaded_files))
            
            progress_bar.empty()
            status_text.empty()
            
            # نمایش نتایج در گالری
            cols = st.columns(3)
            for idx, result in enumerate(results):
                with cols[idx % 3]:
                    st.image(result['image'], caption=f"{result['name']} ({result['count']} defects)", use_column_width=True)
            
            # نمایش خلاصه
            st.markdown("### 📊 Summary")
            summary_data = []
            for r in results:
                summary_data.append({
                    'Image': r['name'],
                    'Defects Found': r['count'],
                    'Status': '✅' if r['count'] > 0 else '✅ No Defects'
                })
            st.dataframe(summary_data, use_container_width=True)

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
            # ذخیره ویدیو موقت
            temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
            temp_video.write(video_file.read())
            video_path = temp_video.name
            
            st.video(video_path)
    
    with col2:
        st.markdown("### 📥 Processed Video")
        if video_file is not None:
            if st.button("🎥 Process Video", key="detect_video"):
                try:
                    with st.spinner("Processing video... This may take a while."):
                        output_path = process_video(
                            model, video_path, conf_threshold, iou_threshold
                        )
                    
                    st.success("✅ Video processed successfully!")
                    
                    # نمایش ویدیو
                    with open(output_path, 'rb') as f:
                        video_bytes = f.read()
                    st.video(video_bytes)
                    
                    # پاک کردن فایل‌های موقت
                    os.unlink(video_path)
                    os.unlink(output_path)
                    
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
        Built with ❤️ using YOLO and Streamlit | Powered by Hugging Face Spaces
    </div>
""", unsafe_allow_html=True)
