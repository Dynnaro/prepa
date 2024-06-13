import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State, callback
import plotly.express as px
import pandas as pd
import dash_leaflet as dl

dash.register_page(__name__, order=1, path="/")


df = pd.read_csv('/Users/mak/Desktop/Code_With_Me/project/c.csv')
Ctx=dash.callback_context



CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'height':'100vh',
}



content = html.Div(
    
    [
        html.H1('hello world'),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        dl.Map(dl.TileLayer(), center=[56,10], zoom=6, style={'height': '70vh'})
        
    ],
    
    style=CONTENT_STYLE
    
    
    
    
    
    )




# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position":"absolute",
    "height": "100rem",
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P('Coming soon!'),

    ],
    style=SIDEBAR_STYLE,
)





layout = html.Div([
    sidebar,
    content,

])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')
