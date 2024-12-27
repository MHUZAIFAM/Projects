# Dogs vs Cats Image Classification

This project uses a Convolutional Neural Network (CNN) to classify images of dogs and cats. The dataset consists of around 25,000 images, with approximately 12,000 images per class (dog and cat). The goal is to create a model that can accurately distinguish between images of dogs and cats.

## Dataset

The dataset for this project is the **Kaggle Dogs vs. Cats Dataset**, which can be found [here](https://www.kaggle.com/datasets/karakaggle/kaggle-cat-vs-dog-dataset). The images are stored in two directories, one for each class:
- `Cat/` (Contains 12,491 images)
- `Dog/` (Contains 12,470 images)

## Project Overview

### Goal:
Classify images into two categories:
- **Dog**
- **Cat**

### Approach:
- **Preprocessing**: The images will be resized to a fixed size (e.g., 150x150 pixels) for input into the CNN.
- **Model**: A simple Convolutional Neural Network (CNN) will be trained to classify the images.
- **Evaluation**: The performance of the model will be evaluated using accuracy and other metrics such as confusion matrix and classification report.

### Libraries and Tools:
- Python 3.x
- TensorFlow / Keras for model building and training
- OpenCV for image preprocessing (optional)
- Matplotlib for visualizations

## Steps to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/dogs-vs-cats-classification.git
cd dogs-vs-cats-classification
```
### 2. Install Dependencies
You can install the required libraries by running:
```
pip install -r requirements.txt
```
requirements.txt:
```
tensorflow
keras
numpy
matplotlib
opencv-python
```
### 3. Download the Dataset
Download the dataset from Kaggle and extract it into the data/ directory of this project. Ensure the following directory structure:
```
data/
  |-- PetImages/
      |-- Cat/
      |-- Dog/
```
### 4. Train the Model
To train the model, run:
```
python train.py
```

This will
- Load the images
- Preprocess them (resize, normalize)
- Split them into training and validation sets
- Train the CNN model
- Save the trained model
### 5.
