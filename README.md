# ⚽ Football Player Detection using YOLOv8x

> Real-time detection of football players, referees, goalkeepers, and the ball using the powerful YOLOv8x model — built on a custom-labeled dataset and deployed with Django.

---

## 📌 Overview

In modern football, data is power. The ability to detect players automatically from match footage unlocks new possibilities: tactical analysis, spatial player positioning, and even lightweight VAR systems.

This project focuses on **real-time object detection** in football matches — specifically identifying players, goalkeepers, referees, and the ball from video footage.

> 🔸 Note: This project is currently focused on **detection**, not **tracking** across frames.

---

## 🎯 Goals

- 🎥 Detect players and key match elements from football videos.
- 🧠 Utilize the YOLOv8x model for high-accuracy object detection under various lighting and camera angles.
- 🌐 Deploy the model in a Django-based web interface.
- ✅ Visualize bounding boxes on detected objects in real time.

---

## 📁 Dataset

- **Source**: [Football Players Detection Dataset v14 – Roboflow](https://universe.roboflow.com/)
- **Annotations**: Custom bounding boxes per object.
- **Classes Included**:
  - `Player`
  - `Goalkeeper`
  - `Referee`
  - `Ball`

---

## 🧠 Model Information

| Item            | Detail                       |
|-----------------|------------------------------|
| Model           | YOLOv8x                      |
| Framework       | PyTorch (via Ultralytics)    |
| Reason Chosen   | Highest accuracy variant of YOLOv8 – ideal for detailed object detection tasks |

---

## 🏋️ Training Details

| Parameter       | Value             |
|-----------------|-------------------|
| Platform        | Google Colab      |
| GPU             | NVIDIA RTX 3060 6GB |
| Epochs          | 50                |
| Batch Size      | 3                 |
| RAM Usage       | ~4.5 GB           |
| Validation Set  | 49 Images         |
| Detected Objects| 1,174 Instances   |

---

## 📊 Evaluation Metrics

| Metric         | Value  |
|----------------|--------|
| Precision (Box P) | 0.931 |
| Recall (R)         | 0.818 |
| mAP@0.5           | 0.900 |
| mAP@0.5:0.95      | 0.627 |

---

## 🚀 Deployment

- **Backend**: Django
- **Deployment Mode**: Localhost (Test Phase)
- **Features**:
  - Upload match video
  - Process video with YOLOv8x
  - Return annotated video with bounding boxes

---

## 🔗 Demo & Resources

- 📓 **Colab Notebook**: [Open in Colab](#) *(insert your link here)*
- 🎥 **Detection Sample Video**: [Watch the result](#) *(insert your link here)*

---

## 📌 Project Status

- ✅ Dataset Prepared
- ✅ Model Trained
- ✅ Model Evaluated
- ✅ Video Detection Working
- ✅ Django App Running
- 🔄 Final Step: Integrate detection visualization to web interface

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics)
- [Django](https://www.djangoproject.com/)
- [OpenCV](https://opencv.org/)
- [Roboflow](https://roboflow.com/)
- [Jupyter Notebook](https://jupyter.org/)

---

## 🧪 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/faturbbx/VAR-football-YOLOv9.git
   cd VAR-football-YOLOv9
