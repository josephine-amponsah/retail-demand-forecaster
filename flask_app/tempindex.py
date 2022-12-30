import io
from flask import Flask, request, render_template
import flask
import plotly
import plotly.express as px
import pandas as pd
import webbrowser
import os
import requests, json
import chartjs
# from waitress import serve
from flask_bootstrap import Bootstrap

sales_url="https://github.com/ladyjossy77/retail-optimization/blob/master/data/sales.csv?raw=true"
s=requests.get(sales_url).content
sales_data =pd.read_csv(io.StringIO(s.decode('utf-8')))

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
# server = Flask(__name__)
app = Flask(__name__, template_folder= 'templates', static_folder= 'static')


# @app.route('/')
# def pages():
#     return render_template('dashboard.html')

@app.route('/', methods=['GET', 'POST'])
# def dropdown():
#     years = sales_data["year"].unique().tolist()
#     return render_template('dashboard.html', years = years)
def monthlyChart():
    
    # fig1 = px.line(sales_data, x ="year", y = "Order_Demand", )
    # years = sales_data["year"].unique().tolist()
    # sales = sales_data[sales_data["year"] == 2017]
    # data = sales.groupby("month_year")["Order_Demand"].sum()
    # # test_data = px.data.itis()
    # labels = sales["month_year"]
    # values = data
    # gJSON = json.dumps(labels, values)
    return render_template('dashboard.html')

@app.route('/project', methods=['GET'])
def projections_page():
    return render_template('proj.html')

@app.route('/tables', methods=['GET'])
def data_page():
    sales = sales_data[sales_data["year"] == 2016]
    data = sales.groupby("month_year")["Order_Demand"].sum()
    info = data.reset_index(drop= False)
    # test_data = px.data.itis()
    x = []
    y = []
    for i, j in zip(info.month_year, info.Order_Demand):
        x.append(i)
        y.append(j)
    return render_template('data.html', label = json.dumps(x), value = json.dumps(y))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

