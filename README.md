---
title: Textblob Sentiment Demo
emoji: 🦀
colorFrom: blue
colorTo: red
sdk: gradio
sdk_version: 4.44.0  # Or 5.23.1 if you want the latest
app_file: app.py
pinned: false
---

# Sentiment Analysis with Python & Hugging Face

[![Open in Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/nuna-bit/textblob-sentiment-demo)

## Overview
The primary objective of this repository is to demonstrate a modern AI development workflow: from local experimentation to automated cloud deployment. This project showcases how to use **TextBlob** for sentiment analysis and **GitHub Actions** to automatically sync code with **Hugging Face Spaces**.

### Live Demo
You can try the sentiment analyzer directly in your browser without installing anything:
👉 **[Click here to open the Interactive Demo](https://huggingface.co/spaces/nuna-bit/textblob-sentiment-demo)**

---

## Technical Details
This project uses a rule-based Natural Language Processing (NLP) approach.
- **Library:** TextBlob (built on NLTK).
- **Metric:** Calculates "Polarity" (a score from -1.0 to 1.0) to determine if text is Positive, Negative, or Neutral.
- **CI/CD:** Automated deployment via GitHub Actions (syncing `app.py` and `requirements.txt`).

## Local Setup & Usage

### Prerequisites
- Python 3.10 or newer.
- `pip` package manager.

### Install & Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nuna-bit/Sentiment-Analysis-with-Python.git](https://github.com/nuna-bit/Sentiment-Analysis-with-Python.git)
   cd Sentiment-Analysis-with-Python
2. **Install dependencies**
    ```bash
   pip install -r requirements.txt
4. **Run the Script**
   ```bash
   python sentiment_analysis.py

## Project Structure
- `app.py`: The Gradio web interface running on Hugging Face
- `sentiment_analysis.py`: The core logic for local command-line usage
- `.github/workflows/`: Automation script for syncing with the cloud
- `requirements.txt`: Necessary libraries (TextBlob, Gradio, Setuptools).
   
---

## License 
This project is licensed under the MIT License. It is intended for educational purposes and personal use. For any commercial use or redistribution, please refer to the terms mentioned in the license file.

---

> [!Note]
>  This repository is primarily for educational purposes

