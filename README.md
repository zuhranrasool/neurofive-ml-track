# 🚢 Titanic Survival Prediction - Exploratory Data Analysis (EDA)

A professional data analysis project that explores the famous Titanic dataset using Python, Pandas, Matplotlib, and Seaborn. This project performs comprehensive Exploratory Data Analysis (EDA) to understand passenger demographics, identify missing values, analyze survival patterns, and visualize important relationships within the dataset.

---

## 📌 Project Overview

The Titanic disaster is one of the most well-known tragedies in history. This project analyzes the Titanic passenger dataset to discover patterns and insights related to passenger survival.

The project focuses on data exploration, visualization, and statistical analysis before applying any machine learning models.

---

## 🎯 Objectives

- Explore the Titanic dataset.
- Understand the dataset structure.
- Detect missing values.
- Perform statistical analysis.
- Visualize important features.
- Discover survival patterns.
- Prepare the dataset for future machine learning tasks.

---

## 🛠️ Technologies Used

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub
- VS Code
- Anaconda

---

## 📁 Project Structure

```
neurofive-ml-track/
│
├── data/
│   └── train.csv
│
├── notebooks/
│   └── Titanic_EDA.ipynb
│
├── images/
│   ├── missing_values.png
│   ├── survival_distribution.png
│   ├── gender_distribution.png
│   ├── passenger_class_distribution.png
│   ├── age_distribution.png
│   ├── fare_distribution.png
│   ├── correlation_heatmap.png
│   ├── survival_by_gender.png
│   └── survival_by_class.png
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 📊 Dataset Information

- **Dataset:** Titanic - Machine Learning from Disaster
- **Source:** Kaggle
- **Records:** 891
- **Features:** 12

### Features

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

## 🔍 Exploratory Data Analysis (EDA)

The project includes:

- Dataset Information
- Summary Statistics
- Missing Value Analysis
- Duplicate Record Check
- Data Type Analysis
- Numerical Feature Analysis
- Categorical Feature Analysis
- Correlation Analysis

---

## 📈 Visualizations

The following visualizations were created:

- Missing Values Overview
- Passenger Survival Distribution
- Gender Distribution
- Passenger Class Distribution
- Age Distribution
- Fare Distribution
- Correlation Heatmap
- Survival by Gender
- Survival by Passenger Class

---

## 📌 Key Findings

- Most passengers travelled in **Third Class**.
- Female passengers had a significantly higher survival rate than male passengers.
- First Class passengers showed the highest survival rate.
- Cabin contained the largest number of missing values.
- Most passengers were between **20 and 40 years** of age.
- Ticket fares were positively skewed with a few high-value outliers.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/zuhranrasool/neurofive-ml-track.git
```

Move into the project directory:

```bash
cd neurofive-ml-track
```

Create the Conda environment:

```bash
conda create -n neurofive_ml python=3.12 -y
```

Activate the environment:

```bash
conda activate neurofive_ml
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```
notebooks/Titanic_EDA.ipynb
```

Run all notebook cells to reproduce the analysis and visualizations.

---

## 🔮 Future Improvements

- Perform data preprocessing.
- Handle missing values.
- Feature engineering.
- Train machine learning models.
- Compare multiple classification algorithms.
- Evaluate model performance.
- Deploy the model as a web application.

---

## 👨‍💻 Author

**Zuhran Rasool**

Artificial Intelligence Intern

GitHub: https://github.com/zuhranrasool

---

## 📜 License

This project is licensed under the MIT License.
## Task 3 — Titanic Survival Prediction

### Machine Learning Classification

Task 3 extends the Titanic project from exploratory data analysis and data cleaning into machine learning classification.

The objective is to build a Logistic Regression model that predicts whether a Titanic passenger survived based on selected passenger features.

### Project Progression

- **Task 1:** Exploratory Data Analysis (EDA)
- **Task 2:** Data Cleaning & Visualization
- **Task 3:** Machine Learning Classification
### Machine Learning Approach

#### Dataset
The project uses the Titanic dataset from `data/train.csv`.

#### Features
The following features were selected for prediction:

- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

`PassengerId` was excluded because it does not provide meaningful predictive information for passenger survival.

#### Target Variable
The target variable is `Survived`, where:

- `0` = Did not survive
- `1` = Survived

#### Data Preprocessing
The dataset was prepared by handling missing values during the previous data-cleaning task. Numerical features were standardized using `StandardScaler`, while categorical features were converted into numerical form using `OneHotEncoder`.

#### Train/Test Split
The dataset was divided into training and testing sets using an 80/20 split with stratification to maintain a similar survival distribution in both sets.

#### Machine Learning Model
A Logistic Regression classifier was used to predict Titanic passenger survival.

The preprocessing and model training workflow was organized using a scikit-learn `Pipeline` and `ColumnTransformer`.
### Model Accuracy

The Logistic Regression model achieved an accuracy of **80.45%** on the test dataset.

This accuracy represents the percentage of Titanic passengers in the test set that were correctly classified as either survivors or non-survivors.
### Confusion Matrix

The confusion matrix was used to evaluate the classification results of the Logistic Regression model.

It shows four types of predictions:

- **True Negative (TN):** Passengers who did not survive and were correctly predicted as non-survivors.
- **False Positive (FP):** Passengers who did not survive but were incorrectly predicted as survivors.
- **False Negative (FN):** Passengers who survived but were incorrectly predicted as non-survivors.
- **True Positive (TP):** Passengers who survived and were correctly predicted as survivors.

The confusion matrix provides more detailed information about the model's correct and incorrect predictions beyond the overall accuracy.