from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    This function handles the root endpoint and returns a greeting.

    Returns:
        str: A greeting message.
    """
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
