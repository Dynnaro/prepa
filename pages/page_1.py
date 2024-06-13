import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State, callback


dash.register_page(__name__, order=3)

layout = html.Div([
    html.H1('This is our first page'),
])