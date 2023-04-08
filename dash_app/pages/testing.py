
import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dash_table
# df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path = '/testing')

layout = dbc.Container([
    html.Div('Test'),
    # dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    # dbc.Alert(id='tbl_out'),
])

# @callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
# def update_graphs(active_cell):
#     return str(active_cell) if active_cell else "Click the table"

# df = px.data.tips()


# layout = dbc.Container(
#     [
#         dcc.Dropdown(
#             id="values",
#             value="total_bill",
#             options=[{"value": x, "label": x} for x in ["total_bill", "tip", "size"]],
#             clearable=False,
#         ),
#         dbc.Card([
#             dcc.Graph(id="pie-chart", figure={}),
#         ],)
        
#     ],
#     fluid=True,
#     className="dbc",
    
# )


# @callback(
#     Output("pie-chart", "figure"), 
#     Input("values", "value")
#     )
# def generate_chart(value):
#     data = df[["day", value]]
#     fig = px.histogram(data, y=value, x="day", template="cyborg",  histfunc='sum')
    
#     fig.update_layout(
#         paper_bgcolor = 'rgba(0,0,0,0)',
#         # margin={'l':0, 'r':0, 'b':0},
#         font_color='white',
#         font_size=18,
#         hoverlabel={'bgcolor':'white', 'font_size':16, }
#     )
#     fig.update_traces(
#         # marker_bgcolor="#93c"
#         marker = {
#             'color': '#93c',
#         }
#         )
#     return fig