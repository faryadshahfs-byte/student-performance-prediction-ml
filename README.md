# Student Exam Marks Prediction using Multiple Linear Regression

## Project Overview
This repository contains a production-ready implementation of a Multiple Linear Regression (Multivariate) model using Python and Scikit-Learn. The project focuses on predicting a student's `Exam Marks` based on multiple continuous features: `Study Hours`, `Attendance`, and `Assignments`. It also demonstrates enterprise data preprocessing techniques, specifically handling missing numerical values using Median Imputation.

## Dataset & Feature Engineering
The dataset consists of multiple independent features predicting a single continuous target variable.

### Variables:
* **Independent Variables ($X$):**
  1. `Study Hours`: Total hours spent studying.
  2. `Attendance`: Percentage of classes attended.
  3. `Assignments`: Number of successfully submitted assignments.
* **Dependent Variable ($y$):**
  * `Exam Marks`: Final test percentage obtained.

### Data Preprocessing (Missing Value Imputation):
The raw dataset contained missing data (`na`) in the `Assignments` feature at index 7. To ensure model robustness and avoid structural errors, **Median Imputation** was programmatically applied to clean the dataset before model fitting.

| Study Hours ($X_1$) | Attendance ($X_2$) | Assignments ($X_3$) | Exam Marks ($y$) |
| :--- | :--- | :--- | :--- |
| 1 | 60 | 2.0 | 40 |
| 2 | 65 | 3.0 | 45 |
| 3 | 70 | 4.0 | 55 |
| 4 | 72 | 5.0 | 60 |
| 5 | 75 | 5.0 | 65 |
| 6 | 80 | 5.0 | 72 |
| 7 | 82 | 5.0 (Imputed) | 77 |
| 8 | 85 | 8.0 | 83 |
| 9 | 90 | 9.0 | 89 |
| 10 | 95 | 10.0 | 95 |

## Technologies Used
* **Python 3**
* **NumPy**
* **Pandas** (Data Cleaning & Imputation)
* **Matplotlib**
* **Scikit-Learn** (Statistical Modeling)

## Model Architecture & Core Implementation

```python
import numpy as np
import pandas as pd
from sklearn import linear_model

# 1. Load Dataset
df = pd.read_csv('Multiple_Linear_Regression.csv')

# 2. Data Preprocessing: Convert column to numeric and impute missing values with Median
df['Assignments'] = pd.to_numeric(df['Assignments'], errors='coerce')
median_assignments = df['Assignments'].median()
df['Assignments'].fillna(median_assignments, inplace=True)

# 3. Model Training
lr = linear_model.LinearRegression()
lr. fit(df[['Study Hours', 'Attendance', 'Assignments']], df['Exam Marks'])
