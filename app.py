from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# Set your OpenAI API key here
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    response = ask_gpt(user_message)
    return jsonify({"response": response})

def ask_gpt(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('choices')[0].get('message').get('content')
    else:
        return "Error: Unable to reach OpenAI API."

if __name__ == '__main__':
    app.run(debug=True)
