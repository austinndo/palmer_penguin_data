import dash
import pandas as pd
# import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

##
# Consider using dcc tabs to separate content instead of multipage!
##

# Read and clean the penguin size data
df = pd.read_csv('csv_files/penguins_size.csv')
df = df.dropna()

# Initialize dash app, add styling. use_pages=True to enable multipage
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.YETI])

# # Set layout
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

# View
# print(df)

# Table
# dash_table.DataTable(data=df.to_dict('records'), page_size=10)
