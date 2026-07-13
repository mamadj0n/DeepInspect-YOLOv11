# 🔍 DeepInspect-YOLOv11

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-FF0000?logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)

**سیستم تشخیص خودکار عیوب صنعتی با استفاده از هوش مصنوعی و YOLO**

> 🎯 یک جعبه ابزار جامع برای تشخیص دقیق و سریع عیوب صنعتی در تصاویر و ویدیوها

---

## 📋 توضیحات

**DeepInspect-YOLOv11** یک پلتفرم قدرتمند و کاربر‌پسند برای تشخیص و شناسایی خودکار عیوب در تصاویر و ویدیوهای صنعتی است. این پروژه از مدل YOLOv11 استفاده می‌کند و اطلاعات را از داتاست MVTec AD استخراج کرده است.

### 🎯 اهداف اصلی:

- ✅ **تشخیص دقیق** عیوب (ترک‌ها، شکستگی‌ها، خراش‌ها، و...)
- ✅ **پردازش سریع** تصاویر و ویدیوها در زمان واقعی
- ✅ **رابط کاربری سهل‌الاستفاده** مبتنی بر Streamlit
- ✅ **پشتیبانی از پردازش دسته‌ای** چندین تصویر
- ✅ **آمار و تحلیل** جامع نتایج

---

## ✨ ویژگی‌های کلیدی

### 🎯 تشخیص عیوب چندگانه
- تشخیص انواع مختلف عیوب صنعتی با دقت بالا (95%+)
- نمایش اطلاعات دقیق اطمینان برای هر دکتشن
- استخراج خودکار مختصات Bounding Box

### 📸 پردازش تصاویر
- پشتیبانی از فرمت‌های رایج (JPG, PNG, BMP, TIFF)
- تصویرسازی نتایج با جعبه‌های رنگی
- نمایش میزان اطمینان برای هر عیب
- تجسم جدول تفصیلی نتایج

### 🎬 پردازش ویدیو
- پردازش فریم به فریم با نوار پیشرفت دقیق
- دانلود ویدیو ادغام‌شده با تشخیصات
- بهینه‌سازی برای ویدیوهای طولانی
- تنظیم بازه پردازش فریم‌ها

### 📊 پردازش دسته‌ای
- آپلود و پردازش همزمان چندین تصویر
- نمایش خلاصه و آمار دسته‌ای
- گالری نتایج تصویری
- خروجی CSV برای تحلیل بیشتر

### ⚙️ تنظیمات انعطاف‌پذیر
- کنترل آستانه اطمینان (Confidence Threshold)
- تنظیم آستانه IoU (Intersection over Union)
- رابط تعاملی برای بهینه‌سازی مدل

---

## 📊 نتایج مدل

### معیارهای عملکرد

| معیار | نتیجه |
|------|--------|
| **Precision** | 94.2% |
| **Recall** | 91.8% |
| **F1-Score** | 93.0% |
| **mAP@50** | 95.1% |
| **سرعت استنتاج** | 45-50 ms |

#### منحنی‌های ارزیابی

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

#### ماتریس خرابی

<div align="center">

**Confusion Matrix**
![Confusion Matrix](images/confusion_matrix.png)

**Normalized Confusion Matrix**
![Normalized Confusion Matrix](images/confusion_matrix_normalized.png)

</div>

---

## 🖼️ نمونه نتایج

### رابط کاربری Streamlit

![Streamlit UI](images/image_streamlit_UI.png)

### نمونه‌های آموزشی

<div align="center">

**دسته آموزشی 1**
![Train Batch 0](images/train_batch0.jpg)

**دسته آموزشی 2**
![Train Batch 1](images/train_batch1.jpg)

**دسته آموزشی 3**
![Train Batch 2](images/train_batch2.jpg)

</div>

### نتایج اعتبارسنجی

<div align="center">

**برچسب‌های اعتبارسنجی (دسته 1)**
![Val Batch 0 Labels](images/val_batch0_labels.jpg)

**پیش‌بینی‌های اعتبارسنجی (دسته 1)**
![Val Batch 0 Pred](images/val_batch0_pred.jpg)

**برچسب‌های اعتبارسنجی (دسته 2)**
![Val Batch 1 Labels](images/val_batch1_labels.jpg)

**پیش‌بینی‌های اعتبارسنجی (دسته 2)**
![Val Batch 1 Pred](images/val_batch1_pred.jpg)

</div>

### توزیع برچسب‌ها

![Labels Distribution](images/labels.jpg)

### نتایج نهایی آموزش

![Final Results](images/results.png)

---

## 🔧 پیش‌نیازها

قبل از نصب، مطمئن شوید موارد زیر را دارید:

- **Python 3.10** یا بالاتر
- **pip** برای مدیریت بسته‌ها
- **حافظه کافی**: حداقل 4GB RAM
- **GPU (اختیاری)**: برای سرعت بیشتر (NVIDIA CUDA موصی است)

### پیش‌نیازهای سیستم:

# برای Ubuntu/Debian:

```bash
sudo apt-get install python3-dev python3-pip
```

# برای macOS:
```bash
brew install python@3.10
```
# برای Windows:
# از Python.org دانلود کنید
📥 نحوه نصب و راه‌اندازی
گام ۱: کلون کردن مخزن
```bash
git clone https://github.com/mamadj0n/DeepInspect-YOLOv11.git
cd DeepInspect-YOLOv11
```
گام ۲: ایجاد محیط مجازی (توصیه می‌شود)
```bash
python -m venv venv
```

# روی Windows:
```
venv\Scripts\activate
```
# روی macOS/Linux:
```
source venv/bin/activate
```
گام ۳: نصب کتابخانه‌های مورد نیاز

# برای اجرای برنامه (توصیه شده):
```bash
pip install -r app/requirements.txt
```
گام ۴: نصب وابستگی‌های سیستم

# برای Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```
# برای macOS:
```bash
brew install ffmpeg
```
# برای Windows:
# از https://ffmpeg.org/download.html دانلود کنید
گام ۵: اجرای برنامه
```bash
streamlit run app/app.py
```
برنامه به‌صورت خودکار در آدرس http://localhost:8501 باز می‌شود.

🚀 نحوه استفاده
1️⃣ تصویر تکی
به تب 🖼️ Single Image بروید
تصویر خود را آپلود کنید
دکمه 🔍 Detect Defects را کلیک کنید
نتایج تشخیص را ببینید و جزئیات را بررسی کنید
می‌توانید تصویر ادغام‌شده را دانلود کنید
2️⃣ پردازش دسته‌ای
به تب 📂 Batch Processing بروید
چندین تصویر را آپلود کنید (تا 50 تصویر)
دکمه 🔍 Process Batch را کلیک کنید
تمام نتایج در یک گالری نمایش داده می‌شود
جدول خلاصه‌ای از نتایج را ببینید
3️⃣ تجزیه‌و‌تحلیل ویدیو
به تب 🎥 Video Analysis بروید
ویدیو خود را آپلود کنید
(اختیاری) تنظیمات frame interval را تغییر دهید
دکمه 🎥 Process Video را کلیک کنید
ویدیوی پردازش‌شده را دانلود کنید
⚙️ تنظیمات مدل
در نوار کناری (Sidebar) می‌توانید موارد زیر را تنظیم کنید:

تنظیم	محدوده	توضیح
Confidence Threshold	0.0 - 1.0	حداقل امتیاز اطمینان برای تشخیص
IoU Threshold	0.0 - 1.0	آستانه تقاطع برای فیلترکردن دکتشن‌های تکراری
📁 ساختار پروژه

```Code
DeepInspect-YOLOv11/
│
├── app/
│   ├── app.py                 # 🎯 اپلیکیشن اصلی Streamlit
│   ├── DownloadModel.py       # دانلود مدل
│   └── requirements.txt        # وابستگی‌های برنامه
│
├── images/                    # 📊 تصاویر نتایج و نمودارها
│   ├── BoxF1_curve.png
│   ├── BoxP_curve.png
│   ├── BoxR_curve.png
│   ├── BoxPR_curve.png
│   ├── confusion_matrix.png
│   ├── train_batch*.jpg
│   ├── val_batch*.jpg
│   └── ...
│
├── predictions/               # 📁 خروجی برنامه (تصاویر/ویدیوهای تشخیص‌شده)
│
├── config.py                  # ⚙️ تنظیمات پروژه
├── data_prep.py               # 📊 آماده‌سازی داده‌ها
├── utils.py                   # 🛠️ توابع کمکی
├── train.py                   # 🚀 آموزش مدل
├── evaluate.py                # 📈 ارزیابی مدل
├── download_weights.py        # 📥 دانلود وزن‌های مدل
│
├── requirements.txt           # 📦 تمام وابستگی‌ها
├── runtime.txt                # 🐍 نسخه Python
├── packages.txt               # 📚 بسته‌های سیستم
├── LICENSE                    # 📜 مجوز
└── README.md                  # 📖 این فایل
```
🛠️ تکنولوژی‌های استفاده شده
تکنولوژی	توضیح	نسخه
Python	زبان برنامه‌نویسی اصلی	3.10+
PyTorch	فریم‌ورک یادگیری عمیق	2.0+
YOLOv11	مدل تشخیص اشیاء	8.2.0
Streamlit	رابط کاربری وب تعاملی	1.35+
OpenCV	پردازش و تجسم تصویر	4.9+
NumPy	محاسبات عددی	1.26+
Pillow	کار با فرمت‌های تصویری	10.3+
Pandas	تحلیل و پردازش داده‌ها	2.0+
scikit-learn	تقسیم داده‌های استراتژیک	1.3+
📊 نمونه نتایج
خروجی JSON
```JSON
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
جدول خروجی دسته‌ای
Image	Defects Found	Inference Time
img1.jpg	2	42.15 ms
img2.jpg	1	46.89 ms
img3.jpg	0	38.42 ms
🔄 نحوه دانلود و استفاده از مدل
دانلود خودکی
مدل YOLO به‌صورت خودکی بر اساس اینترنت در اولین اجرای برنامه دانلود می‌شود:

```Code
📥 https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```
دانلود دستی
اگر دانلود خودکار ناموفق بود:

لینک بالا را باز کنید
فایل best.pt را دانلود کنید
فایل را در پوشه اصلی پروژه قرار دهید
بررسی وزن‌های مدل
```bash
python -c "from ultralytics import YOLO; model = YOLO('best.pt'); print(model.info())"
```
🎨 رنگ‌کدگذاری و قراردادها
برنامه برای بهتر دیدن عیوب از رنگ‌های مختلف استفاده می‌کند:

رنگ	نوع عیب	مثال
🔴 قرمز	عیوب بحرانی	ترک‌ها، شکستگی‌ها، خراش‌ها
🟢 سبز	عیوب دیگر	عیوب سطح‌ای، آلودگی
فرمت برچسب: [defect_name] \| [confidence]

⚡ نکات بهینه‌سازی
برای سرعت بیشتر ⚡
# ✅ روش‌های بهینه‌سازی:
1. GPU را فعال کنید (NVIDIA CUDA)
2. Confidence Threshold را افزایش دهید (مثلاً 0.5 به جای 0.25)
3. از Frame Interval در ویدیو استفاده کنید (مثلاً skip every 2 frames)
4. مدل کوچک‌تر استفاده کنید (اگر سرعت مهم‌تر از دقت است)
برای دقت بیشتر 🎯

# ✅ روش‌های افزایش دقت:
1. Confidence Threshold را کاهش دهید (0.15-0.2)
2. از تصاویر با کیفیت بالا استفاده کنید
3. مدل را Fine-tune کنید با داده‌های خاص خود
4. IoU Threshold را کاهش دهید برای تشخیص‌های دقیق‌تر
🐛 رفع مشکلات رایج
❌ خطای "Model not found"
```bash
# ✅ راه‌حل ۱: مدل را دوباره دانلود کنید
rm best.pt
```
# سپس برنامه را دوباره اجرا کنید

# ✅ راه‌حل ۲: دانلود دستی
```bash
wget https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```
❌ خطای CUDA/GPU
bash
# اگر GPU موجود نیست:
# ✅ مدل به‌صورت خودکار روی CPU اجرا می‌شود (کندتر)

# بررسی GPU:
```python
-c "import torch; print(torch.cuda.is_available())"```
❌ بالا نبودن دقت
# ✅ راه‌حل‌ها:
1. Confidence Threshold را از 0.25 به 0.15 تغییر دهید
2. IoU Threshold را از 0.45 به 0.3 تغییر دهید
3. تصاویر درون‌رفت را افزایش دهید (Resolution >= 640x640)
4. مدل را Fine-tune کنید با داده‌های خود (آموزش مجدد)
❌ خطای حافظه (OutOfMemory)

# ✅ راه‌حل‌ها:
1. Batch size را کاهش دهید
2. از GPU کاهش‌یافته استفاده کنید
3. دسته‌های کوچک‌تر آپلود کنید
📝 مجوز و حقوق
این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر به فایل LICENSE مراجعه کنید.


MIT License - استفاده آزاد برای مقاصد تجاری و غیرتجاری

📞 تماس و پیوندها
👤 توسعه‌دهنده: @mamadj0n
🔗 مخزن: DeepInspect-YOLOv11
📖 مستندات YOLO: Ultralytics YOLO
🌐 Streamlit: streamlit.io
🐛 گزارش مشکلات: Issues
📚 منابع و مراجع
اسناد رسمی
📖 YOLOv11 Documentation
📖 Streamlit Documentation
📖 PyTorch Tutorials
📖 OpenCV Documentation
داتاست‌های مفید
🔗 MVTec AD Dataset
🔗 COCO Dataset
🔗 ImageNet
مقالات و تحقیقات
📄 YOLOv11 Paper
📄 Object Detection Review
📄 Defect Detection Survey
🙏 تشکر و قدردانی
این پروژه به لطف موارد زیر ممکن شده است:

🙌 Ultralytics برای مدل YOLO قدرتمند
🙌 Streamlit برای رابط کاربری زیبا و قوی
🙌 PyTorch برای فریم‌ورک یادگیری عمیق
🙌 OpenCV برای پردازش تصویر حرفه‌ای
🙌 MVTec برای داتاست آموزشی
⭐ اگر این پروژه را دوست دارید
کمک‌های ممکن
⭐ یک Star بگذارید تا دیگران هم از آن آگاه شوند
🔄 آن را Share کنید با دوستان
💬 نظر و پیشنهادتان را بنویسید
🐛 مشکلات را گزارش دهید
🤝 مشارکت کنید در توسعه
Code
✨ Built with ❤️ using YOLO and Streamlit | Powered by Streamlit Cloud | MODSO ✨
📈 آمار پروژه
معیار	تعداد
⭐ Stars	![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social)
🍴 Forks	![Forks](https://img.shields.io/github/forks/mamadj0n/DeepInspect-YOLOv11?style=social)
👁️ Watchers	![Watchers](https://img.shields.io/github/watchers/mamadj0n/DeepInspect-YOLOv11?style=social)
📦 Python Version	![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
📄 License	![License](https://img.shields.io/badge/license-MIT-green.svg)
آخرین به‌روزرسانی: 13 مرداد 1405 (2026-07-13)

آن‌لاین نسخه: GitHub Repository
