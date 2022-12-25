import io
import dash
from flask import Flask, request, render_template
import flask
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import webbrowser
import os
import requests
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

@app.route('/', methods=['GET'])
def dropdown():
    return render_template('dashboard.html')

@app.route('/analysis', methods=['GET'])
def analysis_page():
    years = sales_data['year'].unique()
    return render_template('analytics.html', years = years)

@app.route('/project', methods=['GET'])
def projections_page():
    return render_template('proj.html')

@app.route('/tables', methods=['GET'])
def data_page():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

