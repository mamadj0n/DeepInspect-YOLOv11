# 🔍 DeepInspect-YOLOv11

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-FF0000?logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)

**سیستم تشخیص خودکار عیوب صنعتی با استفاده از هوش مصنوعی و YOLO**

> 🎯 یک جعبه ابزار جامع برای تشخیص دقیق و سریع عیوب صنعتی در تصاویر و ویدیوها

### 🚀 **[تجربه نسخه زنده](https://deepinspect-yolov11.streamlit.app)** 🚀

---

## �� درباره پروژه

**DeepInspect-YOLOv11** یک پلتفرم قدرتمند و کاربر‌پسند برای تشخیص و شناسایی خودکار عیوب در تصاویر و ویدیوهای صنعتی است.

### 🎯 اهداف اصلی

- ✅ **تشخیص دقیق** عیوب (ترک‌ها، شکستگی‌ها، خراش‌ها و...)
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

## 📊 نتایج و عملکرد

### معیارهای عملکرد

| معیار | نتیجه |
|------|--------|
| **Precision** | 98.2% |
| **Recall** | 95.8% |
| **F1-Score** | 97.0% |
| **mAP@50** | 95.1% |
| **سرعت استنتاج** | 25-30 ms |
| **اندازه مدل** | 48.4 MB |

### منحنی‌های ارزیابی

<div align="center">

| Precision Curve | Recall Curve |
|---|---|
| ![Precision](images/BoxP_curve.png) | ![Recall](images/BoxR_curve.png) |

| F1 Curve | PR Curve |
|---|---|
| ![F1](images/BoxF1_curve.png) | ![PR](images/BoxPR_curve.png) |

</div>

### ماتریس خرابی

<div align="center">

| Confusion Matrix | Normalized Confusion Matrix |
|---|---|
| ![CM](images/confusion_matrix.png) | ![CM Norm](images/confusion_matrix_normalized.png) |

</div>

---

## 🖼️ نمونه‌های نتایج

### رابط کاربری Streamlit

![Streamlit UI](images/image_streamlit_UI.png)

### نمونه‌های آموزشی

<div align="center">

| دسته 1 | دسته 2 | دسته 3 |
|---|---|---|
| ![Batch 0](images/train_batch0.jpg) | ![Batch 1](images/train_batch1.jpg) | ![Batch 2](images/train_batch2.jpg) |

</div>

### نتایج اعتبارسنجی

<div align="center">

| برچسب‌ها | پیش‌بینی‌ها |
|---|---|
| ![Val 0 Labels](images/val_batch0_labels.jpg) | ![Val 0 Pred](images/val_batch0_pred.jpg) |
| ![Val 1 Labels](images/val_batch1_labels.jpg) | ![Val 1 Pred](images/val_batch1_pred.jpg) |

</div>

### توزیع برچسب‌ها و نتایج نهایی

<div align="center">

![Labels Distribution](images/labels.jpg)
![Final Results](images/results.png)

</div>

---

## 🔧 پیش‌نیازها

### نیازمندی‌های نرم‌افزاری
- **Python 3.10** یا بالاتر
- **pip** برای مدیریت بسته‌ها

### نیازمندی‌های سخت‌افزاری
- **حافظه RAM**: حداقل 4GB
- **GPU (اختیاری)**: برای سرعت بیشتر (NVIDIA CUDA موصی است)

### نصب وابستگی‌های سیستم

#### روی Ubuntu/Debian
```bash
sudo apt-get install python3-dev python3-pip ffmpeg
```

#### روی macOS
```bash
brew install python@3.10 ffmpeg
```

#### روی Windows
- Python را از [python.org](https://www.python.org/) دانلود کنید
- FFmpeg را از [ffmpeg.org](https://ffmpeg.org/download.html) دانلود کنید

---

## 📥 نصب و راه‌اندازی

### گام ۱: کلون کردن مخزن

```bash
git clone https://github.com/mamadj0n/DeepInspect-YOLOv11.git
cd DeepInspect-YOLOv11
```

### گام ۲: ایجاد محیط مجازی

```bash
python -m venv venv
```

**فعال کردن محیط مجازی:**

##### روی Windows
```bash
venv\Scripts\activate
```

##### روی macOS/Linux
```bash
source venv/bin/activate
```

### گام ۳: نصب کتابخانه‌های مورد نیاز

```bash
pip install -r app/requirements.txt
```

### گام ۴: اجرای برنامه

```bash
streamlit run app/app.py
```

برنامه به‌صورت خودکار در آدرس `http://localhost:8501` باز می‌شود.

---

## 🚀 نحوه استفاده

### 1️⃣ تصویر تکی

1. به تب **🖼️ Single Image** بروید
2. تصویر خود را آپلود کنید
3. دکمه **🔍 Detect Defects** را کلیک کنید
4. نتایج تشخیص را ببینید و جزئیات را بررسی کنید
5. تصویر ادغام‌شده را دانلود کنید

### 2️⃣ پردازش دسته‌ای

1. به تب **📂 Batch Processing** بروید
2. چندین تصویر را آپلود کنید (تا 50 تصویر)
3. دکمه **🔍 Process Batch** را کلیک کنید
4. تمام نتایج در یک گالری نمایش داده می‌شود
5. جدول خلاصه‌ای از نتایج را ببینید

### 3️⃣ تجزیه‌و‌تحلیل ویدیو

1. به تب **🎥 Video Analysis** بروید
2. ویدیو خود را آپلود کنید
3. (اختیاری) تنظیمات frame interval را تغییر دهید
4. دکمه **🎥 Process Video** را کلیک کنید
5. ویدیوی پردازش‌شده را دانلود کنید

### ⚙️ تنظیمات مدل

در نوار کناری (Sidebar) می‌توانید موارد زیر را تنظیم کنید:

| تنظیم | محدوده | توضیح |
|------|--------|--------|
| Confidence Threshold | 0.0 - 1.0 | حداقل امتیاز اطمینان برای تشخیص |
| IoU Threshold | 0.0 - 1.0 | آستانه تقاطع برای فیلترکردن دکتشن‌های تکراری |

---

## 📁 ساختار پروژه

```
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
├── predictions/               # 📁 خروجی برنامه
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

---

## 🛠️ تکنولوژی‌های استفاده شده

| تکنولوژی | توضیح | نسخه |
|---------|--------|------|
| Python | زبان برنامه‌نویسی اصلی | 3.10+ |
| PyTorch | فریم‌ورک یادگیری عمیق | 2.0+ |
| YOLOv11 | مدل تشخیص اشیاء | 8.2.0 |
| Streamlit | رابط کاربری وب تعاملی | 1.35+ |
| OpenCV | پردازش و تجسم تصویر | 4.9+ |
| NumPy | محاسبات عددی | 1.26+ |
| Pillow | کار با فرمت‌های تصویری | 10.3+ |
| Pandas | تحلیل و پردازش داده‌ها | 2.0+ |
| scikit-learn | تقسیم داده‌های استراتژیک | 1.3+ |

---

## 📊 نمونه خروجی

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

### جدول خروجی دسته‌ای

| تصویر | عیوب یافت شده | زمان استنتاج |
|------|-------------|------------|
| img1.jpg | 2 | 42.15 ms |
| img2.jpg | 1 | 46.89 ms |
| img3.jpg | 0 | 38.42 ms |

---

## 🔄 مدیریت مدل

### دانلود خودکی

مدل YOLO به‌صورت خودکار در اولین اجرای برنامه دانلود می‌شود از:

```
https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```

### دانلود دستی

اگر دانلود خودکار ناموفق بود:

1. لینک بالا را باز کنید
2. فایل `best.pt` را دانلود کنید
3. فایل را در پوشه اصلی پروژه قرار دهید

### بررسی وزن‌های مدل

```bash
python -c "from ultralytics import YOLO; model = YOLO('best.pt'); print(model.info())"
```

---

## 🎨 رنگ‌کدگذاری

برنامه برای بهتر دیدن عیوب از رنگ‌های مختلف استفاده می‌کند:

| رنگ | نوع عیب | مثال |
|------|---------|------|
| 🔴 قرمز | عیوب بحرانی | ترک‌ها، شکستگی‌ها، خراش‌ها |
| 🟢 سبز | عیوب دیگر | عیوب سطح‌ای، آلودگی |

**فرمت برچسب:** `[defect_name] | [confidence]`

---

## ⚡ نکات بهینه‌سازی

### برای سرعت بیشتر ⚡

1. GPU را فعال کنید (NVIDIA CUDA)
2. Confidence Threshold را افزایش دهید (مثلاً 0.5 به جای 0.25)
3. از Frame Interval در ویدیو استفاده کنید (مثلاً skip every 2 frames)
4. مدل کوچک‌تر استفاده کنید (اگر سرعت مهم‌تر از دقت است)

### برای دقت بیشتر 🎯

1. Confidence Threshold را کاهش دهید (0.15-0.2)
2. از تصاویر با کیفیت بالا استفاده کنید
3. مدل را Fine-tune کنید با داده‌های خاص خود
4. IoU Threshold را کاهش دهید برای تشخیص‌های دقیق‌تر

---

## 🐛 رفع مشکلات رایج

### ❌ خطای "Model not found"

```bash
# ✅ راه‌حل ۱: مدل را دوباره دانلود کنید
rm best.pt
# سپس برنامه را دوباره اجرا کنید

# ✅ راه‌حل ۲: دانلود دستی
wget https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```

### ❌ خطای CUDA/GPU

```bash
# بررسی GPU:
python -c "import torch; print(torch.cuda.is_available())"
```

**نوت:** اگر GPU موجود نیست، مدل به‌صورت خودکار روی CPU اجرا می‌شود (کندتر).

### ❌ بالا نبودن دقت

1. Confidence Threshold را از 0.25 به 0.15 تغییر دهید
2. IoU Threshold را از 0.45 به 0.3 تغییر دهید
3. تصاویر درون‌رفت را افزایش دهید (Resolution >= 640x640)
4. مدل را Fine-tune کنید با داده‌های خود

### ❌ خطای حافظه (OutOfMemory)

1. Batch size را کاهش دهید
2. از GPU کاهش‌یافته استفاده کنید
3. دسته‌های کوچک‌تر آپلود کنید

---

## 📝 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است. برای جزئیات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

استفاده آزاد برای مقاصد تجاری و غیرتجاری ✅

---

## 📚 منابع و مراجع

### اسناد رسمی

- 📖 [YOLOv11 Documentation](https://docs.ultralytics.com/)
- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- 📖 [PyTorch Tutorials](https://pytorch.org/tutorials/)
- 📖 [OpenCV Documentation](https://docs.opencv.org/)

### داتاست‌های مفید

- 🔗 [MVTec AD Dataset](https://www.mvtec.com/company/research/datasets/ad)
- 🔗 [COCO Dataset](https://cocodataset.org/)
- 🔗 [ImageNet](https://www.image-net.org/)

### مقالات و تحقیقات

- 📄 [YOLOv11 Paper](https://docs.ultralytics.com/)
- 📄 [Object Detection Review](https://arxiv.org/)
- 📄 [Defect Detection Survey](https://arxiv.org/)

---

## 🙏 تشکر و قدردانی

این پروژه به لطف موارد زیر ممکن شده است:

- 🙌 [Ultralytics](https://www.ultralytics.com/) برای مدل YOLO قدرتمند
- 🙌 [Streamlit](https://streamlit.io/) برای رابط کاربری زیبا و قوی
- 🙌 [PyTorch](https://pytorch.org/) برای فریم‌ورک یادگیری عمیق
- 🙌 [OpenCV](https://opencv.org/) برای پردازش تصویر حرفه‌ای
- 🙌 [MVTec](https://www.mvtec.com/) برای داتاست آموزشی

---

## ⭐ پشتیبانی

اگر این پروژه را دوست دارید، می‌توانید:

- ⭐ یک **Star** بگذارید تا دیگران هم از آن آگاه شوند
- 🔄 آن را **Share** کنید با دوستان
- 💬 **نظر و پیشنهادتان** را بنویسید
- 🐛 **مشکلات** را گزارش دهید
- 🤝 در **توسعه** مشارکت کنید

---

## 📞 تماس و پیوندها

- 👤 **توسعه‌دهنده:** [@mamadj0n](https://github.com/mamadj0n)
- 🔗 **مخزن:** [DeepInspect-YOLOv11](https://github.com/mamadj0n/DeepInspect-YOLOv11)
- 🐛 **گزارش مشکلات:** [Issues](https://github.com/mamadj0n/DeepInspect-YOLOv11/issues)

---

<div align="center">

### 📊 آمار پروژه

[![Stars](https://img.shields.io/github/stars/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)
[![Forks](https://img.shields.io/github/forks/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)
[![Watchers](https://img.shields.io/github/watchers/mamadj0n/DeepInspect-YOLOv11?style=social)](https://github.com/mamadj0n/DeepInspect-YOLOv11)

---

✨ **Built with ❤️ using YOLO and Streamlit | Powered by Streamlit Cloud** ✨

**آخرین به‌روزرسانی:** 13 مرداد 1405 (2026-07-13)

</div>
