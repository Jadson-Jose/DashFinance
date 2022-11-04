from dash.dependencies import Input, Output
from dash import dash_table
# from dash.dash_table.Fromat import group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# ============== Layout ==============
layout = dbc.Col([
    html.H1("MyBudget", className="text-primary"),
    html.P("By Jadson Silva", className="text-info"),
    html.Hr(),

    # Seção Perfil --------------------------------------------
    dbc.Button(id='botao_avatar', children=[html.Img(
        src='/assets/img_hom.png', id='Avatar_change', alt='Avatar', className='perfil_avatar')], style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # Seção Novo --------------------------------------------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-novo-receita',
                       children=['+ Receita'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa',
                       children=['- Despesa'])
        ], width=6)
    ]),

    # Seção Nav --------------------------------------------
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("extratos", href="/estratos", active="exact"),
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})

])
