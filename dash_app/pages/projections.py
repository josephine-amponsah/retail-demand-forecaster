import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table
import json

# app = Dash(__name__)
dash.register_page(__name__, path = '/projections')
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
sales = pd.read_csv("../data/sales.csv")
returns = pd.read_csv("../data/returns.csv")
targets = ["Orders", "Returns", "Revenue"]

year_filter =  sales["year"].unique().tolist()
year_options = year_filter.sort() 
category_filter = sales["Product_Category"].unique().tolist()
summary_table = pd.DataFrame.from_dict({
    "warehouse":[], "orders":[], "returns":[], "net_sales":[], "yoy_growth":[]
})

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']


layout = html.Div([
    dcc.Store(id = "sales-data"),
    dcc.Store(id = "projected-data"),
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Forecaster", className="card-title"),
                        dbc.Row([
                            
                            # dbc.Col([dbc.Input(className="year-dropdown")], width = 4)
                        ]),
                        html.Div([
                                dcc.DatePickerRange(
                                    # style={"width": "100%"},
                                    # start_date = "2022-01",
                                    min_date_allowed = "2022-01-02",
                                    display_format = "MMM YYYY",
                                    start_date_placeholder_text="Start Date",
                                    end_date_placeholder_text="End Date",
                                    calendar_orientation = 'vertical',
                                    className = "dbc ",
                                    id = "date-picker",
                                )
                            ], className = "dbc date-picker-box Input-styling"),
                        html.Br(),
                        html.Div("Warehouses"),
                        dcc.Dropdown( placeholder = 'Warehouse', id = 'whse-selection', className="dbc year-dropdown .Select-control") ,
                        html.Br(),
                        html.Div("Categories"),
                        dcc.Dropdown( placeholder = 'Year', id = 'cat-selection', className="dbc year-dropdown .Select-control"),
                        html.Br(),
                        html.Div("Target"),
                        dcc.Dropdown(placeholder = "Target", options = targets, className="year-dropdown dbc .Select-control"),
                        html.Br(),
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                html.Button( 'Run', id = 'model-run',
                                    className="btn btn-info") 
                                ], width = 4),
                            ], justify = 'center')
                        ])
                        
                    ], className="card-body")
                ], className= "card border-light mb-3"
            ), width=4
        ),
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Projected Demand", className="card-title"),
                        dcc.Graph( id = "projected-demand-chart")
                    ], className="card-body")
                ], className= "card bg-light mb-3"
            ), width=8
        ),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Warehouses", className="card-title"),
                        
                    ], className="card-body")
                ], className= "card bg-light mb-3"
            ), width=4
        ),
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        dbc.Row([
                            dbc.Col([html.H6("Projected Data", className="card-title")], width=10),
                            dbc.Col([
                                html.Button( 'Download', id = '',
                                    className="btn btn-info") 
                                ], width = 2),
                        ], justify= 'end', className = "details-table-nav"),
                        
                        dbc.Table.from_dataframe(summary_table, striped=True, bordered=True, hover=True, index=True)
                    ], className="card-body")
                ], className= "card bg-light mb-3"
            ), width=8
        ),
    ])


])


@callback(
    Output("whse-selection", "options"),
    Input("sales-store", "data")
)
def filter_options(data):
    # sourcery skip: inline-immediately-returned-variable
    sales_data = pd.DataFrame(json.loads(data))
    options = sales_data["Warehouse"]
    options = options.unique()
    return options

@callback(
    Output("cat-selection", "options"),
    Input("sales-store", "data")
)
def filter_options(data):
    # sourcery skip: inline-immediately-returned-variable
    sales_data = pd.DataFrame(json.loads(data))
    options = sales_data["Product_Category"]
    options = options.unique()
    return options


@callback(
    Output("projected-data", "data"),
    State("date-picker", "start_date"),
    State("date-picker", "end_date"),
    State("whse-selection", "value"),
    State("cat-selection", "value"),
    State("targets", "value"),
    Input("sales-store", "data"),
    Input("model-run", "click")
)
def date_picker(start, end, whse, cat, target, data, click):
    if click ==1:
        data = pd.DataFrame(json.loads(data))
        
    
    return data


@callback(
    Output("projected-demand-chart", "figure"),
    # Input("date-time-filter", "value"),
    Input("projection-store", "data")
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