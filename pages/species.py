import dash
import dash_bootstrap_components as dbc
import plotly_express as px
from dash import html, dcc, callback, Output, Input
from .home import df

dash.register_page(__name__)


layout = html.Div([
    html.H1("Species graph"),
    dcc.RadioItems(options=['Adelie', 'Chinstrap',
                   'Gentoo'], value='Adelie', id='controls-and-radio-item'),
    dcc.Graph(figure=px.scatter(df, x='species', y='culmen_length_mm'))
    # dcc.Graph(figure={}, id='controls-and-graph')
])


# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value'))
# def update_graph(species):
#     fig = px.scatter(df, x='culmen_length_mm', y=species)
#     return fig
