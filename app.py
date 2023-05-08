import pandas as pd
import plotly.express as px

# Read the penguin size data
df = pd.read_csv('./data/penguins_size.csv')
# Remove rows with empty cells 'NaN'
df = df.dropna()

# View
print(df)
