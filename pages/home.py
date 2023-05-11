import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, dash_table
from .nav import navbar

# Read and clean the penguin size data
df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()


def title():
    return f'Palmer Penguin Data'


def description():
    return f'Data visualization of the Palmer Penguin data'


# Set the path for home page
dash.register_page(__name__, path='/', title=title, description=description)

layout = html.Div(children=[
    dbc.Row([dbc.Col(navbar(), width=2)]),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])
