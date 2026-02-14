import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import transformers
from PIL import Image
import requests
from io import BytesIO
import warnings
import os

# Silence warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
transformers.utils.logging.set_verbosity_error()
warnings.filterwarnings("ignore")

def run_caption_demo():
    """
    Simple Image Captioning using a pre-trained Vision-Encoder-Decoder model.
    This uses ViT (Vision Transformer) as the encoder and GPT-2 as the decoder.
    """
    model_name = "nlpconnect/vit-gpt2-image-captioning"
    
    print(f"--- Loading Image Captioning AI ({model_name}) ---")
    
    # Load model, processor, and tokenizer
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = VisionEncoderDecoderModel.from_pretrained(model_name).to(device)
    feature_extractor = ViTImageProcessor.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Sample Image URL (A city skyline)
    url = "https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&q=80&w=1000"
    print(f"Fetching image from: {url}")
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    if img.mode != "RGB":
        img = img.convert(mode="RGB")
    
    # Show the image using the system's default viewer
    img.show()

    # Pre-process image
    inputs = feature_extractor(images=[img], return_tensors="pt")
    pixel_values = inputs.pixel_values.to(device)

    # Generate Caption
    print("AI is thinking...")
    # Add attention_mask to silence warning
    output_ids = model.generate(
        pixel_values, 
        max_length=16, 
        num_beams=4,
        attention_mask=torch.ones(pixel_values.shape[0], pixel_values.shape[1]).to(device)
    )
    
    # Decode result
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
    
    print("\n" + "="*40)
    print(f"GENERATED CAPTION: {caption}")
    print("="*40 + "\n")

if __name__ == "__main__":
    try:
        run_caption_demo()
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Tip: Make sure you have the required libraries installed (pip install -r requirements.txt)")
