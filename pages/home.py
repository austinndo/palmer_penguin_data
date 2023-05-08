import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from .nav import navbar


def title():
    return f'Palmer Penguin Data'


def description():
    return f'Data visualization of the Palmer Penguin data'


# Set the path for home page
dash.register_page(__name__, path='/', title=title, description=description)

layout = html.Div(children=[
    html.H1(children='This is the Home page'),
    html.Div(children=''' This is the Home page content '''),
    dbc.Row([dbc.Col(navbar(), width=2)]),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])
