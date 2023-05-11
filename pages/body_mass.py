import pandas as pd
import dash
import plotly_express as px
from dash import callback, dcc, html, Input, Output, dash_table


df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()


def title():
    return f'Body Mass Comparison'


def description():
    return f'Comparison of Palmer penguins body mass in grams'


dash.register_page(__name__, path='/body_mass',
                   title=title, description=description)

# species_fig = px.scatter(
#     data_frame=df, x=[0, 1, 2, 3, 4, 5], y=[5, 12, 14, 6, 7, 8])

species_fig = px.scatter(
    data_frame=df, x=df['Sample Number'], y=df['Body Mass (g)'])

# Trying to return a figure in the children of html.Div([ ]) seems to cause errors. "An object was provided as `children` instead of a component, string, or number... ""
layout = html.Div([
    dcc.Tabs(id='body_mass_tabs', value='species', children=[
        dcc.Tab(label='Species', value='species'),
        dcc.Tab(label='Island', value='island'),
        dcc.Tab(label='Sex', value='sex'),
    ]),
    html.Div(id='body_mass_graphs'),
])


@callback(
    Output('body_mass_graphs', 'children'),
    Input('body_mass_tabs', 'value')
)
def render(tab):
    if tab == 'species':
        return html.Div([
            html.H3('Body Mass by Species'),
            dcc.Graph(
                figure=species_fig
            )
        ])
    elif tab == 'island':
        return html.Div([
            html.H3('Body Mass by Island'),
        ])
    elif tab == 'sex':
        return html.Div([
            html.H3('Body Mass by Sex'),
        ])
