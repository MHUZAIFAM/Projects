# 🩺 Diabetes Prediction using Machine Learning

This project uses machine learning models to predict the likelihood of diabetes in patients based on medical diagnostic measurements. It is based on the **Pima Indians Diabetes Dataset** from Kaggle.

## 📁 Dataset
- **Source:** [Kaggle - Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Records:** 768 samples
- **Features:** 8 input features + 1 target variable (`Outcome`)

| Feature                    | Description                                      |
|----------------------------|--------------------------------------------------|
| Pregnancies                | Number of times pregnant                         |
| Glucose                    | Plasma glucose concentration                     |
| BloodPressure              | Diastolic blood pressure (mm Hg)                |
| SkinThickness              | Triceps skin fold thickness (mm)                |
| Insulin                    | 2-Hour serum insulin (mu U/ml)                  |
| BMI                        | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction   | Diabetes pedigree function                      |
| Age                        | Age in years                                    |
| Outcome                    | 0 = Non-diabetic, 1 = Diabetic (Target)         |

---

## 🚀 Project Workflow

### 1. **Data Preprocessing**
- Replaced 0s in `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` with median values
- Scaled features using `StandardScaler`
- Split dataset into train/test sets (80/20)

### 2. **Models Trained**
- Logistic Regression ✅ (best test accuracy)
- K-Nearest Neighbors
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

### 3. **Model Evaluation**
- Metrics used: Accuracy, ROC AUC, Confusion Matrix, Classification Report
- Best performing model: **Logistic Regression**
    - Accuracy: ~0.76
    - ROC AUC: ~0.82

---

## 💾 Saved Artifacts
- `diabetes_logreg_model.pkl`: Trained Logistic Regression model
- `scaler.pkl`: Scaler used to preprocess features

---

## 🧪 How to Use

```python
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('diabetes_logreg_model.pkl')
scaler = joblib.load('scaler.pkl')

# Example patient input: [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
patient = np.array([[2, 120, 70, 22, 85, 32.0, 0.5, 25]])

# Scale and predict
patient_scaled = scaler.transform(patient)
prediction = model.predict(patient_scaled)

print("Diabetes Prediction:", "Positive" if prediction[0] == 1 else "Negative")
```

## 👨‍💻 Author
### M Huzaifa
Machine Learning | Computer Vision | AI Health Projects


