# 🎙️ IELTS AI-Shadow Examiner

**Rocket-fast, AI-powered speaking practice for IELTS aspirants.**  
*Developed by **Arrya Thakur** for Leap Finance Internship Prototype.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/) 

## 🚀 Overview

The **IELTS AI-Shadow Examiner** is a real-time web application designed to simulate the high-pressure environment of the IELTS Speaking Test (Part 2). Unlike standard voice recorders, this app uses multimodal Generative AI to **listen, transcribe, and grade** your response in a single step, providing instant feedback just like a real examiner.

## ✨ Key Features

*   **🗣️ Real-Time AI Analysis:** Uses **Google Gemini 2.0 Flash** to process audio directly (multimodal) for ultra-low latency.
*   **📝 Instant Transcription:** Converts speech to text automatically to help you spot errors.
*   **📊 Band Score Prediction:** Grades your response on a 0-9 scale based on official IELTS criteria:
    *   *Lexical Resource*
    *   *Grammatical Range*
    *   *Coherence & Fluency*
*   **🎯 "Leap Fix" Engine:** Identifies your biggest weakness and suggests one immediate, actionable fix.
*   **📱 Responsive UI:** Built with Streamlit for a clean, professional interface on any device.

## 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/) (Python)
*   **AI Engine:** [Google Gemini API](https://ai.google.dev/) (gemini-flash-latest) via `google-generativeai`
*   **Audio Processing:** Streamlit Native Audio Input
*   **Deployment:** Streamlit Community Cloud

## ⚙️ Local Setup Guide

If you want to run this app on your own machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/arrya5/ielts-shadow-app.git
cd ielts-shadow-app
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GOOGLE_API_KEY="your_actual_api_key_here"
```
*(Get a free key from [aistudio.google.com](https://aistudio.google.com/))*

### 5. Run the App
```bash
streamlit run app.py
```

## ☁️ Deployment Guide

This app is designed to be deployed instantly on **Streamlit Community Cloud**:

1.  Push your code to GitHub.
2.  Go to [share.streamlit.io](https://share.streamlit.io/).
3.  Click **New App** and select this repository.
4.  **Crucial:** In "Advanced Settings", add your API Key to the **Secrets** section:
    ```toml
    GOOGLE_API_KEY = "your_actual_api_key_here"
    ```
5.  Click **Deploy**!

## 👨‍💻 Author

**Arrya Thakur**  
*Computer Science Student at SRM University*  
*Aspiring Builder & AI Engineer*

---
*Built with ❤️ for the Leap Finance "Shadow a Founder" Challenge.*
