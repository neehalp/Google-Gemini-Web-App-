from flask import Flask, request, render_template
import textwrap
import os
import google.generativeai as genai

app = Flask(__name__)

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Ensure that the GOOGLE_API_KEY environment variable is set
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        query = request.form['query']
        response = model.generate_content(query)
        markdown_text = to_markdown(response.text)
        response_text = markdown_text
    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
