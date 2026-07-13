import os
import urllib.request

def download_model_weights():
    # مسیری که می‌خواهید مدل در آن ذخیره شود
    save_path = "weights/best.pt"
    
    # لینک دانلودی که از GitHub Releases یا Hugging Face گرفته‌اید
    url = "https://github.com/mamadj0n/DeepInspect-YOLOv11/releases/download/v1.0.0/best.pt"
    
    # بررسی اینکه آیا مدل از قبل وجود دارد یا خیر
    if not os.path.exists(save_path):
        print("[*] Model weights not found. Downloading...")
        # ساخت پوشه‌های مسیر در صورت عدم وجود
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        urllib.request.urlretrieve(url, save_path)
        print("✅ Download complete!")
    else:
        print("[*] Model weights already exist.")

if __name__ == "__main__":
    download_model_weights()
