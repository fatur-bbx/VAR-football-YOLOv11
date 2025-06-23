import gradio as gr
from ultralytics import YOLO
import torch

# Menggunakan CPU (standar di tier gratis Hugging Face)
device = "cpu"

# Muat model Anda yang sudah dilatih
model = YOLO('p_detector_best.pt')
model.to(device)

def detect_objects(image):
    # Lakukan prediksi
    results = model(image)
    
    # Gambar bounding box pada hasil
    annotated_image = results[0].plot()
    
    return annotated_image

# Judul dan deskripsi untuk aplikasi Anda
title = "Player Detector (YOLOv11)"
description = "Unggah gambar pertandingan untuk mendeteksi pemain. Model ini dilatih secara custom dan di-deploy di Hugging Face Spaces."

# Membuat antarmuka Gradio
iface = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="pil", label="Upload Gambar Pertandingan"),
    outputs=gr.Image(type="pil", label="Hasil Deteksi Pemain"),
    title=title,
    description=description,
)

# Jalankan aplikasi
iface.launch()