import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# app = Dash(__name__)
dash.register_page(__name__, path = "/")
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

revSummary = ['Products Sold', 'Revenue', 'Avg. Purchase',  'Freight Revenue']

layout = html.Div([
    dbc.Row([
        dbc.Row([
            dbc.Col([
                  html.Div([
                      html.I(className="bi bi-search"),
                      html.I(className="bi bi-bell-fill"),
                      html.I(className="bi bi-person-circle"),
                  ], className='icon-bar'),
                  ],  width=3)
        ], justify="end"),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col(dbc.Card(
                children=[html.Div(title), html.Div("value", className='value'), html.Div("description")], className='summary-cards',),
                width=3,)
            for title in revSummary
        ]),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                dbc.Col([dcc.Graph(id="bar-trans-count")],
                        width= 6)
                ,
                dbc.Col([dcc.Graph(id="bar-trans-rev")], 
                        width= 6)
                ],),
            ], width= 9),
            dbc.Col([
                dbc.Container([dbc.Card(children=[html.Div("Charts")], className = "side-card")], className = "side-card")
            ], width= 3)
        ], justify = "between"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="bar-trans-count")
                ,
                dcc.Graph(id="bar-sales-rev")
            ], width=9),
            dbc.Col([
                dbc.Card(children=[html.Div("Charts")])
            ], width=3)
        ]),
    ], className="dashboard")


])

