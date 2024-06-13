import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State

app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.BOOTSTRAP] ,include_assets_files=True)
server = app.server

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
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Home", href="/")),
                    dbc.NavItem(dbc.NavLink("About", href="/about")),

                    
                    ]),
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

sidebar = html.Div(
    [
        dbc.Button("=",  outline=True, color="secondary", className="me-1", id="open-offcanvas", n_clicks=0 ),
        dbc.Offcanvas(
            [
                html.Br(),
                html.Br(),
                html.P(
                    "This is the content of the Offcanvas. "
                    "Close it by clicking on the close button, or "
                    "the backdrop."
                ),
                
                html.A("Tunis", href="#tunis"),
                html.Br(),
                html.A("Bizert", href="#bizert")
            
            
            ],
            
            id="offcanvas",
            title="Title",
            is_open=False,
        ),
    ],

    style={"top":"0",
           "position":"sticky" , "z-index":"122222", "width":"10    0%"}
   
)






content = html.Div([dash.page_container], className="h-100" )

app.layout = html.Div([dcc.Location(id="url"),navbar, sidebar ,content] )

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



@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open  
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