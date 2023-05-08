import dash
from dash import html

dash.register_page(__name__)

layout = html.H1(
    "There seems to be something wrong with this path. Please return to another page.")
