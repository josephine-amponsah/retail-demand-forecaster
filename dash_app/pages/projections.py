import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table
import json
from sktime.forecasting.base import ForecastingHorizon
from modules import forecastingPipeline as forecaster
from datetime import datetime
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path = '/projections')

targets = ["Orders", "Returns", "Revenue"]


summary_table = pd.DataFrame.from_dict({
    "warehouse":[], "orders":[], "returns":[], "net_sales":[], "yoy_growth":[]
})

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']


layout = html.Div([
    dcc.Store(id = "filtered-data"),
    dcc.Store(id = "projected-data"),
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Forecaster", className="card-title"),
                        dbc.Row([
                            
                        ]),
                        html.Div([
                                dcc.DatePickerRange(
                                    # style={"width": "100%"},
                                    start_date = "2022-01-01",
                                    min_date_allowed = "2022-01-02",
                                    display_format = "DD MMM YYYY",
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
                        dcc.Dropdown(placeholder = "Target", options = targets, className="year-dropdown dbc .Select-control", id = "targets"),
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
                ], className= "card bg-light mb-3", id="whse-projection"
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
                        
                        dbc.Table(id = "predicted-table")
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
    data = pd.DataFrame(json.loads(data))
    options = data["Warehouse"]
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
    # Input("sales-store", "data"),
    Input("model-run", "n_clicks")
)
def date_picker(start, end, whse, cat, target, click):
    periods = 0
    fh = 0
    start_date = start
    end_date = end
    if click is None:
        raise PreventUpdate
        # data = pd.DataFrame()
        # data = data.to_json(date_format='iso') 
    else:
        # start_date = pd.Timestamp(start_date)
        # end_date = pd.Timestamp(end_date)
        # start_date = pd.Period(start_date, freq ="M")
        # end_date = end_date.to_period("M")
        # # months = (start_date - end_date) + 1
        fh = ForecastingHorizon(
            pd.PeriodIndex(pd.date_range("2023-01", periods= 2, freq="M")), is_relative=False
        )
        pred = forecaster.forecast(fh)
        data = pred.to_json(date_format='iso')
    return data


@callback(
    Output("projected-demand-chart", "figure"),
    # Input("date-time-filter", "value"),
    Input("projected-data", "data")
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
    Output("predicted-table", "children"),
    Input("projected-data", "data")
)
def data_table(data):
    data = pd.DataFrame(json.loads(data))
    # data = data[(data["year"] == date )& (data["Warehouse"] == whse)]
    # table = data[["Warehouse","Product_Category", "month_year","Order_Demand"]]
    # table = table.groupby(["Warehouse","Product_Category", "month_year"], as_index = False).agg(
    #     Demand = pd.NamedAgg(column = "Order_Demand", aggfunc = sum),
    #     # Returns = pd.NamedAgg(column = "Returns", aggfunc = sum)
    #)
    df = dbc.Table.from_dataframe(data, striped=True, bordered=True, hover=True, index=True, responsive = True)
    return df

# @callback(
#     Output("whse-projection", "children"),
#     State("targets", "value"),
#     Input("projected-data", "data")
# )
# def whse_projections(data, value):
#     data = pd.DataFrame(json.loads(data))
#     df = data[["Warehouse", value]]
#     df = data.groupby(["Warehouse"], as_index= false)["Order_Demand"].sum()
#     return df
