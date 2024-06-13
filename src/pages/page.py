import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State, callback
import plotly.express as px
import pandas as pd
import dash_leaflet as dl



dash.register_page(__name__, order=1, path="/page")


layout = html.Div([
    html.H1("Statistics"),

])