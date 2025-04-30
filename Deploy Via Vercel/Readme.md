## Project Structure for Vercel
```bash
google-gemini-web-app/
├── api/
│   └── index.py          # Flask logic
├── templates/
│   └── index.html        # Frontend HTML
├── requirements.txt
├── vercel.json
└── .env (not pushed to GitHub)
```

## Modify api/index.py
 Move app.py to api/index.py and modify as follows:
 ```bash
 from flask import Flask, request, render_template
import google.generativeai as genai
import os

app = Flask(__name__, template_folder="../templates")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        query = request.form["query"]
        response = model.generate_content(query)
        response_text = response.text
    return render_template("index.html", response_text=response_text)

# Vercel-compatible entry point
def handler(environ, start_response):
    return app(environ, start_response)
```

## Create vercel.json

```bash
{
  "builds": [
    { "src": "api/index.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "api/index.py" }
  ]
}
```
## 🔐 Add Environment Variables on Vercel
Go to your project on Vercel Dashboard, then:

Settings > Environment Variables

Add:
```bash 
GOOGLE_API_KEY=your_google_api_key_here
```
## Deploy via Vercel
Go to https://vercel.com/import

Select your GitHub repository

Click Deploy