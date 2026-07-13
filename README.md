# 🔍 DeepInspect-YOLOv11

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-FF0000?logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**سیستم تشخیص خودکار عیوب صنعتی با استفاده از هوش مصنوعی و YOLO**

---

## 📋 توضیحات

**DeepInspect-YOLOv11** یک رابط کاربری قدرتمند و اینتویتیو برای تشخیص و شناسایی خودکار عیوب در تصاویر و ویدیوهای صنعتی است. این پروژه از مدل YOLOv11 پیشرفته استفاده می‌کند تا با دقت بالا عیوب مختلف را تشخیص و موقعیت‌یابی کند.

**اهداف اصلی:**
- ✅ تشخیص دقیق عیوب (ترک‌ها، شکستگی‌ها، خراش‌ها و...)
- ✅ پردازش سریع تصاویر و ویدیوها در زمان واقعی
- ✅ رابط کاربری سهل‌الاستفاده مبتنی بر Streamlit
- ✅ پشتیبانی از دسته‌ای پردازش چندین تصویر

---

## ✨ ویژگی‌های کلیدی

🎯 **تشخیص عیوب چندگانه:**
- تشخیص انواع مختلف عیوب صنعتی با دقت بالا
- نمایش اطلاعات دقیق اطمینان برای هر دکتشن
- استخراج خودکار مختصات Bounding Box

📸 **پردازش تصاویر:**
- پشتیبانی از فرمت‌های رایج (JPG, PNG, BMP, TIFF)
- تصویرسازی نتایج با جعبه‌های رنگی
- نمایش میزان اطمینان برای هر عیب

🎬 **پردازش ویدیو:**
- پردازش فریم به فریم با نوار پیشرفت
- دانلود ویدیو ادغام‌شده با تشخیصات
- بهینه‌سازی برای ویدیوهای طولانی

📊 **پردازش دسته‌ای:**
- آپلود و پردازش همزمان چندین تصویر
- نمایش خلاصه و آمار دسته‌ای
- گالری نتایج تصویری

⚙️ **تنظیمات انعطاف‌پذیر:**
- کنترل آستانه اطمینان (Confidence Threshold)
- تنظیم آستانه IoU (Intersection over Union)
- رابط تعاملی برای بهینه‌سازی مدل

---

## 🔧 پیش‌نیازها

قبل از نصب، مطمئن شوید موارد زیر را دارید:

- **Python 3.10** یا بالاتر
- **pip** برای مدیریت بسته‌ها
- **حافظه کافی**: حداقل 4GB RAM
- **GPU (اختیاری)**: برای سرعت بیشتر (NVIDIA CUDA موصی است)

---

## 📥 نحوه نصب و راه‌اندازی

### گام ۱: کلون کردن مخزن

```bash
git clone https://github.com/mamadj0n/DeepInspect-YOLOv11.git
cd DeepInspect-YOLOv11
```

### گام ۲: ایجاد محیط مجازی (توصیه می‌شود)

```bash
python -m venv venv

# روی Windows:
venv\Scripts\activate

# روی macOS/Linux:
source venv/bin/activate
```

### گام ۳: نصب کتابخانه‌های مورد نیاز

```bash
pip install -r app/requirements.txt
```

یا برای نصب کامل:

```bash
pip install -r requirements.txt
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

### 2️⃣ پردازش دسته‌ای

1. به تب **📂 Batch Processing** بروید
2. چندین تصویر را آپلود کنید
3. دکمه **🔍 Process Batch** را کلیک کنید
4. تمام نتایج در یک گالری نمایش داده می‌شود

### 3️⃣ تجزیه‌و‌تحلیل ویدیو

1. به تب **🎥 Video Analysis** بروید
2. ویدیو خود را آپلود کنید
3. دکمه **🎥 Process Video** را کلیک کنید
4. ویدیوی پردازش‌شده را دانلود کنید

### ⚙️ تنظیمات مدل

در نوار کناری (Sidebar) می‌توانید موارد زیر را تنظیم کنید:

- **Confidence Threshold**: حداقل امتیاز اطمینان برای تشخیص (۰.۰ تا ۱.۰)
- **IoU Threshold**: آستانه تقاطع برای فیلترکردن دکتشن‌های تکراری (۰.۰ تا ۱.۰)

---

## 📁 ساختار پروژه

```
DeepInspect-YOLOv11/
├── app/
│   ├── app.py                 # اپلیکیشن اصلی Streamlit
│   └── requirements.txt        # وابستگی‌های پروژه
├── predictions/               # پوشه خروجی (تصاویر/ویدیوهای تشخیص‌شده)
├── requirements.txt           # وابستگی‌های کامل
├── best.pt                    # مدل YOLO (دانلود خودکار)
└── README.md                  # این فایل
```

---

## 🛠️ تکنولوژی‌های استفاده شده

| تکنولوژی | توضیح | نسخه |
|---------|-------|------|
| **Python** | زبان برنامه‌نویسی | 3.10+ |
| **PyTorch** | فریم‌ورک یادگیری عمیق | - |
| **YOLOv11** | مدل تشخیص اشیاء | 8.2.0 |
| **Streamlit** | رابط کاربری وب | 1.35+ |
| **OpenCV** | پردازش تصویر | 4.9+ |
| **NumPy** | محاسبات عددی | 1.26+ |
| **Pillow** | کار با تصاویر | 10.3+ |

---

## 📊 نمونه نتایج

برنامه برای هر دکتشن اطلاعات زیر ارائه می‌دهد:

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
    }
  ]
}
```

---

## 🔄 نحوه دانلود مدل

مدل YOLO به‌صورت خودکار بر اساس اینترنت در اولین اجرای برنامه دانلود می‌شود:

```python
# فایل best.pt از اینجا دانلود می‌شود:
https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt
```

اگر دانلود خودکار ناموفق بود، می‌توانید فایل را دستی دانلود و در پوشه اصلی قرار دهید.

---

## 🎨 رنگ‌کدگذاری

برنامه برای بهتر دیدن عیوب از رنگ‌های مختلف استفاده می‌کند:

- 🔴 **قرمز**: عیوب مهم (ترک‌ها، شکستگی‌ها، خراش‌ها)
- 🟢 **سبز**: عیوب دیگر

---

## ⚡ نکات بهینه‌سازی

### برای سرعت بیشتر:
- از **GPU** استفاده کنید
- **Confidence Threshold** را افزایش دهید (مثلاً ۰.۵ به جای ۰.۲۵)
- از **Frame Interval** در ویدیو استفاده کنید

### برای دقت بیشتر:
- **Confidence Threshold** را کاهش دهید
- از **تصاویر با کیفیت بالا** استفاده کنید
- مدل را بر اساس داده‌های خاص خود **Fine-tune** کنید

---

## 🐛 رفع مشکلات رایج

### ❌ خطای "Model not found"
**راه‌حل:** مطمئن شوید فایل `best.pt` در پوشه اصلی پروژه است یا اتصال اینترنت را بررسی کنید.

### ❌ خطای CUDA/GPU
**راه‌حل:** اگر GPU موجود نیست، مدل به‌صورت خودکار روی CPU اجرا می‌شود (کندتر).

### ❌ بالا نبودن دقت
**راه‌حل:** مدل را بر روی داده‌های خاص خود آموزش دهید یا `Confidence Threshold` را تنظیم کنید.

---

## 📝 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است. برای جزئیات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

```
MIT License - استفاده آزاد برای مقاصد تجاری و غیرتجاری
```

---

## 🤝 مشارکت در پروژه

اگر می‌خواهید به این پروژه کمک کنید:

1. ✅ **Fork** مخزن را کنید
2. ✅ **Branch** جدید ایجاد کنید:
   ```bash
   git checkout -b feature/بهبود-شما
   ```
3. ✅ **Commit** تغییرات خود:
   ```bash
   git commit -m "توضیح تغییرات"
   ```
4. ✅ **Push** به branch:
   ```bash
   git push origin feature/بهبود-شما
   ```
5. ✅ **Pull Request** بفرستید

---

## 📞 تماس و پیوندها

- 👤 **توسعه‌دهنده**: [mamadj0n](https://github.com/mamadj0n)
- 🔗 **مخزن**: [DeepInspect-YOLOv11](https://github.com/mamadj0n/DeepInspect-YOLOv11)
- 📖 **مستندات YOLO**: [Ultralytics YOLO](https://docs.ultralytics.com/)
- 🌐 **Streamlit**: [streamlit.io](https://streamlit.io/)

---

## 📚 منابع مفید

- [YOLOv11 Documentation](https://docs.ultralytics.com/models/yolov11/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [OpenCV Documentation](https://docs.opencv.org/)

---

## 🙏 تشکر و قدردانی

- **Ultralytics** برای مدل YOLO
- **Streamlit** برای رابط کاربری قدرتمند
- **PyTorch** برای فریم‌ورک یادگیری عمیق

---

## ⭐ اگر این پروژه را دوست دارید

**لطفاً یک ⭐ Star** بگذارید تا دیگران هم از آن آگاه شوند!

```
Built with ❤️ using YOLO and Streamlit | Powered by Streamlit Cloud | MODSO
```

---

**آخرین به‌روزرسانی**: ۱۳ مرداد ۱۴۰۵ (۲۰۲۶-۰۷-۱۳)
