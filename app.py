import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input

# Read the penguin size data
df = pd.read_csv('./data/penguins_size.csv')
# Remove rows with empty cells 'NaN'
df = df.dropna()

# Initialize dash app
app = Dash(__name__)

# Set layout
app.layout = html.Div([
    html.Div(children='Palmer Penguin Data')
])

if __name__ == '__main__':
    app.run_server(debug=True)

# # View
# print(df)
