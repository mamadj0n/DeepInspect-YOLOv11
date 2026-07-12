import gradio as gr
import json
from DefectInference import DefectInference
# Global variables for model caching (prevents reloading on every click)
current_model = None
current_settings = {}

def get_model(model_path, conf, iou):
    """Loads the model or reads it from cache if settings haven't changed."""
    global current_model, current_settings
    if (current_model is None or 
        current_settings.get('path') != model_path or 
        current_settings.get('conf') != conf or 
        current_settings.get('iou') != iou):
        
        current_model = DefectInference(model_path=model_path, conf_threshold=conf, iou_threshold=iou)
        current_settings = {'path': model_path, 'conf': conf, 'iou': iou}
    return current_model

def process_single_image(image_path, model_path, conf, iou):
    if not image_path:
        return None, "No image uploaded."
    
    model = get_model(model_path, conf, iou)
    result = model.predict_image(image_path, save_result=True, output_dir="gradio_outputs")
    
    annotated_img = result.get('annotated_image', image_path)
    # Convert prediction dictionary to a readable JSON format for display
    preds_str = json.dumps(result['predictions'], indent=2, ensure_ascii=False)
    
    return annotated_img, preds_str

def process_batch_images(image_paths, model_path, conf, iou):
    if not image_paths:
        return []
    
    model = get_model(model_path, conf, iou)
    output_images = []
    
    for img_path in image_paths:
        result = model.predict_image(img_path, save_result=True, output_dir="gradio_outputs")
        if 'annotated_image' in result:
            output_images.append(result['annotated_image'])
            
    return output_images

def process_video_file(video_path, model_path, conf, iou):
    if not video_path:
        return None
    
    model = get_model(model_path, conf, iou)
    out_video_path = model.predict_video(video_path, output_dir="gradio_outputs")
    
    return out_video_path

# ==========================================
# Gradio Blocks UI Design
# ==========================================
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    
    # Header and Logo
    gr.Markdown(
        """
        <div style="text-align: center;">
            <h1>AI-Powered Industrial Defect Detection Panel</h1>
        </div>
        """
    )
    
    with gr.Row():
        # Configuration Column (Sidebar)
        with gr.Column(scale=1, variant="panel"):
            gr.Markdown("### ⚙️ Model Settings")
            model_input = gr.Textbox(label="Model Path (best.pt)", value="runs/detect/mvtec_defect_detection/yolov11m_phase3/weights/best.pt")
            conf_input = gr.Slider(minimum=0.0, maximum=1.0, value=0.25, step=0.05, label="Confidence Threshold")
            iou_input = gr.Slider(minimum=0.0, maximum=1.0, value=0.45, step=0.05, label="IoU Threshold")
        
        # Main Tabs Column
        with gr.Column(scale=3):
            with gr.Tabs():
                
                # Tab 1: Single Image
                with gr.TabItem("🖼️ Single Image"):
                    with gr.Row():
                        img_input = gr.Image(type="filepath", label="Input Image")
                        img_output = gr.Image(type="filepath", label="Detection Result")
                    img_json_out = gr.Textbox(label="Output Details (JSON)", lines=5)
                    img_btn = gr.Button("Process Image", variant="primary")
                    
                    img_btn.click(
                        fn=process_single_image,
                        inputs=[img_input, model_input, conf_input, iou_input],
                        outputs=[img_output, img_json_out]
                    )
                
                # Tab 2: Batch Processing
                with gr.TabItem("📂 Batch Processing"):
                    batch_input = gr.File(file_count="multiple", type="filepath", label="Select Multiple Images", file_types=["image"])
                    batch_output = gr.Gallery(label="Results", columns=3, height="auto")
                    batch_btn = gr.Button("Process Batch", variant="primary")
                    
                    batch_btn.click(
                        fn=process_batch_images,
                        inputs=[batch_input, model_input, conf_input, iou_input],
                        outputs=[batch_output]
                    )
                
                # Tab 3: Video Processing
                with gr.TabItem("🎥 Video Analysis"):
                    with gr.Row():
                        vid_input = gr.Video(label="Upload Video")
                        vid_output = gr.Video(label="Processed Video")
                    vid_btn = gr.Button("Process Video", variant="primary")
                    
                    vid_btn.click(
                        fn=process_video_file,
                        inputs=[vid_input, model_input, conf_input, iou_input],
                        outputs=[vid_output]
                    )

# Application Launch (Configured for Kaggle environment to generate a public link)
def app ():
    if __name__ == "__main__":
        os.makedirs("gradio_outputs", exist_ok=True)
        # share=True creates a public live link (e.g., xxxxx.gradio.live)
        demo.launch(share=True, debug=True)

app()
