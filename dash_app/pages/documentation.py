
import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table
# df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path='/testing')

layout = dbc.Container([
    html.Section([
        html.H4('Table of content'),
        html.Ol([
            html.Li([html.A("Introduction", href="#introduction")]),
            html.Li([html.A("Installation and Requirements", href="#install")]),
            html.Li([html.A("User Guide", href="#guide")]),
            html.Li([html.A("Machine Learning Model", href="#model")]),
            html.Li([html.A("Technical Documentation", href="#technical")]),
            html.Li([html.A("Future Development", href="#future")]),
            html.Li([html.A("Conclusion", href="#conclusion")]),
        ]),
    ]),
    html.Br(),
    html.Section([
        html.H4("Introduction"),
        html.P("Welcome to the documentation for our Dash application! Our application is designed to help"
        " businesses gain insights into demand and returns for various products and warehouses, as well as "
        "make projections for future demand using a hierarchical forecasting model."),
        html.P("The application consists of two main pages: the dashboard and projections page. On the "
        "dashboard page, users can view insights on demand and returns for various products and under their "
        "categories for a number of warehouses. On the projections page, users can make demand projections "
        "for a specified period of time using a hierarchical forecasting model."),
        html.P("Our application is built using Dash, a Python framework for building web applications. We've "
        "also utilized several other Python libraries, including Pandas and Sktime, to implement the forecasting model."),
    ], id="introduction"),
    html.Br(),
    html.Section([
        html.H4("Installation and Requirements"),
        html.H5("Running the App Locally"),
        html.P("To run the app locally, follow these steps:"),
        html.Li([
            html.Span("Clone the repository from GitHub: ", style={'fontWeight': 'bold'}),
            html.Span("git clone https://github.com/your-username/your-app.git")
        ]),
        html.Li([
            html.Span("Navigate to the root directory of the app: ", style={'fontWeight': 'bold'}),
            html.Span("cd your-app")
        ]),
        html.Li([
            html.Span("install the necessary dependencies: ", style={'fontWeight': 'bold'}),
            html.Span("pip install -r requirements.txt")
        ]),
        html.Li([
            html.Span("Run the app: ", style={'fontWeight': 'bold'}),
            html.Span("python app.py")
        ]),
        html.Li([
            html.Span("", style={'fontWeight': 'bold'}),
            html.Span("Open your web browser and navigate to http://localhost:port-number")
        ]),
        html.P("You should now see the app running locally on your machine."
        "These instructions assume that you have Python and pip installed on "
        "your machine. If you don't have these installed, please refer to the Python "
        "documentation for installation instructions.")
    ], id="install"),
    html.Br(),
    html.Section([
        html.H4("User Guide"),
        html.P("The app, as previously stated, consists of two main pages: dashboard and projections. "
        "The dashboard displays insights on demand and returns for various products and under their "
        "categories for a number of warehouses. The projections page runs on a hierarchical forecasting model, "
        "that predicts the demand of products for a period specified by the user."),
        html.H5("Dashboard Page"),
        html.P("The dashboard page displays insights on demand and returns for various products and under "
        "their categories for a number of warehouses. Here's a breakdown of the different sections of the page:"),
        html.Li([
            html.Span("Filters", style={'fontWeight': 'bold'}),
            html.Span("Use the filters at the top of the page to select the year for which you wish to view the insights."
            "The filter on the data table is used to select the warehouse, whose data you wish to observe or retrieve")
        ]),
        html.Li([
            html.Span("Demand chart", style={'fontWeight': 'bold'}),
            html.Span("The demand chart displays the total demand for products in the specified year over monthly periods.")
        ]),

        html.Li([
                html.Span("Summary cards", style={'fontWeight': 'bold'}),
                html.Span("")
        ]),
        html.Li([
                html.Span("Stats cards", style={'fontWeight': 'bold'}),
                html.Span("This covers the highlights and top 10 categories card. These features provide insights on best and least"
                " performing products and/or categories for the specified year")
        ]),
        html.Li([
                html.Span("", style={'fontWeight': 'bold'}),
                html.Span("")
        ]),
        
        html.H5("Projections Page"),
        html.P(),
        html.Li([
            html.Span("Demand chart", style={'fontWeight': 'bold'}),
            html.Span("The demand chart displays the demand for the selected product or category over time, broken down by warehouse.")
        ]),


    ], id="guide"),
    html.Br(),
    html.Section([
        html.H4("Machine Learning Model"),
        html.P(),
        html.H5("Model Overview"),
        html.P(),
        html.H5("Base Estimators"),
        html.P(),
        html.Li([
            html.Span("", style={'fontWeight': 'bold'}),
            html.Span("")
        ]),
        html.I(),
        html.H5("Performance Evaluation"),
        html.P(),
        html.P(),
    ], id="model"),
    html.Br(),
    html.Section([
        html.H4("Technical Documentation"),
        html.H5("Architecture Overview"),
        html.P(),
        html.Ol([
            html.Li([
                html.Span("", style={'fontWeight': 'bold'}),
                html.Span("")
            ]),
        ]),
        html.H5("Architecture Components"),
        html.P(),
        html.Ol([
            html.Li([
                html.Span("", style={'fontWeight': 'bold'}),
                html.Span("")
            ]),
        ]),
        html.P(),

    ], id="techincal"),
    html.Section([
        html.H4("Future Developments"),
        html.H5("Accounting for error margins"),
        html.P(),
        html.H5("Downloading data"),
        html.P(),
        html.H5("Addition target variables"),
        html.P()
    ], id="future"),
    html.Section([
        html.H4("Conclusion"),
        html.P()
    ], id="conclusion")



])
