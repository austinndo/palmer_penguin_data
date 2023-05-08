import dash
from dash import html, dcc


def title():
    return f'Palmer Penguin Data'


def description():
    return f'Data visualization of the Palmer Penguin data'


# Set the path for home page
dash.register_page(__name__, path='/', title=title, description=description)

layout = html.Div(children=[
    html.H1(children='This is the Palmer Penguin Home page'),
    html.Div(children=''' This is the Home page content '''),
])
