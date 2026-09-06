# 🧠 Brain Tumor Detection using CNN

This project uses a Convolutional Neural Network (CNN) to classify brain MRI images into 4 tumor types using the **Brain Tumor MRI Dataset**.

---

## 📂 Dataset
- Source: Kaggle
- Structure:
/Training/
glioma/
meningioma/
pituitary/
no_tumor/
/Testing/
same 4 classes

- Pre-sorted into training and testing sets.

---

## 🧠 Model Architecture
- Built using TensorFlow/Keras
- CNN layers: Conv2D → MaxPooling → Flatten → Dense
- Trained for 15 epochs with data augmentation

---

## 📈 Results
- ✅ Training Accuracy: ~91%
- ✅ Validation Accuracy: ~83%
- ✅ Test Accuracy: **84.82%**
- Loss and accuracy monitored during training

---

## 🔍 Tumor Localization (Grad-CAM)
Grad-CAM used to visualize **which region of the MRI** the CNN focused on when making predictions.

---

## 🚀 How to Run
1. Clone the repo or open in Google Colab / Kaggle
2. Train the CNN or load saved model
3. Run Grad-CAM to visualize predictions

---

## 📦 Requirements
- Python 3
- TensorFlow / Keras
- OpenCV
- NumPy, Matplotlib

---

## ✨ Credits
- Dataset from Kaggle
- Model built by Muhammad Huzaifa

