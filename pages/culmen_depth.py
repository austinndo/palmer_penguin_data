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
    return f'Culmen Depth Comparison'


def description():
    return f'Comparison of Palmer penguins culmen depth'


dash.register_page(__name__, path='/culmen_depth',
                   title=title, description=description)

#####  Create my figures  #####
species_fig = px.scatter(
    data_frame=df, x=df['Sample Number'], y=df['Culmen Depth (mm)'], title='Culmen Depth by Species', color=df['Species'])

island_fig = px.scatter(
    data_frame=df, x=df['Sample Number'], y=df['Culmen Depth (mm)'], title='Culmen Depth by Island', color=df['Island'])

sex_fig = px.scatter(
    data_frame=df, x=df['Sample Number'], y=df['Culmen Depth (mm)'], title='Culmen Depth by Sex', color=df['Sex'])


##### Set the layout #####
layout = html.Div([
    dcc.Tabs(id='culmen_depth_tabs', value='species', children=[
        dcc.Tab(label='Species', value='species'),
        dcc.Tab(label='Island', value='island'),
        dcc.Tab(label='Sex', value='sex'),
    ]),
    html.Div(id='culmen_depth_graphs'),
])

##### Interactivity with callbacks #####


@callback(
    Output('culmen_depth_graphs', 'children'),
    Input('culmen_depth_tabs', 'value')
)
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
