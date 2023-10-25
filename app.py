"""
This is a simple Flask web application.

It provides a basic web service that responds with a 'Hello, World!' message when accessed.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
