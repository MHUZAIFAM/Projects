# MNIST Handwritten Digit Classification

This project uses a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset. The model is trained on 60,000 images and evaluated on 10,000 test images. After training for 10 epochs, the model achieves an accuracy of approximately 99% on the test dataset.

## Features
- Trains a CNN model on the MNIST dataset.
- Preprocessing of images to grayscale and normalization.
- Evaluation of model performance on test data.

## Requirements
- TensorFlow
- NumPy
- Matplotlib
- Keras
- Python 3.x

## Usage
1. Download the MNIST dataset or use the included dataset.
2. Run the training script to train the CNN model:
   ```bash
   python train_model.py
   ```
## Results
- Training Accuracy: ~99.87%
- Test Accuracy: ~99.04%
- Validation Accuracy: ~99.25%

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The MNIST dataset is provided by Yann LeCun and others.
The CNN model is implemented using TensorFlow/Keras.
