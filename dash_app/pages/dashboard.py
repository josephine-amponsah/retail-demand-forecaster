import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
from dash import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import sys
import json
import numerize
from numerize import numerize

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
    "categories":["X"], "orders":[10], "returns":[1], "net_sales":[9], "month_on_month":[2.5]
})

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']

layout = html.Div([
    dcc.Store(id = "sales-data"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown( placeholder = 'Year', id = 'date-time-filter',
                 className="dbc year-dropdown .Select-control", value = 2021) 
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
                                        html.H5(className="card-title", id = "sum-of-orders"),
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
                                        html.H5( className="card-title", id = "sum-of-returns"),
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
                                        dbc.Col(["Name"], id ="highest-cat-name", className = "border-right", width =6),
                                        dbc.Col(["Orders"], id ="highest-cat-orders",  width =6),
                                        # dbc.Col(["Revenue"], id ="highest-cat-revenue", width =4),
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
                                    dbc.Col(["Name"], id ="most-purchased-name", className = "border-right", width =6),
                                    dbc.Col(["Orders"], id ="most-purchased-orders", width =6),
                                    # dbc.Col(["Revenue"], id ="most-purchased-revenue", width =4),
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
                                        dbc.Col(["Name"], id ="least-purchased-name", className = "border-right", width =6),
                                        dbc.Col(["Orders"], id ="least-purchased-orders", width =6),
                                        # dbc.Col(["Revenue"], id ="least-purchased-revenue", width =4),
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
                                        dbc.Col(["Name"], id ="most-returned-name", className = "border-right", width =6),
                                        dbc.Col(["Orders"], id ="most-returned-orders", width =6),
                                        # dbc.Col(["Revenue"], id ="most-returned-revenue", width =4),
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
                        html.H6("Top 10 Categories", className="card-title"),
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
                                    dcc.Dropdown( placeholder = 'Warehouse', id = 'table-warehouse-filter',
                                        className="dbc year-dropdown .Select-control") 
                                ], width=8),
                                dbc.Col([
                                    html.Button( 'Filter', id = 'table-filter',
                                        className="btn btn-info") 
                                ], width = 4),
                            ])
                            
                        ], width=6)
                        
                    ], justify= "between", className="details-table-nav"),
                    
                    dbc.Table.from_dataframe(summary_table, striped=True, bordered=True, hover=True, index=True, id= "data-table")
                ], className= "card bg-light mb-3 details-table-section second-section"
            ), width=8
        , ),
    ],  )


])

# @callback(Output('sales-data', 'cdata'))
# def store_sales_data():  # sourcery skip: inline-immediately-returned-variable
    
#     return sales_data.reset_index().to_json(orient="split")
#year dropdown options
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
    data = data[data["year"] == year]
    total_orders = data["Order_Demand"].sum()
    total_orders = numerize.numerize(total_orders)
    return [total_orders]


@callback(
    [Output("highest-cat-name", "children"), Output("highest-cat-orders", "children")], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == year]
    high_cat = data[["Product_Category", "Order_Demand"]]
    high_cat = high_cat.groupby(["Product_Category"]).sum("Order_Demand")
    high_cat_name= high_cat.idxmax()
    high_cat_orders = numerize.numerize(high_cat["Order_Demand"].max())
    return [high_cat_name, high_cat_orders]

@callback(
    [Output("most-purchased-name", "children"), Output("most-purchased-orders", "children")], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == year]
    most_purchased = data[["Product_Code", "Order_Demand"]]
    most_purchased = most_purchased.groupby(["Product_Code"]).sum("Order_Demand")
    most_purchased_name= most_purchased.idxmax()
    most_purchased_orders = numerize.numerize(most_purchased["Order_Demand"].max())
    return [most_purchased_name, most_purchased_orders]

@callback(
    [Output("least-purchased-name", "children"), Output("least-purchased-orders", "children")], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == year]
    least_purchased = data[["Product_Code", "Order_Demand"]]
    least_purchased = least_purchased.groupby(["Product_Code"]).sum("Order_Demand")
    least_purchased_name= least_purchased.idxmin()
    least_purchased_orders = numerize.numerize(least_purchased["Order_Demand"].min())
    return [least_purchased_name, least_purchased_orders]

@callback(
    [Output("most-returned-name", "children"), Output("most-returned-orders", "children")], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == year]
    most_returned = data[["Product_Code", "Returns"]]
    most_returned = most_returned.groupby(["Product_Code"]).sum("Returns")
    most_returned_name= most_returned.idxmax()
    most_returned_orders = numerize.numerize(most_returned["Returns"].max())
    return [most_returned_name, most_returned_orders]

@callback(
    [Output("sum-of-returns", "children"), ], 
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)
def date_summary(year, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == year]
    total_returns = data["Returns"].sum()
    total_returns = numerize.numerize(total_returns)
    return [total_returns]

@callback(
    Output("monthly-sales-chart", "figure"),
    Input("date-time-filter", "value"),
    Input("sales-store", "data")
)

def salesTrend(date, data):
    plot_data = pd.DataFrame(json.loads(data))
    plot_data = plot_data[plot_data["year"] == date]
    plot_data = plot_data.groupby(["month_year", "month"]).sum("Order_Demand")
    plot_data = pd.DataFrame(plot_data).reset_index()
    fig = px.histogram(plot_data, y="Order_Demand", x="month", template="cyborg",  histfunc='sum', 
                       labels = {'Order_Demand':'Orders', "month": "Month"})
    
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
    Input("sales-store", "data")
)
def gauge(value, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == value]
    gauge_data = data[["Warehouse", "Order_Demand"]]
    gauge_data = gauge_data.groupby(["Warehouse"]).sum("Order_Demand").reset_index()
    
    # labels = ["NET-DEMAND", "RETURNS"]
    # values = [4500, 2500]

# Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels= gauge_data["Warehouse"].apply(str.upper), values= gauge_data["Order_Demand"] , hole=.7)])
    
    fig.update_traces(
        marker_colors= ["#93c", "#f80"]
    )
    
    fig.update_layout(
        margin={'l':20, 'r':20, 'b':0, 't':0},
        height = 200
    )
    return fig
    
@callback(
    Output("data-table", "data"),
    Input("date-time-filter", "value"),
    Input('table-warehouse-filter', "value2"),
    Input("sales-store", "data")
)
def data_table(value,value2, data):
    data = pd.DataFrame(json.loads(data))
    data = data[data["year"] == value & data["Warehouse"] == value2]
    table = data[["Product_Category", "Order_Demand", "Returns"]]
    table = table.groupby("Product_Category")["Order_Demand", "Returns"].sum().reset_index()
    table["Net_Sales"] = table["Order_Demand"] - table["Returns"]
    table["Month-on-month %"] = table["Net_Sales"].pct_change(axis = 'rows')
    table = table.rename(columns = {"Product_Category": "Category", "Order_Demand": "Demand"})
    return table