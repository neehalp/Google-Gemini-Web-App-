## 🧾 Project Structure for Heroku
```bash
google-gemini-web-app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Procfile
└── .env (not pushed to GitHub)
```

## 🛠️ Step-by-Step Deployment

### 1. Login to Heroku
```bash
heroku login
```

### 2. initialize Git
```bash
git init
git add .
git commit -m "Initial commit"
```

### 3. Create Heroku App
```bash
heroku create your-app-name
```

### 4. Set Buildpack (Python)
```bash
heroku buildpacks:set heroku/python
```

### 5. Set Environment Variable
```bash
heroku config:set GOOGLE_API_KEY=your_google_api_key
```
 
### 6. Deploy to Heroku
```bash
git push heroku master
```

### 7. Open the APP'
```bash
heroku open
```
## ⚙️ Important Files
Procfile
```bash
web: python app.py
```

