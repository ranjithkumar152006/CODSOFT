# 👁️ VisionAI: Advanced Multimodal Image Captioning

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-6.0+-orange.svg)](https://gradio.app/)
[![Deep Learning](https://img.shields.io/badge/Model-BLIP--Large-green.svg)](https://huggingface.co/Salesforce/blip-image-captioning-large)

VisionAI is a professional-grade, AI-powered image captioning application that bridges the gap between Computer Vision (CV) and Natural Language Processing (NLP). Powered by **Salesforce's BLIP-Large**, it delivers high-fidelity scene descriptions, real-time translations, and neural voice synthesis.

---

## 🚀 Live Demo

You can access the live version of this app here:
👉 **[Open VisionAI Live Interface](https://2343aa45d084d7df61.gradio.live)**

_(Note: The link remains active while the server terminal is running. For 24/7 hosting, deployment to Hugging Face Spaces is recommended.)_

---

## ✨ Key Features

- **🧠 Maximum Precision**: Powered by **BLIP-Large (1.8GB)** with 7-beam search decoding for professional-grade detail and accuracy.
- **🌐 Multilingual Engine**: Seamless translation of captions into **Hindi, Spanish, French, German, and Chinese**.
- **🎙️ Neural TTS**: Integrated Text-to-Speech that reads out captions in the target language with natural intonation.
- **🎨 Premium UX**: Glassmorphic dark-mode interface designed with custom CSS for a state-of-the-art feel.
- **� Universal Input**: Supports local file uploads, **direct clipboard pasting (from Chrome/Edge)**, and live webcam capture.
- **⚡ Error Robustness**: Advanced error handling for corrupted images or unsupported clipboard formats.

---

## 🛠️ Technology Stack

- **Large Language Model**: `Salesforce/blip-image-captioning-large`
- **Frameworks**: `PyTorch`, `Hugging Face Transformers`
- **Web Interface**: `Gradio`
- **Logic & Tools**: `Google-Translator`, `gTTS`, `Pillow (PIL)`

---

## 📂 Project Navigation

| File                     | Role                                                                     |
| :----------------------- | :----------------------------------------------------------------------- |
| `advanced_captioning.py` | **Core Application**. Launches the high-fidelity Web UI with BLIP-Large. |
| `cnn_rnn_model.py`       | Educational module demonstrating CNN (ResNet) + RNN/LSTM logic.          |
| `caption_demo.py`        | Lightweight test script for quick model validation.                      |
| `requirements.txt`       | Dependency manifest for environment setup.                               |

---

## 🚀 Getting Started

### 1. Environment Setup

```bash
# Install the neural engine and dependencies
pip install -r requirements.txt
```

### 2. Launch the App

```bash
python advanced_captioning.py
```

---

## 💡 Engineering Logic

1. **Multimodal Encoding**: The `BLIP` (Bootstrapping Language-Image Pre-training) encoder reconciles visual pixels with semantic tokens.
2. **Beam Search Decoding**: Instead of picking the most "likely" next word, the AI explores 7 parallel sentence structures to find the most contextually accurate description.
3. **Translation Hook**: Captions are dynamically passed to the Google Translation cloud before reaching the UI.
4. **Audio Synthesis**: The final string is converted into a neural-encoded MP3 stream for immediate playback.

---

## 📋 Clipboard Support (New!)

You can now **Copy Image** directly from your web browser (Chrome/Edge/Firefox) and **Paste (Ctrl+V)** directly into the VisionAI upload box. The system will automatically handle the conversion.

---

# Execution Video

Watch the execution of the tic_tac_toe AI here:
Click here to view execution video : https://drive.google.com/file/d/1VvH4HG4CdV0osqlNz8iPOwEBe3MbPUp4/view?usp=sharing

## Author

Ranjith kumar.A
