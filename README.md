# 📄 Resume Keyword Tracker & Matcher

An intuitive Streamlit application designed to evaluate resume compatibility against job descriptions using automated text extraction, NLP preprocessing, and TF-IDF semantic scoring.

---

### 🌐 Live Demo & Repository

App link : https://resume-keyword-tracker-hssgsqsbmn33dpca4f3rtg.streamlit.app/

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github&logoColor=white)](https://github.com)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)

---

### 📌 Features

- 📑 **PDF Resume Parsing**: Extracts structured text directly from PDF resumes using `pdfplumber`.
- 🔍 **Keyword & Semantic Matching**: Computes term relevance and similarity matrices using Scikit-Learn's `TfidfVectorizer`.
- 🛑 **Stopword Normalization**: Cleans and normalizes text streams with automated NLTK corpus downloads.
- ⚡ **Interactive Web Interface**: Instant feedback and score breakdowns powered by Streamlit Community Cloud.

---

### 🛠️ Tech Stack & Badges

| Category | Tools / Libraries |
| :--- | :--- |
| **Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Text Processing** | ![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=flat) |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) |
| **PDF Extraction** | ![PDFPlumber](https://img.shields.io/badge/pdfplumber-Parsing-lightgrey?style=flat) |
| **Deployment** | ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-Deployed-success?style=flat&logo=streamlit&logoColor=white) |

---

### 📁 Project Structure

```text
resume-keyword-tracker/
├── apps.py            # Streamlit frontend & application entry point
├── extractor.py       # PDF parsing & text extraction logic
├── analyzer.py        # Text preprocessing, TF-IDF matching, & scoring
├── requirements.txt   # Third-party runtime dependencies
└── README.md          # Project documentation
