# 🌐 Google Gemini AI Web App

This project is a lightweight **Flask web application** that integrates with **Google's Gemini AI (via the `google-generativeai` SDK)** to provide AI-powered text generation directly through a browser interface.

## 🚀 Features
- Simple web-based UI to interact with Google's Gemini model.
- Accepts user queries and returns AI-generated responses in markdown format.
- Easy to deploy locally or on cloud platforms like **Heroku** or **Vercel**.

## 🧩 Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML (Jinja templating)
- **AI Integration**: `google-generativeai` for Gemini Pro model
- **Environment Management**: `python-dotenv`

## 🔧 How to Use

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/google-gemini-web-app.git
cd google-gemini-web-app
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file
```bash
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run The Application
```bash
python app.py
```
### 6. Get Your Gemini API Key here: 
https://aistudio.google.com/app/apikey
