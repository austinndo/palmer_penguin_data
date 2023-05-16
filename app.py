import dash
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

##### Read and clean the penguin size data. dropna() to remove rows with empty cell(s) #####
df = pd.read_csv('csv_files/penguins_lter.csv')
df = df.drop(columns=['studyName', 'Region', 'Stage', 'Comments',
             'Clutch Completion', 'Date Egg', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)'])
df = df.dropna()
df = df.drop(df[(df['Sex'] != 'MALE') & (df['Sex'] != 'FEMALE')].index)
# Goes from 344 to 333 records

##### Initialize dash app, add styling. use_pages=True to enable multipage #####
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[
           dbc.themes.YETI])
server = app.server

##### Navbar #####
nav_links = [
    dbc.NavItem(
        dbc.NavLink("Data Table", active="exact", href="/")),
    dbc.NavItem(
        dbc.NavLink("Body Mass", active="partial", href="/body_mass")),
    dbc.NavItem(
        dbc.NavLink("Culmen Depth", active="partial", href="/culmen_depth")),
    dbc.NavItem(
        dbc.NavLink("Culmen Length", active="partial", href="/culmen_length")),
    dbc.NavItem(
        dbc.NavLink("Flipper Length", active="partial", href="/flipper_length"))
]

nav = dbc.Nav(nav_links, pills=True, justified=True)

##### Set layout  #####
app.layout = html.Div([
    html.H1('Palmer Penguin Data'),
    nav,
    dash.page_container,
])


if __name__ == '__main__':
    app.run_server(debug=True)
    # print(df)
