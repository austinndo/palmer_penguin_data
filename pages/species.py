import dash
import dash_bootstrap_components as dbc
import plotly_express as px
from dash import html, dcc
from .home import df

dash.register_page(__name__)


layout = html.Div([
    html.H1("Species graph"),
    dcc.Graph(figure=px.scatter(df, x='species', y='culmen_length_mm'))])
