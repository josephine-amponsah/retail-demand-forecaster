
import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = px.data.tips()
dash.register_page(__name__, path = '/testing')

layout = dbc.Container(
    [
        dcc.Dropdown(
            id="values",
            value="total_bill",
            options=[{"value": x, "label": x} for x in ["total_bill", "tip", "size"]],
            clearable=False,
        ),
        dcc.Graph(id="pie-chart"),
    ],
    fluid=True,
    className="dbc",
)


@callback(Output("pie-chart", "figure"), Input("values", "value"))
def generate_chart(value):
    fig = px.bar(df, y=value, x="day", template="cyborg")
    
    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)',
        margin={'l':0, 'r':0, 'b':0},
        font_color='white',
        font_size=18,
        hoverlabel={'bgcolor':'white', 'font_size':16, }
    )
    fig.update_traces(
        # marker_bgcolor="#93c"
        marker = {
            'color': '#93c',
        }
        )
    return fig