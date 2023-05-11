import dash
import pandas as pd
# import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

##### Read and clean the penguin size data. dropna() to remove rows with empty cell(s) #####
df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()

##### Initialize dash app, add styling. use_pages=True to enable multipage #####
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.YETI])

##### Set layout  #####
app.layout = html.Div([
    html.H1('Palmer Penguin Data'),
    html.Div([
        html.Div(
            dcc.Link(
                f"{page['name']} - {page['path']}", href=page["relative_path"]
            )
        )
        for page in dash.page_registry.values()
    ]),
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)
    # print(df)
