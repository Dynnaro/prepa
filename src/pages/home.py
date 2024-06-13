import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State, callback
import plotly.express as px
import pandas as pd
import dash_leaflet as dl

photo = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

dash.register_page(__name__, order=1, path="/" )


#df = pd.read_csv('/Users/mak/Desktop/Code_With_Me/project/prepa-insights/c.csv')
Ctx=dash.callback_context




'''

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
'''


CONTENT_STYLE = {
    "padding-left": "40px",

    'height':'100%',
}


faculties_Tunis = html.Div(
   
    [
    html.H1("Tunis:" ,id='tunis', className="bg-light p-2 rounded"),
    dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src=photo, top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dcc.Link(html.Button("View Statistics"), href="/page"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

        ],

        className="mt-5", justify='around', align='center'
        ),

    dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                

        ],

        className="mt-5", justify='around', align='center'
        ),
    
        dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                

        ],

        className="mt-5", justify='around', align='center'
        ),
        


    ],
style={"padding":"20px" , "margin-top":"0px"},            
className="bg-dark rounded  ")   


faculties_Bizert = html.Div(
   
    [
    html.H1("Bizert:" ,id='bizert', className="bg-light p-2 rounded"),
    dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dcc.Link(html.Button("LOG_VIEW"), href="/page"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

        ],

        className="mt-5", justify='around', align='center'
        ),

    dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                

        ],

        className="mt-5", justify='around', align='center'
        ),
    
        dbc.Row(
        [
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),

            
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                dbc.Card(
                    [
                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    ],
                    
                    className="d-flex justify-content-between",
                    style={"width": "18rem", },
                ),
                

        ],

        className="mt-5", justify='around', align='center'
        ),
        


    ],
style={"padding":"20px" , "margin-top":"40px"},            
className="bg-dark rounded  ")    
    


content = html.Div(
    
    [
        #dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        #dcc.Graph(id='graph-content'),
        #dl.Map(dl.TileLayer(), center=[56,10], zoom=6, style={'height': '70vh'})
        faculties_Tunis,
        faculties_Bizert
        
        
    ],
    
    style=CONTENT_STYLE
    
    
    
    
    
    )


layout = html.Div([
    content,

])
'''
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')
'''