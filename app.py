from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Function to fetch stock data
def fetch_stock_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

# Function to create a plot
def create_open_close_plot(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data['Open'], label='Open', marker='o', linestyle='-', markersize=4)
    plt.plot(data.index, data['Close'], label='Close', marker='o', linestyle='-', markersize=4)
    plt.title('Opening and Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    return plt

# Define a route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        stock_symbol = request.form.get("stock_symbol")
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=10)
        stock_data = fetch_stock_data(stock_symbol, start_date, end_date)
        plot = create_open_close_plot(stock_data)

        img = BytesIO()
        plot.savefig(img, format="png")
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template("home.html", stock_symbol=stock_symbol, plot_url=plot_url)

    return render_template("home.html", stock_symbol="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


"""just simple web application"""
#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def index():
"""
    This function handles the root route.
    It returns a 'Hello, World!' message when the root route is accessed.
    Returns:
        str: A greeting message.
    """
 #   return 'Hello, World!'

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port=80)


