import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
from waitress import serve

# from app.pages import sales
sales = pd.read_csv("../data/sales.csv")
returns = pd.read_csv("../data/returns.csv")

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
server = app.server
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
            dbc.Row([
                dbc.Col("MARQET", width = 4, className = "logo"),
                dbc.Col([
                    dbc.Row([
                        dbc.Col(
                                [dbc.NavLink(page["name"], href=page['path'], style={"color":"black"})],)
                            for page in dash.page_registry.values()
                    ], className = "nav-subtext", align = 'center', justify = 'end')
                        
            ], width = 3),
            ], justify= 'between',
            className = "nav-card"),
            dbc.Row([dash.page_container])
            ], className = "application")
]
)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8080)
    #serve(app, host='0.0.0.0', port=8080)

