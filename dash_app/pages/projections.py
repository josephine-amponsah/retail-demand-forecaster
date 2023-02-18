import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table

# app = Dash(__name__)
dash.register_page(__name__, path = '/projections')
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
sales = pd.read_csv("../data/sales.csv")
returns = pd.read_csv("../data/returns.csv")


year_filter =  sales["year"].unique().tolist()
year_options = year_filter.sort() 
category_filter = sales["Product_Category"].unique().tolist()
summary_table = pd.DataFrame.from_dict({
    "warehouse":[], "orders":[], "returns":[], "net_sales":[], "yoy_growth":[]
})

revSummary = ['Products Sold', 'Returns', 'Highest Grossing Warehouse',  'Best Performing Category']

layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Forecaster", className="card-title"),
                        dbc.Row([
                            html.Div("Date Range"),
                            dbc.Col([dbc.Input(className="year-dropdown")], width = 4)
                        ]),
                        
                        html.Div("Warehouses"),
                        dcc.Dropdown(className="year-dropdown dbc Select-control"),
                        html.P("Categories"),
                        dcc.Dropdown(className="year-dropdown dbc Select-control"),
                        html.P("forecast target(demand/returns/revenue)"),
                        dcc.Dropdown(className="year-dropdown dbc Select-control"),
                        html.Button(className="btn btn-info")
                    ], className="card-body")
                ], className= "card border-light mb-3"
            ), width=4
        ),
        dbc.Col(
            html.Div(
                [
                    html.Div([
                        html.H6("Projected Demand", className="card-title"),
                        # dcc.Graph( id = "projected-demand-chart")
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


# @callback(
#     Output("projected-demand-chart", "figure"),
#     Input("date-time-filter", "value"),
    
# )

# def salesTrend(date):
#     # masks = (sales.year == date) & (sales.Product_Category == category)
#     # filtered_data = sales.loc[masks, :]
#     # filtered_data = filtered_data.fillna(0)
    
#     # fig_data = filtered_data.groupby("month_year")["Order_Demand"].sum().to_frame().reset_index()
#     data = sales[sales["year"] == date]
#     fig = px.line(data, y="Order_Demand", x="month_year", template="cyborg")
    
#     fig.update_layout(
#         paper_bgcolor = '#222',
#         margin={'l':20, 'r':20, 'b':0},
#         font_color='white',
#         font_size=18,
#         hoverlabel={'bgcolor':'white', 'font_size':16, },
#         bargap=.25
        
#     )
#     fig.update_traces(
#         # marker_bgcolor="#93c"
#         marker = {
#             'color': '#93c',
#         }
#         )
    
#     return fig