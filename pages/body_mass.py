import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

df = pd.read_csv('csv_files/penguins_size.csv')
df = df.dropna()


def title():
    return f'Body Mass Comparison'


def description():
    return f'Comparison of Palmer penguins body mass in grams'


dash.register_page(__name__, path='/body_mass',
                   title=title, description=description)

layout = html.Div([
    dcc.Tabs(id='body_mass_tabs', value='species', children=[
        dcc.Tab(label='Species', value='species'),
        dcc.Tab(label='Island', value='island'),
        dcc.Tab(label='Sex', value='sex'),
    ]),
    html.Div(id='body_mass_content')
])


# @Dash(__name__).callback(
#     Output('body_mass_content', 'children'),
#     Input('body_mass_tabs', 'value')
# )
def render(tab):
    if tab == 'species':
        return html.Div([
            html.H3('Body Mass by Species'),
        ])
    elif tab == 'island':
        return html.Div([
            html.H3('Body Mass by Island'),
        ])
    elif tab == 'sex':
        return html.Div([
            html.H3('Body Mass by Sex'),
        ])
