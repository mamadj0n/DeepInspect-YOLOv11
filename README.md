# 🔍 DeepInspect-YOLOv11

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-FF0000?logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)

**Automatic industrial defect detection system using AI and YOLO**

> 🎯 A comprehensive toolkit for accurate and fast industrial defect detection in images and videos

---

## 📋 Description

**DeepInspect-YOLOv11** is a powerful and user-friendly platform for automatic defect recognition in industrial images and videos. It uses the YOLOv11 model and leverages the MVTec AD dataset.

### 🎯 Main Goals:

- ✅ **Accurate detection** of defects (cracks, breaks, scratches, etc.)
- ✅ **Fast processing** of images and videos in real-time
- ✅ **Easy-to-use interface** built with Streamlit
- ✅ **Batch processing** support for multiple images
- ✅ **Comprehensive statistics and analytics** of results

---

## ✨ Key Features

### 🎯 Multi-Defect Detection
- Detection of various industrial defect types with high accuracy (95%+)
- Detailed confidence information for each detection
- Automatic Bounding Box coordinate extraction

### 📸 Image Processing
- Support for common formats (JPG, PNG, BMP, TIFF)
- Result visualization with colored boxes
- Confidence display for each defect
- Detailed result table visualization

### 🎬 Video Processing
- Frame-by-frame processing with a detailed progress bar
- Downloadable video with overlaid detections
- Optimized for long videos
- Frame interval configuration

### 📊 Batch Processing
- Simultaneous upload and processing of multiple images
- Batch summary and statistics display
- Image results gallery
- CSV output for further analysis

### ⚙️ Flexible Settings
- Confidence Threshold control
- IoU (Intersection over Union) threshold adjustment
- Interactive interface for model optimization

---

## 📊 Model Results

### Performance Metrics

| Metric | Result |
|--------|--------|
| **Precision** | 94.2% |
| **Recall** | 91.8% |
| **F1-Score** | 93.0% |
| **mAP@50** | 95.1% |
| **Inference Speed** | 45-50 ms |

#### Evaluation Curves

<div align="center">

**Precision Curve**
![Precision Curve](images/BoxP_curve.png)

**Recall Curve**
![Recall Curve](images/BoxR_curve.png)

**F1 Curve**
![F1 Curve](images/BoxF1_curve.png)

**PR Curve**
![PR Curve](images/BoxPR_curve.png)

</div>

#### Confusion Matrix

<div align="center">

**Confusion Matrix**
![Confusion Matrix](images/confusion_matrix.png)

**Normalized Confusion Matrix**
![Normalized Confusion Matrix](images/confusion_matrix_normalized.png)

</div>

---

## 🖼️ Sample Results

### Streamlit UI

![Streamlit UI](images/image_streamlit_UI.png)

### Training Samples

<div align="center">

**Training Batch 1**
![Train Batch 0](images/train_batch0.jpg)

**Training Batch 2**
![Train Batch 1](images/train_batch1.jpg)

**Training Batch 3**
![Train Batch 2](images/train_batch2.jpg)

</div>

### Validation Results

<div align="center">

**Validation Labels (Batch 1)**
![Val Batch 0 Labels](images/val_batch0_labels.jpg)

**Validation Predictions (Batch 1)**
![Val Batch 0 Pred](images/val_batch0_pred.jpg)

**Validation Labels (Batch 2)**
![Val Batch 1 Labels](images/val_batch1_labels.jpg)

**Validation Predictions (Batch 2)**
![Val Batch 1 Pred](images/val_batch1_pred.jpg)

</div>

### Label Distribution

![Labels Distribution](images/labels.jpg)

### Final Training Results

![Final Results](images/results.png)

---

## 🔧 Prerequisites

Before installation, ensure you have:

- **Python 3.10** or higher
- **pip** for package management
- **Sufficient memory**: Minimum 4GB RAM
- **GPU (optional)**: For faster processing (NVIDIA CUDA recommended)

### System prerequisites:

```bash
# For Ubuntu/Debian:
sudo apt-get install python3-dev python3-pip

# For macOS:
brew install python@3.10

# For Windows:
# Download from Python.org
```

---

## 📥 Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/mamadj0n/DeepInspect-YOLOv11.git
cd DeepInspect-YOLOv11
```

### Step 2: Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install required packages

```bash
# To run the app (recommended):
pip install -r app/requirements.txt

# Or for full installation (training and evaluation):
pip install -r requirements.txt
```

### Step 4: Install system dependencies

```bash
# For Ubuntu/Debian:
sudo apt-get install ffmpeg

# For macOS:
brew install ffmpeg

# For Windows:
# Download from https://ffmpeg.org/download.html
```

### Step 5: Run the application

```bash
streamlit run app/app.py
```

The app will automatically open at `http://localhost:8501`.

---

## 🚀 How to Use

### 1️⃣ Single Image
- Go to the 🖼️ Single Image tab
- Upload your image
- Click the 🔍 Detect Defects button
- View detection results and examine details
- Download the annotated image

### 2️⃣ Batch Processing
- Go to the 📂 Batch Processing tab
- Upload multiple images (up to 50)
- Click the 🔍 Process Batch button
- All results are displayed in a gallery
- View a summary table of results

### 3️⃣ Video Analysis
- Go to the 🎥 Video Analysis tab
- Upload your video
- (Optional) Adjust frame interval settings
- Click the 🎥 Process Video button
- Download the processed video

### ⚙️ Model Settings
In the sidebar, you can adjust the following:

| Setting | Range | Description |
|---------|-------|-------------|
| Confidence Threshold | 0.0 - 1.0 | Minimum confidence score for detection |
| IoU Threshold | 0.0 - 1.0 | Intersection over Union threshold to filter duplicate detections |

---

## 📁 Project Structure

```
DeepInspect-YOLOv11/
│
├── app/
│   ├── app.py                 # 🎯 Main Streamlit application
│   ├── DownloadModel.py       # Model downloader
│   └── requirements.txt       # App dependencies
│
├── images/                    # 📊 Result images and graphs
│   ├── BoxF1_curve.png
│   ├── BoxP_curve.png
│   ├── BoxR_curve.png
│   ├── BoxPR_curve.png
│   ├── confusion_matrix.png
│   ├── train_batch*.jpg
│   ├── val_batch*.jpg
│   └── ...
│
├── predictions/               # 📁 Output directory (detected images/videos)
│
├── config.py                  # ⚙️ Project settings
├── data_prep.py               # 📊 Data preparation
├── utils.py                   # 🛠️ Helper functions
├── train.py                   # 🚀 Model training
├── evaluate.py                # 📈 Model evaluation
├── download_weights.py        # 📥 Download model weights
│
├── requirements.txt           # 📦 All dependencies
├── runtime.txt                # 🐍 Python version
├── packages.txt               # 📚 System packages
├── LICENSE                    # 📜 License
└── README.md                  # 📖 This file
```

---

## 🛠️ Technologies Used

| Technology | Description | Version |
|------------|-------------|---------|
| Python | Main programming language | 3.10+ |
| PyTorch | Deep learning framework | 2.0+ |
| YOLOv11 | Object detection model | 8.2.0 |
| Streamlit | Interactive web interface | 1.35+ |
| OpenCV | Image processing & visualization | 4.9+ |
| NumPy | Numerical computations | 1.26+ |
| Pillow | Image format handling | 10.3+ |
| Pandas | Data analysis and processing | 2.0+ |
| scikit-learn | Strategic data splitting | 1.3+ |

---

## 📊 Sample Results

### JSON Output

```json
{
  "image_path": "test_image.jpg",
  "inference_time_ms": 45.32,
  "num_detections": 3,
  "predictions": [
    {
      "defect": "crack",
      "confidence": 0.92,
      "bbox": [100, 150, 50, 60],
      "class_id": 0
    },
    {
      "defect": "scratch",
      "confidence": 0.88,
      "bbox": [250, 200, 40, 30],
      "class_id": 2
    },
    {
      "defect": "broken",
      "confidence": 0.85,
      "bbox": [400, 100, 60, 50],
      "class_id": 1
    }
  ]
}
```

### Batch Output Table

| Image | Defects Found | Inference Time |
|-------|--------------|----------------|
| img1.jpg | 2 | 42.15 ms |
| img2.jpg | 1 | 46.89 ms |
| img3.jpg | 0 | 38.42 ms |

---

## 🔄 How to Download and Use the Model

### Automatic Download
The YOLO model is downloaded automatically on the first run of the application:

```
https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```

### Manual Download
If automatic download fails:

1. Open the link above
2. Download the `best.pt` file
3. Place the file in the project root directory

### Check Model Weights

```bash
python -c "from ultralytics import YOLO; model = YOLO('best.pt'); print(model.info())"
```

---

## 🎨 Color Coding & Conventions

The app uses different colors for better defect visualization:

| Color | Defect Type | Example |
|-------|------------|---------|
| 🔴 Red | Critical defects | Cracks, breaks, scratches |
| 🟢 Green | Other defects | Surface anomalies, contamination |

Label format: `[defect_name] | [confidence]`

---

## ⚡ Optimization Tips

### For Speed ⚡

```python
# ✅ Optimization methods:
1. Enable GPU (NVIDIA CUDA)
2. Increase Confidence Threshold (e.g., 0.5 instead of 0.25)
3. Use Frame Interval in videos (e.g., skip every 2 frames)
4. Use a smaller model (if speed matters more than accuracy)
```

### For Accuracy 🎯

```python
# ✅ Methods to increase accuracy:
1. Lower Confidence Threshold (0.15-0.2)
2. Use high-quality images
3. Fine-tune the model with your own data
4. Lower IoU Threshold for finer detections
```

---

## 🐛 Troubleshooting Common Issues

### ❌ "Model not found" Error

```bash
# ✅ Solution 1: Re-download the model
rm best.pt
# Then restart the application

# ✅ Solution 2: Manual download
wget https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```

### ❌ CUDA/GPU Error

```bash
# If GPU is not available:
# ✅ The model will automatically run on CPU (slower)

# Check GPU:
python -c "import torch; print(torch.cuda.is_available())"
```

### ❌ Low Accuracy

```bash
# ✅ Solutions:
1. Change Confidence Threshold from 0.25 to 0.15
2. Change IoU Threshold from 0.45 to 0.3
3. Increase input image resolution (>= 640x640)
4. Fine-tune the model with your own data (retrain)
```

### ❌ Out of Memory Error

```bash
# ✅ Solutions:
1. Reduce batch size
2. Use a smaller GPU
3. Upload smaller batches
```

---

## 📝 License & Rights

This project is released under the MIT License. See the LICENSE file for details.

```
MIT License - Free to use for commercial and non-commercial purposes
```

### Note for Industrial Applications
If you use this project for industrial purposes, please:

- ✅ Test your version thoroughly
- ✅ Fine-tune the model on specific data
- ✅ Verify results with experts
- ✅ Accept legal responsibility

---

## 🤝 Contributing to the Project

If you'd like to contribute:

### Contribution Steps

✅ Fork the repository
```bash
git clone https://github.com/YOUR_USERNAME/DeepInspect-YOLOv11.git
```

✅ Create a new branch
```bash
git checkout -b feature/your-improvement
```

✅ Commit your changes
```bash
git commit -m "Description: improved model accuracy +"
```

✅ Push to the branch
```bash
git push origin feature/your-improvement
```

✅ Submit a Pull Request

### Areas Needing Help
- 🔧 Code performance improvements
- 📚 Better documentation
- 🐛 Bug fixes
- ✨ New features
- 🌐 Document translation

---

## 📞 Contact & Links

- 👤 Developer: [@mamadj0n](https://github.com/mamadj0n)
- 🔗 Repository: [DeepInspect-YOLOv11](https://github.com/mamadj0n/DeepInspect-YOLOv11)
- 📖 YOLO Documentation: [Ultralytics YOLO](https://docs.ultralytics.com/)
- 🌐 Streamlit: [streamlit.io](https://streamlit.io/)
- 🐛 Report Issues: [Issues](https://github.com/mamadj0n/DeepInspect-YOLOv11/issues)

---

## 📚 Resources & References

### Official Documentation
- 📖 [YOLOv11 Documentation](https://docs.ultralytics.com/)
- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- 📖 [PyTorch Tutorials](https://pytorch.org/tutorials/)
- 📖 [OpenCV Documentation](https://docs.opencv.org/)

### Useful Datasets
- 🔗 [MVTec AD Dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad)
- 🔗 [COCO Dataset](https://cocodataset.org/)
- 🔗 [ImageNet](https://www.image-net.org/)

### Papers & Research
- 📄 [YOLOv11 Paper](https://arxiv.org/abs/...)
- 📄 [Object Detection Review](https://arxiv.org/abs/...)
- 📄 [Defect Detection Survey](https://arxiv.org/abs/...)

---

## 🙏 Acknowledgements

This project is made possible thanks to:

- 🙌 Ultralytics for the powerful YOLO model
- 🙌 Streamlit for the beautiful and robust UI
- 🙌 PyTorch for the deep learning framework
- 🙌 OpenCV for professional image processing
- 🙌 MVTec for the training dataset

---

## ⭐ If You Like This Project

Ways to help:
- ⭐ Star it to let others know
- 🔄 Share it with friends
- 💬 Write your comments and suggestions
- 🐛 Report issues
- 🤝 Contribute to development

```
✨ Built with ❤️ using YOLO and Streamlit | Powered by Streamlit Cloud | MODSO ✨
```

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| ⭐ Stars | ![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social) |
| 🍴 Forks | ![Forks](https://img.shields.io/github/forks/mamadj0n/DeepInspect-YOLOv11?style=social) |
| 👁️ Watchers | ![Watchers](https://img.shields.io/github/watchers/mamadj0n/DeepInspect-YOLOv11?style=social) |
| 📦 Python Version | ![Python](https://img.shields.io/badge/python-3.10+-blue.svg) |
| 📄 License | ![License](https://img.shields.io/badge/license-MIT-green.svg) |

**Last updated:** August 4, 2026 (2026-08-04) (equivalent to 13 Mordad 1405)

**Online version:** [GitHub Repository](https://github.com/mamadj0n/DeepInspect-YOLOv11)
```
