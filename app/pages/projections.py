import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table

# app = Dash(__name__)
dash.register_page(__name__, path = '/projections')
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
sales = pd.read_csv("../data/sales.csv")
returns = pd.read_csv("../data/returns.csv")

revSummary = ['Revenue', 'Transactions', 'Avg. Purchase',  'Profit']

layout = html.Div([
    dbc.Row([
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([dcc.DatePickerRange()], width = 3),
            dbc.Col([dcc.Dropdown()], width = 3),
            dbc.Col([dbc.Button()], width = 3),
            dbc.Col([dbc.Button("Download")], width = 3),
        ]),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dcc.Graph(id="bar-trans-count", className = "graph-style")
                ]),
            ], width=6),
            dbc.Col([
                dash_table.DataTable(
                id='table-container',
                data=[],
                columns=[{"name":i,"id":i,'type':'text'} for i in sales.columns],
                style_table={'overflow':'scroll','height':600},
                style_cell={'textAlign':'center'},
                row_deletable=True,
                editable=True)
            ], width= 6)
        ], style={"height": "100vh"})
    ], className="dashboard")


])