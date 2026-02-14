
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr
from PIL import Image
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
import tempfile

# Force CPU if CUDA is not available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load SOTA Model: BLIP-Large (Maximum Accuracy)
# This is the "Large" version of BLIP, which is the most powerful model for captioning in this class
MODEL_NAME = "Salesforce/blip-image-captioning-large"
print(f"Loading {MODEL_NAME}... (This is a 1.8GB model for maximum accuracy)")
processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

def predict_caption(image, language):
    if image is None:
        return "Please upload or paste an image first.", "", None
    
    try:
        # Pre-process image (image is already PIL because of type="pil")
        img = image.convert("RGB")
        
        # Generate Caption using BLIP-Large
        inputs = processor(img, return_tensors="pt").to(device)
        
        # Advanced Beam Search for high-fidelity descriptions
        output = model.generate(
            **inputs, 
            max_new_tokens=80,      # Increased for highly detailed descriptions
            num_beams=7,            # Higher beam count for extreme accuracy
            repetition_penalty=1.2, # Prevents the AI from repeating words
            length_penalty=1.0,     # Encourages a good balance of length
            early_stopping=True
        )
        
        caption_en = processor.decode(output[0], skip_special_tokens=True).strip()
        
        # Filter out common prefixes some models add
        if caption_en.startswith("a photo of "):
            caption_en = caption_en.replace("a photo of ", "", 1)
        
        # Translate if needed
        target_langs = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Hindi": "hi",
            "Chinese": "zh-CN"
        }
        
        selected_lang_code = target_langs.get(language, "en")
        
        if selected_lang_code != "en":
            final_caption = GoogleTranslator(source='auto', target=selected_lang_code).translate(caption_en)
        else:
            final_caption = caption_en

        # Generate Audio (TTS)
        tts = gTTS(text=final_caption, lang=selected_lang_code)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        
        return caption_en, final_caption, temp_file.name
        
    except Exception as e:
        return f"Error processing image: {str(e)}", "Please try a different image format or upload the file directly.", None

# Custom CSS for Premium Look
custom_css = """
body { background-color: #0f172a; color: #f8fafc; }
.gradio-container { font-family: 'Inter', sans-serif; }
.main-title { text-align: center; margin-bottom: 2rem; }
.main-title h1 { 
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    font-weight: 800;
}
.generate-btn {
    background: linear-gradient(90deg, #0ea5e9, #6366f1) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
}
.output-box {
    border-radius: 12px !important;
    border: 1px solid #334155 !important;
    background: #1e293b !important;
}
"""

with gr.Blocks(elem_classes="gradio-container") as demo:
    gr.HTML("<div class='main-title'><h1>VisionAI: Advanced Image Captioning</h1><p>Generate detailed captions and translations with voice feedback.</p></div>")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="Upload Image, Paste, or use Webcam", type="pil")
            language_opt = gr.Dropdown(
                choices=["English", "Spanish", "French", "German", "Hindi", "Chinese"],
                value="English",
                label="Target Language"
            )
            submit_btn = gr.Button("Generate Caption", variant="primary", elem_classes="generate-btn")
        
        with gr.Column(scale=1):
            with gr.Group(elem_classes="output-box"):
                out_en = gr.Textbox(label="Original Caption (English)", interactive=False)
                out_translated = gr.Textbox(label="Translated Caption", interactive=False)
                out_audio = gr.Audio(label="Voice Output", interactive=False)
    
    gr.Examples(
        examples=[
            ["https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&q=80&w=1000", "English"],
            ["https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=1000", "Spanish"]
        ],
        inputs=[input_image, language_opt]
    )

    submit_btn.click(
        fn=predict_caption,
        inputs=[input_image, language_opt],
        outputs=[out_en, out_translated, out_audio]
    )

if __name__ == "__main__":
    demo.launch(share=True, css=custom_css, theme=gr.themes.Soft())
