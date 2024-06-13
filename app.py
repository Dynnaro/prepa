import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State

app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title="Prepa Insights"

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    
        [ 
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                        
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Nav([dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))for page in dash.page_registry.values()]),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
    color="dark",
    dark=True,
    className="d-flex justify-content-evenly align-items-center p-3"
)







# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position":"absolute",
    "height": "100vh",
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
               
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([dash.page_container], className="h-100" )

app.layout = html.Div([dcc.Location(id="url"),navbar , content] )

'''
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.Div(html.H1("Oh cool, this is page 2!", style={"color":"blue"}))

'''


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(port=8888)