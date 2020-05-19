import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import json
import flask as flask




def fetch_stock_info(ticker,start_date,end_date):
    df = web.DataReader(ticker,"yahoo", start_date, end_date)
    df = df.to_json()
    return df

# print(fetch_stock_info("TSLA","2019-06-29","2019-11-17"))
    
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home():
    stock_info = fetch_stock_info("TSLA","2019-06-29","2019-11-17")
    return f"<h1>{stock_info}</h1>"


app.run()