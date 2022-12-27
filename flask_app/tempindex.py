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
def dropdown():
    years = sales_data["year"].unique().tolist()
    return render_template('dashboard.html', years = years)
def monthlyChart():
    df = px.data.iris()
    labels = sales_data["month_year"]
    value = sales_data["Order_Demand"]
    fig1 = px.scatter(x ="sepal_length", y = "sepal_width", data = df)
    graphJSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphJSON = graphJSON)

@app.route('/project', methods=['GET'])
def projections_page():
    return render_template('proj.html')

@app.route('/tables', methods=['GET'])
def data_page():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

