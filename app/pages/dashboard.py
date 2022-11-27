import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# app = Dash(__name__)
dash.register_page(__name__, path = "/")
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

sales = pd.read_csv("../data/sales.csv")
returns = pd.read_csv("../data/returns.csv")

year_filter =  sales["year"].unique().tolist()
category_filter = sales["Product_Category"].unique().tolist()

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']

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
        dbc.Row([
            dbc.Col([
                  dcc.Dropdown(
                      options = year_filter,
                      value = year_filter[-1],
                      id = "date-year-filter"
                  ),
                  ],  width=3)
        ], justify="end"),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        dbc.Row([
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Products Sold"), 
                    html.Div( [],
                        id = "sales",className='value',),
                    html.Div("description")
                    ], className='summary-cards',)
                    ], width=3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Returns"), 
                    html.Div([], className='value', id ="returns"),
                    html.Div("description")
                    ], className='summary-cards',)
                    ], width = 3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Best Performing Warehouse"), 
                    html.Div([], className='value', id = "warehouse"),
                    html.Div("description")
                    ], className='summary-cards',),
                    ], width = 3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Highest Grossing Category"), 
                    html.Div([], className='value', id = "category"),
                    html.Div("description")
                    ], className='summary-cards',),
                ]
                    , width = 3)
                
                # 
        
            
        ]),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
            dbc.Col([
                  dcc.Dropdown(
                      options = year_filter,
                      value = year_filter[-1],
                      id = "date-time-filter"
                  ),
                  ],  width=3),
            dbc.Col([
                  dcc.Dropdown(
                      options = category_filter,
                      value = category_filter[-1],
                      id = "category-filter"
                  ),
                  ],  width=3)
        ], justify="end"),
                dbc.Row([
                dbc.Col([dcc.Graph(id="sales-over-time")],)
                        # width= 6)
                ,
                # dbc.Col([dcc.Graph(id="bar-trans-rev")], 
                #         width= 6)
                ],),
            ], width= 9),
            dbc.Col([
                dbc.Container([dbc.Card(children=[html.Div("Charts")], className = "side-card")], className = "side-card")
            ], width= 3)
        ], justify = "between"),
        # dbc.Row([
        #     dbc.Col([
        #         dcc.Graph(id="bar-trans-count")
        #         ,
        #         dcc.Graph(id="bar-sales-rev")
        #     ], width=9),
        #     dbc.Col([
        #         dbc.Card(children=[html.Div("Charts")])
        #     ], width=3)
        # ]),
    ], className="dashboard")


])

@callback(
    [Output("sales", "children"), Output("returns", "children"), Output("warehouse", "children"), Output("category", "children")], 
    Input("date-year-filter", "value")
)
def date_summary(year):
    # sum of sales and returns
    mask = sales.year == year
    mask2 = returns.year == year
    filtered_sales = sales.loc[mask,:]
    total_sales = filtered_sales["Order_Demand"].sum()
    total_sales = format(total_sales, ",")
    filtered_returns = returns.loc[mask2,:]
    total_returns = filtered_returns["Order_Demand"].sum()
    total_returns = format(total_returns, ",")
    
    #warehouse performance
    warehouse_data = filtered_sales.groupby("Warehouse")["Order_Demand"].sum().to_frame()
    best_warehouse = warehouse_data.idxmax(axis= 0)[0]
    
    #product category performance
    
    prod_cat = filtered_sales.groupby("Product_Category")["Order_Demand"].sum().to_frame()
    best_category =prod_cat.idxmax(axis= 0)[0]
    
    return [total_sales], [total_returns], [best_warehouse], [best_category]

@callback(
    [Output("sales-over-time", "value")],
    Input("date-time-filter", "value"),
    Input("category-filter", "value"),
)

def salesTrend(date, category):
    return 