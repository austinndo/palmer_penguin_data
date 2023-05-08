import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

# Read and clean the penguin size data
df = pd.read_csv('./data/penguins_size.csv')
df = df.dropna()

# Initialize dash app, add styling
app = Dash(__name__, external_stylesheets=[dbc.themes.YETI])

# Set layout
app.layout = html.Div([
    html.Div(children='Palmer Penguin Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

if __name__ == '__main__':
    app.run_server(debug=True)

# # View
# print(df)
