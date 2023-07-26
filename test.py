from gazpacho import get, Soup
import requests

import json
url = 'https://drivepublic.hqontario.ca/Report/GetWaitTimesEDData'
html = get(url)
soup = Soup(html)
type(html)

data = json.loads(html)
len(data)

pd.DataFrame(data)

# ------------------------------------------


import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

df['total exports'].max()

df[df['total exports']==df['total exports'].max()]


for col in df.columns:
    df[col] = df[col].astype(str)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

df['code'].unique()


df['text'] = df['state'] + '<br>' + \
    'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
    'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
    'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = df['code'],
    z = dff['Deaths'].astype(float),
    locationmode = 'USA-states',
    text = df['state'],
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "Millions USD")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = '2011 US Agriculture Exports by State<br>(Hover for breakdown)'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
fig.show()

# ------------------------------------------


dff = pd.read_csv('old_data.csv')
dff = dff.dropna()

dff['Deaths'] = pd.to_numeric(dff['Deaths'], errors="coerce")
dff = dff[dff['Year'] == 2015]

dff = pd.DataFrame(dff.groupby('County')['Deaths'].sum()).reset_index()

dff = dff.rename(columns={'County': 'code'})

dff['code'] = dff['code'].str.strip()

dff.head()


for col in dff.columns:
    dff[col] = dff[col].astype(str)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]
#dff['text'] = dff['code'] + '<br>' + dff['Deaths']

data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = dff['code'],
    z = dff['Deaths'].astype(float),
    locationmode = 'USA-states',
    text = dff['code'],
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "hello")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = '2011 US Agriculture Exports by State<br>(Hover for breakdown)'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
fig.show()
