# Platform-Based Advertisement Recommendation System

## Overview

The Platform-Based Advertisement Recommendation System is a machine learning project designed to recommend the most suitable advertising platform based on business and audience characteristics.

The system analyzes factors such as product category, target audience, geography, brand awareness, product price range, and advertising budget to predict the most effective advertising platform.

This project demonstrates the complete machine learning workflow, including dataset generation, preprocessing, feature engineering, model training, evaluation, and recommendation generation.

---

## Problem Statement

Businesses often struggle to choose the right advertising platform due to the large number of available marketing channels.

Selecting an inappropriate platform can lead to inefficient budget utilization and reduced campaign effectiveness.

This project aims to provide a data-driven recommendation system that assists businesses in selecting the most suitable advertising platform.

---

## Features

* Advertisement platform recommendation using Machine Learning
* Business-rule-based synthetic dataset generation
* Automatic preprocessing and feature encoding
* Multi-class classification approach
* Random Forest-based recommendation engine
* Logistic Regression baseline comparison
* Feature importance analysis
* Confusion matrix visualization
* Real-world numeric input handling
* Modular project structure

---

## Dataset

Since no publicly available dataset exists for platform-level advertisement recommendation, a custom synthetic dataset was generated using domain-inspired business rules.

### Dataset Characteristics

* Records: ~10,500
* Input Features: 6
* Target Classes: 10

### Features Used

1. Product Category
2. Target Age Group
3. Target Geography
4. Brand Awareness
5. Price Category
6. Budget Category

### Target Variable

Recommended Advertising Platform

---

## Recommended Platforms

The system predicts one of the following platforms:

* Social Media – Facebook
* Social Media – Instagram
* Social Media – YouTube
* Search Engines
* Influencer Marketing
* OTT – Netflix
* OTT – Amazon Prime
* OTT – Disney+
* Cable Networks
* Newspaper

---

## Machine Learning Pipeline

### Data Generation

* Synthetic dataset creation
* Business-rule-based labeling
* Class balancing

### Data Preprocessing

* Validation of inputs
* Label Encoding
* Feature transformation
* Train-Test Split

### Models Used

#### Logistic Regression

Used as a baseline classification model.

#### Random Forest Classifier

Selected as the final model due to superior performance and ability to learn complex decision patterns.

---

## Evaluation Metrics

The following metrics were used:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~58%     |
| Random Forest       | ~95%     |

Random Forest achieved the highest performance and was selected as the final recommendation model.

---

## Project Structure

Platform_Ad_Recommendation/

├── data/

│ └── platform_ad_dataset_FINAL.csv

├── notebooks/

│ └── advertisement_recommendation.ipynb

├── models/

│ ├── random_forest_model.pkl

│ ├── feature_encoders.pkl

│ └── target_encoder.pkl

├── results/

│ ├── confusion_matrix_random_forest.png

│ ├── feature_importance_random_forest.png

│ └── model_accuracy.txt

├── docs/

│ └── report_and_presentation

└── README.md

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

---

## Future Enhancements

* Integration with real advertising campaign data
* Web-based recommendation dashboard
* Automated campaign analytics
* Cost-per-click and ROI analysis
* Real-time recommendation updates

---

## Learning Outcomes

Through this project, the following concepts were implemented and explored:

* Dataset Generation
* Feature Engineering
* Data Preprocessing
* Classification Models
* Random Forest
* Logistic Regression
* Model Evaluation
* Feature Importance Analysis
* Recommendation Systems
* End-to-End Machine Learning Workflow

---

## Author

Abhiram Tekulapalli

B.Tech – Computer Science & Engineering (AI & ML)

Machine Learning Project – Platform-Based Advertisement Recommendation System
