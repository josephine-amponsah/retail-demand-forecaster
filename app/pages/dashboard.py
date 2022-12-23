import dash
from dash import Dash, html, dcc, Input, Output, callback, State
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
        dbc.Col([
                dbc.Card([
                dbc.Row([
                    html.Div(["Year"]),
                    dcc.Dropdown(
                      options = year_filter,
                      value = year_filter[-2],
                      id = "date-year-filter"
                  ),
                dbc.Row([
            dbc.Row([
                  dcc.Dropdown(
                      options = year_filter,
                      value = year_filter[-2],
                      id = "date-time-filter"
                  ),
                  ]),
            dbc.Row([
                  dcc.Dropdown(
                      options = category_filter,
                      value = category_filter[-1],
                      id = "category-filter"
                  ),
                  ])
        ], justify="end"),
                    # dcc.Input()
                    
                    ]),
                dbc.Row([])
            ], className = "filter-card")
            
            
            ], width= 2),
        dbc.Col([
            
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Total Demand"), 
                    html.Div( [],
                        id = "sales",className='value',),
                    html.Div("Products")
                    ], className='summary-cards',outline= True, color = "light")
                    ], width=3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Total Returns"), 
                    html.Div([], className='value', id ="returns"),
                    html.Div("Products")
                    ], className='summary-cards',outline= True, color = "light")
                    ], width = 3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Net Demand"), 
                    html.Div([], className='value', id = "warehouse"),
                    html.Div("Products")
                    ], className='summary-cards',outline= True, color = "light"),
                    ], width = 3)
                ,
                dbc.Col([
                    dbc.Card(
                children=[
                    html.Div("Highest Grossing Category"), 
                    html.Div([], className='value', id = "category"),
                    html.Div("Category")
                    ], className='summary-cards',outline= True, color = "light"),
                ]
                    , width = 3)
                
                # 
        
            
        ]),
                html.Br(),
                
                dbc.Row([
                    dbc.Card([
                        dcc.Graph(
                            figure = {
                            "data" : [],
                            # "layout":{
                            #     "title" :"Demand Trend", 
                            #     "margin":{"t": 20, "b": 20, "l": 15, "r":15},
                            #     # "width" : 1000,
                            #     # "height": 150
                                
                            # },

                            },
                            id="sales-over-time", className = "graph-style")
                    ], className = "graph-card",outline= True, color = "light"),
                ],),
                html.Br(),
                dbc.Row([
                    dbc.Card([
                        dcc.Graph(
                            figure = {
                            "data" : [],
                            "layout":{
                                "margin":{"t": 20, "b": 20, "l": 15, "r":15}
                            }
                            },
                            id="categorical-table", className = "graph-style")
                    ], className = "graph-card",outline= True, color = "light")
                ])
            ], width= 9),
            dbc.Col([
                dbc.Card(children=[
                        dbc.Row([
                            html.Div("Highlights", className = "highlight-title"),
                        ]),
                        html.Br(),
                        dbc.Row([
                            html.Div("Most Returned Product", className = "sub-title"),
                            html.Div([], id = "main-returned", className = "sub-title-main"),
                            html.Div([], id = "details-returned")
                        ], className = "side-card-row"),
                        html.Br(),
                        dbc.Row([
                            html.Div("Highest Purchased", className = "sub-title"),
                            html.Div([], id = "main-purchased", className = "sub-title-main"),
                            html.Div([], id = "details-purchased")
                        ], className = "side-card-row"),
                        html.Br(),
                        dbc.Row([
                            html.Div("Lowest Demanded Product", className = "sub-title"),
                            html.Div([], id = "main-lowest", className = "sub-title-main"),
                            html.Div([], id = "details-lowest")
                            
                        ] , className = "side-card-row")
                        
                        
                        
                        ], className = "side-card",outline= True, color = "light")
                    
            ], width= 3)
        ], justify = "between"),
        
            ]),
        
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
    [Output("sales-over-time", "figure")],
    Input("date-time-filter", "value"),
    Input("category-filter", "value"),
)

def salesTrend(date, category):
    masks = (sales.year == date) & (sales.Product_Category == category)
    filtered_data = sales.loc[masks, :]
    filtered_data = filtered_data.fillna(0)
    
    fig_data = filtered_data.groupby("month_year")["Order_Demand"].sum().to_frame().reset_index()
    sales_trend_figure = {
        "data": [
            {
                "x": fig_data["month_year"],
                "y": fig_data["Order_Demand"],
                "type": "bar",
                "marker": {
           "color": "602BF8",
           "radius": 15
        #    'border-radius':'15px'
       }
                # "hovertemplate": "%{y:.2f}<extra></extra>",
            },
            ],
        "layout":{
                    "margin":{"t": 30, "b": 30, "l": 35, "r":25},
                    # "borderRadius": '15px',
                },
       
        
    }
    return [sales_trend_figure]

@callback(
    [Output("main-returned", "children"), Output("main-purchased", "children"), Output("main-lowest", "children"), 
     Output("details-returned", "children"), Output("details-purchased", "children"), Output("details-lowest", "children")],
    Input("date-year-filter", "value")
)

def highlights(year):
    mask1 = sales.year == year
    mask2 = returns.year == year
    filtered_sales = sales.loc[mask1,:]
    filtered_returns = returns.loc[mask2,:]
    
    # most returned product
    most_returned = filtered_returns.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    returned = most_returned.idxmax(axis = 0)[0]
    details_most_returned =format(most_returned["Order_Demand"].max(), ",")
    
    # most purchased products
    
    most_purchased = filtered_sales.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    purchased = most_purchased.idxmax(axis = 0)[0]
    details_most_purchased = format(most_purchased["Order_Demand"].max(), ",")
    
    
    # lowest performing products
    lowest_performing = filtered_sales.groupby("Product_Code")["Order_Demand"].sum().to_frame()
    performing = lowest_performing.idxmin(axis = 0)[0]
    details_lowest_performing = format(lowest_performing["Order_Demand"].min(), ",")
    
    
    return [returned], [purchased], [performing], [details_most_returned], [details_most_purchased], [details_lowest_performing]