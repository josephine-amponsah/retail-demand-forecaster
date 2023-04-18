import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask_caching import Cache
import os
import requests 
import io
import joblib
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[
                dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc_css, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])
server = app.server

sales_url="https://raw.githubusercontent.com/ladyjossy77/retail-demand-forecaster/master/data/app_data.csv"
timeout = 20

cache = Cache(server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

@cache.memoize(timeout= timeout)
def app_data():  # sourcery skip: inline-immediately-returned-variable
    sales_data =pd.read_csv( sales_url, on_bad_lines='error', index_col= 0)
    df = sales_data.to_json(date_format='iso')
    return df

app.layout = html.Div([
    dcc.Store(id ="sales-store", data = app_data()),
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
                            html.A("Documentation", className ="nav-link", href= dash.page_registry['pages.documentation']['path'])
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
    # model = joblib.load("modules/forecaster.pkl")
    app.run_server(debug=True, host='127.0.0.1', port=8080)
    #serve(app, host='0.0.0.0', port=8080)

