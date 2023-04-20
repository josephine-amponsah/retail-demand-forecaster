
import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table
# df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path='/documentation')

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
            # html.Li([html.A("Conclusion", href="#conclusion")]),
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
            html.Span("Clone the repository from GitHub: ",
                      style={'fontWeight': 'bold'}),
            html.Span("git clone https://github.com/your-username/your-app.git")
        ]),
        html.Li([
            html.Span("Navigate to the root directory of the app: ",
                      style={'fontWeight': 'bold'}),
            html.Span("cd your-app")
        ]),
        html.Li([
            html.Span("install the necessary dependencies: ",
                      style={'fontWeight': 'bold'}),
            html.Span("pip install -r requirements.txt")
        ]),
        html.Li([
            html.Span("Run the app: ", style={'fontWeight': 'bold'}),
            html.Span("python app.py")
        ]),
        html.Li([
            html.Span("", style={'fontWeight': 'bold'}),
            html.Span(
                "Open your web browser and navigate to http://localhost:port-number")
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
                      "The filter on the data table is used to select the warehouse, whose data you wish to observe or retrieve.")
        ]),
        html.Li([
            html.Span("Demand Charts", style={'fontWeight': 'bold'}),
            html.Span("The bar chart displays the total demand for products in the specified year over monthly periods. the guage"
                      "chart displays the same parameter, but as the constitution of each warehouse's total demand by percentage.")
        ]),

        html.Li([
            html.Span("Summary cards", style={'fontWeight': 'bold'}),
            html.Span(
                "These cards display summary statistics on the determined KPI's; demand, returns and net sales.")
        ]),
        html.Li([
            html.Span("Stats cards", style={'fontWeight': 'bold'}),
            html.Span("This covers the highlights and top 10 categories card. These features provide insights on best and least"
                      " performing products and/or categories for the specified year")
        ]),
        html.Li([
            html.Span("Data Table", style={'fontWeight': 'bold'}),
            html.Span(
                "With this table, you can view the detailed data on the demand and product returns and extract same.")
        ]),

        html.H5("Projections Page"),
        html.P(),
        html.Li([
            html.Span("Forecaster settings", style={'fontWeight': 'bold'}),
            html.Span("For determining the forecast settings for the warehouse and/or category you want to forecast, including the forecast period, and the target.")
        ]),
        html.Li([
            html.Span("Projection chart", style={'fontWeight': 'bold'}),
            html.Span(
                "The output of the forecast model is displayed a barchart in this feature.")
        ]),
        html.Li([
            html.Span("Data table", style={'fontWeight': 'bold'}),
            html.Span("This provides detailed data of the output of the model.")
        ]),
        html.Li([
            html.Span("Stats card", style={'fontWeight': 'bold'}),
            html.Span(
                "On this feature, the output of the model is grouped and ranked by category and target variable and the top 10 are displayed.")
        ]),
    ], id="guide"),
    html.Br(),
    html.Section([
        html.H4("Machine Learning Model"),
        html.P("The projections page uses a hierarchical forecasting model to predict demand for various products and warehouses "
               "at different levels of the hierarchy. The model is an EnsembleForecaster, which is a meta-estimator that combines "
               "the predictions of multiple base estimators. The base estimators used in the model are NaiveForecaster and PolynomialTrendForecaster."),
        html.H5("Model Overview"),
        html.P("The hierarchical forecasting model is based on the idea that demand for products at different levels of the hierarchy (such "
               "as product, category, and warehouse) is related and can be used to improve forecast accuracy. The model uses a top-down approach"
               " to generate forecasts, starting from the highest level of the hierarchy (such as total demand for all products and warehouses) "
               "and then disaggregating the forecast to lower levels of the hierarchy (such as demand for individual products and warehouses)."),
        html.P("The model is implemented using the EnsembleForecaster class from the sktime.forecasting.compose module in the Scikit-Time library. "
               "The model is trained on historical demand data for various products and warehouses, using a rolling window approach to simulate "
               "real-time forecasting. The model's performance is evaluated using the R2 score, which is a measure of how well the model fits the data."),
        html.H5("Base Estimators"),
        html.P("The EnsembleForecaster combines the predictions of two base estimators: NaiveForecaster and PolynomialTrendForecaster."),
        html.Li([
            html.Span("Naive Forecaster", style={'fontWeight': 'bold'}),
            html.Span("The NaiveForecaster is a simple forecasting strategy that uses the most recent observation as the forecast for the next period. "
                      "The NaiveForecaster is used as a baseline estimator to compare the performance of the hierarchical forecasting model against a simple forecasting strategy.")
        ]), html.Li([
            html.Span("Polynomial Trend Forecaster",
                      style={'fontWeight': 'bold'}),
            html.Span("The PolynomialTrendForecaster is a regression-based forecasting strategy that fits a polynomial trend to the historical data and extrapolates the trend to "
                      "make future predictions. The PolynomialTrendForecaster is used as a more sophisticated estimator that can capture trends and seasonality in the data.")
        ]),
        html.I(),
        html.H5("Performance Evaluation"),
        html.P("The hierarchical forecasting model achieved an R2 score of 0.8164 on the test set, indicating that the model explains 81.64 percent of the variability in the data. "),
        html.P("The hierarchical forecasting model used in our projections page is a powerful tool for predicting demand for various products and warehouses at different levels of "
               "the hierarchy. The model combines the predictions of multiple base estimators to generate accurate forecasts that can be used to inform business decisions."),
    ], id="model"),
    html.Br(),
    html.Section([
        html.H4("Technical Documentation"),
        html.H5("Architecture Overview"),
        html.P("Here's a high-level overview of the app's architecture:"),
        html.Ol([
            html.Li([
                html.Span("Data Source: ", style={'fontWeight': 'bold'}),
                html.Span("The original data was retrieved from kaggle , cleaned and feature engineered tom meet the objectives of the project. The app data is served from a github repo as a form of an API.")
            ]),
            html.Li([
                html.Span("Data Processing", style={'fontWeight': 'bold'}),
                html.Span(
                    "The app processes the data to generate insights and forecasts, using various Python libraries such as Pandas and Numpy.")
            ]),
            html.Li([
                html.Span("Data Visualization", style={'fontWeight': 'bold'}),
                html.Span(
                    "The application displays the insights generated from the processed data using Dash core components and Plotly.")
            ]),
            html.Li([
                html.Span("Forecasting", style={'fontWeight': 'bold'}),
                html.Span("The projections page runs a hierarchical forecasting model using the sktime library and displays the forecast results using Dash core components and Plotly.")
            ]),
            html.Li([
                html.Span("User Interface", style={'fontWeight': 'bold'}),
                html.Span(
                    "The app's user interface is built using Dash core components, HTML, CSS using cyborg theme from dash bootstrap components.")
            ]),
        ]),
        html.H5("Libraries / Components"),
        html.P(),
        html.Ol([
            html.Li([
                html.Span("Pandas: ", style={'fontWeight': 'bold'}),
                html.Span("The Pandas library is used to manipulate and preprocess the data, including cleaning and filtering the data, and aggregating "
                          "the data by various dimensions such as product, category, and warehouse.")
            ]),
            html.Li([
                html.Span("Numpy: ", style={'fontWeight': 'bold'}),
                html.Span("The NumPy library is used to perform numerical operations on the data, including calculating various metrics such as "
                          "average demand, return rate, and revenue.")
            ]),
            html.Li([
                html.Span("Dash: ", style={'fontWeight': 'bold'}),
                html.Span("Dash core components are used to build various UI elements on the page, including dropdowns, charts, and tables, while the dash HTML components "
                          "borrow the functionality of basic HTML to construct HTML elements.")
            ]),
            html.Li([
                html.Span("Plotly: ", style={'fontWeight': 'bold'}),
                html.Span(
                    "Plotly is used to build the interactive charts displayed on the page, including line charts and stacked bar charts.")
            ]),
            html.Li([
                html.Span("Sktime: ", style={'fontWeight': 'bold'}),
                html.Span("This is a forecasting library, built on machine learning estimators from scikit learn. In this application, it was used to build a hierarchical forecasting "
                          "model that can forecast demand for various products and warehouses at different levels of the hierarchy.")
            ]),
        ]),
        html.H5("Achitecture Design"),
        html.I(),

    ], id="techincal"),
    html.Section([
        html.H4("Future Developments"),
        html.H5("Accounting for error margins"),
        html.P("In the next version of the app, one of the new features will be to account for the error margins in the model output. Currently, the projections "
               "page uses a hierarchical forecasting model to predict demand for various products and warehouses. While the model "
               "has shown good performance on test data, there is always some degree of uncertainty in the forecasts. In future development, "
               "error margins will be incorporated into the model output and provide users with more information on the reliability of the forecasts."),
        html.H5("Downloading data"),
        html.P("Currently, users can view insights on demand and returns for various products and warehouses on the dashboard page, as well as make "
               "demand projections on the projections page. In future development, a feature that allows users to download the data displayed on these pages as CSV files will be added."),
        html.H5("Addition target variables"),
        html.P("In addition to forecasting demand, it is intended that other target variables will be added as input parameters to the hierarchical forecasting model."
               "Specifically, we plan to include forecasts for returns and revenue in future development. This will provide users with a more comprehensive view of their"
               "business performance and allow them to make more informed decisions.")
    ], id="future"),
    # html.Section([
    #     html.H4("Conclusion"),
    #     html.P()
    # ], id="conclusion")



])
