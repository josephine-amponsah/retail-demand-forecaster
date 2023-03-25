import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
from dash import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import sys
import json
import requests
import io
from flask_caching import Cache
sys.path.insert(0, '../modules')



# app = Dash(__name__)
dash.register_page(__name__, path = "/")
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# sales = app.sales_data()
# # store_sales = dcc.Store(id = 'sales-store', data = sales_data.to_dict('records'))
# year_filter =  sales["year"].unique().tolist()
# year_options = year_filter.sort() 
# category_filter = sales["Product_Category"].unique().tolist()
# warehouse_filter = sales["Warehouse"].unique().tolist()
summary_table = pd.DataFrame.from_dict({
    "categories":[], "orders":[], "returns":[], "net_sales":[], "yoy_growth":[]
})

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']

layout = html.Div([
    dcc.Store(id = "sales-data"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown( placeholder = 'Year', id = 'date-time-filter',
                 className="dbc year-dropdown .Select-control", value = 2016) 
            ], width=2),
        dbc.Col([
            html.Button( 'Download Report', id = 'downloader',
                 className="btn btn-info") 
            ], width = 2),
    ], justify= 'end'),
    html.Br(),
    # row with summary cards
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    html.Div(
                        [
                            html.Div([
                                html.P("Orders", className="card-text"),
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("501.36 K", className="card-title", id = "sum-of-orders"),
                                        html.P("15.89 %", className="card-text")
                                    ], width = 8),
                                    dbc.Col([
                                        html.I(className="bi bi-cart-check fa-3x icon-main")
                                    ], width = 4)
                                ])
                            ], className="card-body")
                        ], className= "card bg-light mb-3"
                    ), width=4
        ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div([
                                html.P("Returns", className="card-text"),
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("15.732 K", className="card-title"),
                                        html.P("15.89 %", className="card-text")
                                    ], width = 8),
                                    dbc.Col([
                                        html.I(className = "bi bi-arrow-left-square fa-3x icon-negative")
                                    ], width = 4)
                                ])
                            ], className="card-body")
                        ], className= "card bg-light mb-3"
                    ), width=4
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div([
                                html.P("Revenue", className="card-text"),
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("$3.65 M", className="card-title"),
                                        html.P("15.89 %", className="card-text")
                                    ], width = 8),
                                    dbc.Col([
                                        html.I(className = "bi bi-cash-coin fa-3x icon-positive")
                                    ], width = 4)
                                ])
                            ], className="card-body")
                        ], className= "card bg-light mb-3"
                    ), width=4
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(
                        [
                            html.Div([
                                html.H6("Monthly Sales", className="card-title"),
                                dcc.Graph( id = "monthly-sales-chart")
                            ], className="card-body")
                        ], className= "card bg-light mb-3"
                    ), width=12
                ),
            ]),
        ],),
        dbc.Col([
            html.Div(
                [
                    html.Div([
                        html.H6("Highlights", className="card-title"),
                        html.Br(),
                        dbc.Row([
                                dbc.Col([
                                    html.I(className="bi bi-arrow-up-right-square-fill fa-2x icon-main opacity")
                                ], width = 2),
                                dbc.Col([
                                    dbc.Row([
                                        dbc.Col(["Highest Grossing Category"])
                                    
                                    ]),
                                    dbc.Row([
                                        dbc.Col(["Name"], id ="hightest-cat-name", className = "border-right", width =4),
                                        dbc.Col(["Orders"], id ="highest-cat-orders", className = "border-right", width =4),
                                        dbc.Col(["Revenue"], id ="highest-cat-revenue", width =4),
                                    ]),
                                    # html.Div(["name"],),
                                    # html.Div(["orders"], id ="most-purchased-orders"),
                                    # html.Div(["revenue"], id ="most-purchased-revenue"),
                                ], width = 10)
                        ]),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                html.I(className="bi bi-arrow-up-right-square-fill fa-2x icon-main opacity")
                            ], width = 2),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(["Most Purchased Product"])
                                
                                ]),
                                dbc.Row([
                                    dbc.Col(["Name"], id ="most-purchased-name", className = "border-right", width =4),
                                    dbc.Col(["Orders"], id ="most-purchased-orders", className = "border-right", width =4),
                                    dbc.Col(["Revenue"], id ="most-purchased-revenue", width =4),
                                ]),
                                # html.Div(["name"],),
                                # html.Div(["orders"], id ="most-purchased-orders"),
                                # html.Div(["revenue"], id ="most-purchased-revenue"),
                            ], width = 10)
                            
                            
                        ]),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                html.I(className="bi bi-arrow-down-left-square-fill fa-2x icon-main opacity")
                            ], width = 2),
                             dbc.Col([
                                    dbc.Row([
                                        dbc.Col(["Least Purchased Product"])
                                    
                                    ]),
                                    dbc.Row([
                                        dbc.Col(["Name"], id ="least-purchased-name", className = "border-right", width =4),
                                        dbc.Col(["Orders"], id ="least-purchased-orders", className = "border-right", width =4),
                                        dbc.Col(["Revenue"], id ="least-purchased-revenue", width =4),
                                    ]),
                                    # html.Div(["name"],),
                                    # html.Div(["orders"], id ="most-purchased-orders"),
                                    # html.Div(["revenue"], id ="most-purchased-revenue"),
                                ], width = 10)
                        ]),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                html.I(className="bi bi-arrow-left-square-fill fa-2x icon-main opacity")
                            ], width = 2),
                             dbc.Col([
                                    dbc.Row([
                                        dbc.Col(["Most Returned Product"])
                                    
                                    ]),
                                    dbc.Row([
                                        dbc.Col(["Name"], id ="most-returned-name", className = "border-right", width =4),
                                        dbc.Col(["Orders"], id ="most-returned-orders", className = "border-right", width =4),
                                        dbc.Col(["Revenue"], id ="most-returned-revenue", width =4),
                                    ]),
                                    # html.Div(["name"],),
                                    # html.Div(["orders"], id ="most-purchased-orders"),
                                    # html.Div(["revenue"], id ="most-purchased-revenue"),
                                ], width = 10)
                        ]),
                        html.Br(),
                    ], className="card-body"),
                    
                ], className= "card border-light mb-3"
            )
        ,
            html.Div([
                html.Div([
                    html.Div(["Gauge Chart"]),
                    dcc.Graph(id = "gauge-chart")
                ], className = "card-body")
            ], className="card border-light mb-3"),
            
        ],width=4, className= "fixed-cards"),
        
    ], className = "fixed-section"),
    #row with graph and highlights card
    
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Top 10 Warehouses", className="card-title"),
                        html.Br(),
                        dbc.Row([
                                dbc.Col([
                                    html.I(className="bi bi-arrow-up-right-square-fill icon-main opacity")
                                ], width = 2),
                                
                                dbc.Col(["Name"]),
                                dbc.Col(["Orders"], id ="warehouse-orders", className = ""),
                                dbc.Col(["Revenue"], id ="warehouse-revenue"),
                                
                        ]),
                    ], className="card-body")
                ], className= "card bg-light mb-3 second-section"
            ), width=4
        ),
        dbc.Col(
            html.Div(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H6("Data", className="card-title"),
                            ], className="card-body"),
                        ], width=6),
                        
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown( placeholder = 'Warehouse', id = 'table-category-filter',
                                        className="dbc year-dropdown .Select-control") 
                                ], width=8),
                                dbc.Col([
                                    html.Button( 'Filter', id = 'table-filter',
                                        className="btn btn-info") 
                                ], width = 4),
                            ])
                            
                        ], width=6)
                        
                    ], justify= "between", className="details-table-nav"),
                    
                    dbc.Table.from_dataframe(summary_table, striped=True, bordered=True, hover=True, index=True)
                ], className= "card bg-light mb-3 details-table-section second-section"
            ), width=8
        , ),
    ],  )


])

# @callback(Output('sales-data', 'cdata'))
# def store_sales_data():  # sourcery skip: inline-immediately-returned-variable
    
#     return sales_data.reset_index().to_json(orient="split")

@callback(
    Output("date-time-filter", "options"),
    Input("sales-store", "data")
)
def filter_options(data):
    # sourcery skip: inline-immediately-returned-variable
    sales_data = pd.DataFrame(json.loads(data))
    options = sales_data["year"]
    options = options.unique()
    return options

@callback(
    [Output("sum-of-orders", "children"), ], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    total_orders = data["Order_Demand"].sum()
    return [total_orders]

@callback(
    Output("monthly-sales-chart", "figure"),
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)

def salesTrend(date, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == date]
    fig = px.histogram(data, y="Order_Demand", x="month_year", template="cyborg",  histfunc='sum', 
                       labels = {'Order_Demand':'Orders', "month_year": "Month-Year"})
    
    fig.update_layout(
        paper_bgcolor = '#222',
        margin={'l':20, 'r':20, 'b':0},
        font_color='white',
        # font_size=18,
       
        hoverlabel={'bgcolor':'black', 'font_size':12, },
        bargap=.40
        
    )
    fig.update_traces(
        # marker_bgcolor="#93c"
        marker = {
            'color': '#93c',
        }
        )
    fig.update_xaxes( # the y-axis is in dollars
        dtick= 30, 
        showgrid=True
    )
    
    return fig

@callback(
    Output("gauge-chart", "figure"),
    Input("date-time-filter", "value"),
    
)
def gauge(value):
    labels = ['Oxygen','Hydrogen']
    values = [4500, 2500]

# Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7)])
    
    fig.update_traces(
        marker_colors= ["#93c", "#f80"]
    )
    
    fig.update_layout(
        margin={'l':20, 'r':20, 'b':0, 't':0},
        height = 200
    )
    return fig
    
# @callback(
#     [Output("main-returned", "children"), Output("main-purchased", "children"), Output("main-lowest", "children"), 
#      Output("details-returned", "children"), Output("details-purchased", "children"), Output("details-lowest", "children")],
#     Input("date-year-filter", "value")
# )

# def highlights(year):
    # mask1 = sales.year == year
    # mask2 = returns.year == year
    # filtered_sales = sales.loc[mask1,:]
    # filtered_returns = returns.loc[mask2,:]
    
    # # most returned product
    # most_returned = filtered_returns.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    # returned = most_returned.idxmax(axis = 0)[0]
    # details_most_returned =format(most_returned["Order_Demand"].max(), ",")
    
    # # most purchased products
    
    # most_purchased = filtered_sales.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    # purchased = most_purchased.idxmax(axis = 0)[0]
    # details_most_purchased = format(most_purchased["Order_Demand"].max(), ",")
    
    
    # # lowest performing products
    # lowest_performing = filtered_sales.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    # performing = lowest_performing.idxmin(axis = 0)[0]
    # details_lowest_performing = format(lowest_performing["Order_Demand"].min(), ",")
    
    
    # return [returned], [purchased], [performing], [details_most_returned], [details_most_purchased], [details_lowest_performing]