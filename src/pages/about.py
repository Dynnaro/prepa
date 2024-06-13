import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State, callback
import dash_leaflet as dl
import pandas as pd
import plotly.express as px

dash.register_page(__name__, order=2, path="/about")



about_us = html.P(['This project is made from students to Students.', html.Br(), 'The goal is to provide Prepa studnets with informations about each engineering school to help them make the appropriate choice for their orientation.'], className="border rounded bg-light p-3")


layout = html.Div(
    [

        about_us,

        
    ],
    style={
      
        'margin-top':"3vw",
        'height':'100vh'
        
    },
    
    className="d-flex justify-content-center align-items-start ",
    

    
    
)

