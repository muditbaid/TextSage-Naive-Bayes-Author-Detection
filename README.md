# Naive Bayes Text Classification

This repository contains an implementation of a **Naive Bayes-based text classifier** for author identification, developed as part of the *CSCI 6380 Data Mining* course. The model classifies text segments based on their author using **MultinomialNB** and **BernoulliNB** classifiers from Scikit-Learn.

## 📌 Project Overview
The goal of this project is to classify text excerpts by author using **Naive Bayes classifiers**. The dataset consists of literary works from **Project Gutenberg and the Internet Archive**, preprocessed and vectorized for training and testing.

### 📝 Features Implemented
- **Text Preprocessing**: Tokenization, stopwords removal, and part-of-speech tagging.
- **Vectorization**: Using `CountVectorizer` to transform text into numerical format.
- **Training & Testing**: MultinomialNB and BernoulliNB classifiers trained on book excerpts.
- **Resampling**: Balancing training data for improved accuracy.
- **Evaluation**: Accuracy reports and confusion matrices for model performance analysis.

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/muditbaid/TextSage-Naive-Bayes-Author-Detection.git
cd TextSage-Naive-Bayes-Author-Detection
```

### 2️⃣ Install Dependencies
Create a virtual environment and install the required libraries:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Run the Jupyter Notebook
```bash
jupyter notebook Naive_Bayes.ipynb
```

## 📊 Results & Performance
The results of various experiments, including accuracy reports and confusion matrices, are stored in the `results/` folder. Key findings:
- **Baseline MultinomialNB** performed well but improved with additional preprocessing.
- **BernoulliNB** showed different sensitivity to stopword removal and text transformations.
- **Resampling training data** enhanced model performance significantly.

## 📂 Repository Structure
```
.
├── data/                 # Sample text files used for training/testing
├── results/              # Classification reports and confusion matrices
├── Naive_Bayes.ipynb     # Jupyter Notebook with code implementation
├── text_utilities.py     # Helper functions for text preprocessing
├── requirements.txt      # Dependencies for the project
├── .gitattributes        # Git LFS tracking configuration
├── .gitignore            # Ignoring unnecessary files
└── README.md             # This document
```

## 🛠️ Future Improvements
- Implement **TF-IDF vectorization** instead of `CountVectorizer`.
- Fine-tune hyperparameters for **optimal accuracy**.
- Experiment with **other classification models** beyond Naive Bayes.

## 📌 References
- [Project Gutenberg](https://www.gutenberg.org/)
- [Scikit-Learn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)

## 📝 License
This project is for educational purposes under the *CSCI 6380 Data Mining* course. Free to use with attribution.

---
Feel free to contribute by submitting a pull request! 🚀
