# Platform-Based Advertisement Recommendation System

<p align="center">
  <img src="https://raw.githubusercontent.com/abhiram-tekulapalli/project_readme_assets/main/header.svg" alt="Platform-Based Advertisement Recommendation System" width="100%" />
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://scikit-learn.org"><img src="https://img.shields.io/badge/Scikit--Learn-1.5+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"></a>
  <a href="https://pandas.pydata.org"><img src="https://img.shields.io/badge/Pandas-2.2+-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/NumPy-1.26+-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"></a>
  <a href="https://matplotlib.org"><img src="https://img.shields.io/badge/Matplotlib-3.9+-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"></a>
  <a href="https://seaborn.pydata.org"><img src="https://img.shields.io/badge/Seaborn-0.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn"></a>
  <a href="https://colab.research.google.com"><img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Google Colab"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License"></a>
</p>

---

## 🎯 Overview

The **Platform-Based Advertisement Recommendation System** is a machine learning project designed to recommend the most suitable advertising platform based on business and audience characteristics. The system analyzes factors such as product category, target audience, geography, brand awareness, product price range, and advertising budget to predict the most effective advertising platform.

This project demonstrates the complete machine learning workflow — from synthetic dataset generation through preprocessing, feature engineering, model training, evaluation, and recommendation generation.

---

## 📋 Problem Statement

Businesses often struggle to choose the right advertising platform due to the large number of available marketing channels. Selecting an inappropriate platform can lead to inefficient budget utilization and reduced campaign effectiveness. This project provides a **data-driven recommendation system** that assists businesses in selecting the most suitable advertising platform.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Platform Recommendation** | ML-powered advertisement platform recommendation |
| 📊 **Synthetic Dataset Generation** | Business-rule-based dataset with ~10,500 records |
| 🔧 **Auto Preprocessing** | Automatic feature encoding and data cleaning |
| 🌳 **Multi-class Classification** | 10 target platform classes |
| 🌲 **Random Forest Engine** | Primary recommendation model |
| 📈 **Baseline Comparison** | Logistic Regression for benchmarking |
| 📊 **Feature Importance** | SHAP/permutation importance analysis |
| 🎯 **Confusion Matrix** | Visualization of classification performance |
| 🔢 **Real-world Input Handling** | Numeric input validation and processing |
| 📦 **Modular Structure** | Clean, maintainable project architecture |

---

## 📊 Dataset

Since no publicly available dataset exists for platform-level advertisement recommendation, a **custom synthetic dataset** was generated using domain-inspired business rules.

| Characteristic | Value |
|----------------|-------|
| **Records** | ~10,500 |
| **Input Features** | 6 |
| **Target Classes** | 10 platforms |

### Features Used

1. **Product Category** — Type of product being advertised
2. **Target Audience** — Demographic segment
3. **Geography** — Target region/country
4. **Brand Awareness** — Current brand recognition level
5. **Product Price Range** — Pricing tier
6. **Advertising Budget** — Allocated marketing spend

### Target Platforms

The system predicts one of 10 platforms:
- Social Media: Facebook, Instagram, YouTube
- Search Engines
- Influencer Marketing
- OTT: Netflix, Amazon Prime, Disney+
- Cable Networks
- Newspaper

---

## 🏗️ Project Structure

```
advertisment-platform-recommendation-system/
├── data/                    # Generated datasets
├── notebooks/               # Jupyter notebooks for EDA & modeling
├── src/                     # Source code
│   ├── preprocessing.py     # Data preprocessing pipeline
│   ├── train.py             # Model training scripts
│   ├── evaluate.py          # Evaluation metrics
│   └── recommend.py         # Recommendation inference
├── models/                  # Trained model artifacts
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip / conda

### Installation

```bash
# Clone the repository
git clone https://github.com/abhiram-tekulapalli/advertisment-platform-recommendation-system.git
cd advertisment-platform-recommendation-system

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate dataset & train model
python src/train.py

# Run recommendation
python src/recommend.py --category "Electronics" --audience "Gen Z" --budget 50000
```

---

## 📈 Model Performance

| Model | Accuracy | F1-Score (Macro) | Training Time |
|-------|----------|------------------|---------------|
| **Random Forest** | **92.3%** | **0.91** | 45s |
| Logistic Regression | 78.5% | 0.76 | 12s |

*Feature importance analysis reveals `Advertising Budget` and `Product Category` as top predictors.*

---

## 🛠️ Technologies

<div align="center">

| Category | Tools |
|----------|-------|
| **Language** | Python 3.11+ |
| **ML Framework** | Scikit-Learn, Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Development** | Jupyter Notebook, Google Colab |
| **Version Control** | Git, GitHub |

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/abhiram-tekulapalli/project_readme_assets/main/footer.svg" alt="Footer" width="100%" />
</p>