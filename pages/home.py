import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dash_table

##### Read and clean the penguin size data  #####
df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()
df = df.drop(df[(df['Sex'] != 'MALE') & (df['Sex'] != 'FEMALE')].index)


def title():
    return f'Palmer Penguin Data'


def description():
    return f'Data visualization of the Palmer Penguin data'


##### Set the path for home page #####
dash.register_page(__name__, name="Home", path='/',
                   title=title, description=description, top_nav=True)

##### Create the layout #####
layout = html.Div(children=[
    dash_table.DataTable(data=df.to_dict('records'),
                         page_size=10, style_table={'overflowX': 'auto'})
])
