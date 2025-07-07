# ❤️ Heart Disease Prediction using K-Nearest Neighbors (KNN)

This project predicts the likelihood of heart disease in patients using machine learning — specifically the **K-Nearest Neighbors (KNN)** algorithm — on the UCI Heart Disease dataset.

## 📁 Dataset

**Source**: [UCI Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/mragpavank/heart-diseaseuci)  
**Rows**: 303  
**Target Variable**: `target` (1 = disease, 0 = no disease)

## 🧠 Model Used

- **K-Nearest Neighbors (KNN)**
- Scikit-learn's `KNeighborsClassifier`
- Data preprocessed using `StandardScaler` and `OneHotEncoding` for categorical variables

## 📊 Evaluation Metrics

| Metric      | Score |
|-------------|-------|
| **Accuracy**        | 82.61% |
| **Precision (Class 0)** | 0.78 |
| **Recall (Class 0)**    | 0.78 |
| **Precision (Class 1)** | 0.86 |
| **Recall (Class 1)**    | 0.86 |
| **F1 Score (Macro Avg)**| 0.82 |

### 📉 Classification Report:

![download](https://github.com/user-attachments/assets/1a138c06-bcdf-4e7d-a836-6c5551603d37)




## 📌 Key Features Used

- Age, Sex, Chest Pain Type, Resting Blood Pressure
- Cholesterol, Fasting Blood Sugar
- Resting ECG, Max Heart Rate, Exercise Induced Angina
- ST Depression, Slope, Number of Vessels, Thalassemia

## 📦 Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn` for model building and evaluation

## ✅ How to Run

1. Load the dataset from Kaggle.
2. Preprocess data (one-hot encoding + scaling).
3. Train the `KNeighborsClassifier`.
4. Evaluate using confusion matrix and classification report.

## 🚀 Future Work

- Hyperparameter tuning using `GridSearchCV`
- Try other classifiers (XGBoost, Random Forest, SVM)
- Visualize ROC curves and feature importances

---

🔍 *This project is useful in early-stage detection of cardiovascular disease using non-invasive clinical features.*

