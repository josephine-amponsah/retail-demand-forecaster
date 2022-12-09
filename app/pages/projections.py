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
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    html.Div(["Year"]),
                    dcc.Dropdown(
                    #   options = year_filter,
                    #   value = year_filter[-2],
                    #   id = "date-year-filter"
                  ),
                    # dcc.Input()
                    
                    ]),
                dbc.Row([])
            ], className = "filter-card")
            ], width = 2),
        dbc.Col([
            html.Br(),
            dbc.Row([
                dbc.Card([
                    dcc.Graph(id="bar-trans-count", className = "graph-style"),
                ], className = "graph-card")
        ],),
            html.Br(),
            dbc.Row([
                dbc.Card([
                    dcc.Graph(id="bar-trans-count", className = "graph-style"),
                ], className = "graph-card")
        ],)
    
            ], width = 5),
        dbc.Col([
                dash_table.DataTable(
                id='table-container',
                data=[],
                columns=[{"name":i,"id":i,'type':'text'} for i in sales.columns],
                style_table={'overflow':'scroll','height':600},
                style_cell={'textAlign':'center'},
                row_deletable=True,
                editable=True)
            ], width= 5)
        ], className="dashboard")


])