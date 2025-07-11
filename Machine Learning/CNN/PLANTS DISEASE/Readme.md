# 🌿 Plant Disease Detection using Deep Learning

This project uses **Convolutional Neural Networks (CNN)** with **MobileNetV2** and **Grad-CAM** to detect and explain diseases in plant leaves from the [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease).

---

## 📌 Project Highlights

- ✅ Trained a CNN (MobileNetV2) on 15 classes of plant leaf images
- ✅ Achieved ~90% test accuracy
- ✅ Visualized model predictions using Grad-CAM heatmaps
- ✅ Saved model for later use or deployment

---

## 🧠 Dataset Overview

- **Dataset**: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Total Classes**: 15  
- **Image Count**: 5152 total images (after splitting)
- **Examples of Classes**:
  - `Tomato_Late_blight`
  - `Potato___healthy`
  - `Pepper__bell___Bacterial_spot`
  - `Tomato__Tomato_mosaic_virus`

---

## 🏗️ Model Architecture

- **Base Model**: MobileNetV2 (pretrained on ImageNet)
- **Input Size**: 224 × 224
- **Custom Head**:
  - Global Average Pooling
  - Dropout
  - Dense (15 classes, softmax)

---

## 🔍 Performance Metrics

| Metric         | Score |
|----------------|-------|
| **Accuracy**   | ~90%  |
| **Macro F1-score** | ~0.89 |
| **Best Classes** | Tomato_YellowLeaf_Curl_Virus, Tomato_healthy |
| **Challenging Classes** | Tomato_Early_blight, Target_Spot |

---

## 📊 Confusion Matrix

<img width="1398" height="1190" alt="download" src="https://github.com/user-attachments/assets/87cdc01a-5572-4460-a609-8e0d1f41aa0d" />


*Confusion Matrix visualizing model predictions across 15 classes*

---

## 🔬 Grad-CAM Visualization

Grad-CAM heatmaps show **which parts of the leaf the model focused on** while predicting.

| Original | Grad-CAM Overlay |
|----------|------------------|
| ![orig](sample_leaf.jpg) | ![cam](gradcam_overlay.jpg) |

---

## 💾 How to Use

### 1. Train the Model
```python
model.fit(train_generator, epochs=10, validation_data=val_generator)
```
### 2. Save the Model
``` 
model.save("plant_disease_model.h5")
```
### 3. Load the Model
```
from tensorflow.keras.models import load_model
model = load_model("plant_disease_model.h5")
```

### 4. Predict and Visualize
```
pred = model.predict(img_array)
# ...follow with Grad-CAM visualization
```

### 5. File Structure
```
├── plant_disease_model.h5          # Saved Keras model
├── GradCAM_Visualizer.ipynb        # Notebook with Grad-CAM
├── confusion_matrix.png            # Heatmap image
├── README.md
```

### 6. Future Work
- Improve classification using EfficientNet or ResNet
- Deploy with Gradio or Streamlit for web app
- Augment data to boost weak classes (e.g. Early blight)

### 7. Acknowledgements
- Dataset: PlantVillage on Kaggle
- Model: MobileNetV2 via TensorFlow Keras Applications


