import dash
from dash import html
import dash_bootstrap_components as dbc

# Classname ms-2 = margin start. Use for formatting


def navbar():
    return html.Div(
        dbc.Nav([
            dbc.NavLink([
                html.Div(page["name"], classname="ms-2")
            ], href=page["path"], active="exact",)
            for page in dash.page_registry.values() if page["path"].startswith("/home")
        ],)
    )
