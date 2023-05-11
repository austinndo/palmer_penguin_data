import pandas as pd
import dash
import plotly_express as px
from dash import callback, dcc, html, Input, Output

##### Read and clean the data #####
df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()
df = df.drop(df[(df['Sex'] != 'MALE') & (df['Sex'] != 'FEMALE')].index)

##### Set up and register this Dash page #####


def title():
    return f'Body Mass Comparison'


def description():
    return f'Comparison of Palmer penguins body mass in grams'


dash.register_page(__name__, path='/body_mass',
                   title=title, description=description)

#####  Create my figures  #####
species_fig = px.box(
    data_frame=df, x=df['Species'], y=df['Body Mass (g)'], title='Body Mass by Species', color=df['Species'])

island_fig = px.box(
    data_frame=df, x=df['Island'], y=df['Body Mass (g)'], title='Body Mass by Island', color=df['Island'])

sex_fig = px.box(
    data_frame=df, x=df['Sex'], y=df['Body Mass (g)'], title='Body Mass by Sex', color=df['Sex'])


##### Set the layout #####
layout = html.Div([
    dcc.Tabs(id='body_mass_tabs', value='species', children=[
        dcc.Tab(label='Species', value='species'),
        dcc.Tab(label='Island', value='island'),
        dcc.Tab(label='Sex', value='sex'),
    ]),
    html.Div(id='body_mass_graphs'),
])

##### Interactivity with callbacks #####


@callback(
    Output('body_mass_graphs', 'children'),
    Input('body_mass_tabs', 'value')
)
# Trying to return a figure in the children of html.Div([ ]) seems to cause errors. "An object was provided as `children` instead of a component, string, or number... ""
# use dcc.Graph() to specify the figure to render
def render(tab):
    if tab == 'species':
        return html.Div([
            dcc.Graph(
                figure=species_fig
            )
        ])
    elif tab == 'island':
        return html.Div([
            dcc.Graph(
                figure=island_fig
            )
        ])
    elif tab == 'sex':
        return html.Div([
            dcc.Graph(
                figure=sex_fig
            )
        ])
