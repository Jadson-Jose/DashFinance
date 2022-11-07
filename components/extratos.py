from dash.dependencies import Input, Output
from dash import dash_table
# from dash.dash_table.Fromat import group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app


# ============== Layout ==============
layout = dbc.Col([
    html.H5('Extratos')
],)