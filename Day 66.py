#Day 66: External API call

#Fetch data from an external API and display it on a web page.

import requests
from flask import Flask, render_template

app = Flask(__name__)

# Fetch data from an external API
def fetch_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json() if response.status_code == 200 else []

@app.route('/')
def index():
    posts = fetch_posts()  # Fetch data from external API
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
