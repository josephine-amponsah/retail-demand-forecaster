import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")
import requests
import io

# from app.pages import sales

sales_url="https://github.com/ladyjossy77/retail-optimization/blob/master/data/sales.csv?raw=true"
sales=requests.get(sales_url).content
sales_data =pd.read_csv(io.StringIO(sales.decode('utf-8')))
returns_url="https://github.com/ladyjossy77/retail-optimization/blob/master/data/returns.csv?raw=true"
returns=requests.get(returns_url).content
returns_data =pd.read_csv(io.StringIO(returns.decode('utf-8')))
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[
                dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc_css, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])
server = app.server
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
            html.Nav([
                html.Div([
                    html.A("MARQET", className = "navbar-brand txt-info"),
                    html.Div([
                        html.Ul([
                        html.Li([
                            html.A( "Analytics", className ="nav-link", href= dash.page_registry['pages.dashboard']['path'] ) 
                            ], className="nav-item"),
                        html.Li(
                                [
                            html.A("Projections", className ="nav-link", href= dash.page_registry['pages.projections']['path'])
                                ], className = "nav-item"),
                        html.Li(
                                [
                            html.A("Testing", className ="nav-link", href= dash.page_registry['pages.testing']['path'])
                                ], className = "nav-item"),
                    ], className="navbar-nav me-auto"
                    )
                    ], className = "collapse navbar-collapse" ,id="navbarColor02"),
                ], className= "container-fluid"),
            ],
            className = "navbar navbar-expand-lg navbar-dark bg-dark"),
            html.Br(),
            dbc.Row([dash.page_container], className = 'page-space')
    ], className = "")
]
)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8080)
    #serve(app, host='0.0.0.0', port=8080)

