import pandas as pd
import plotly.express as px

import os
os.chdir('worldwide-timeseries')


world_cases = pd.read_csv('WHO-COVID-19-global-data.csv')

world_cases['Date'] = pd.to_datetime(world_cases['Date_reported'], format='%Y-%m-%d', exact=False)
world_cases = world_cases.sort_values(by='Date_reported') # sort rows based on timestamp
# world_cases['Date'] = world_cases.timestamp.apply(lambda x: x.date()).apply(str) # convert timestamp to a string

world_cases[' Cumulative_cases'] = pd.to_numeric(world_cases[' Cumulative_cases'])
  
fig = px.choropleth(world_cases, 
                    locations =" Country", 
                    locationmode = 'country names',
                    color=" Cumulative_cases", 
                    hover_name =" Country",  
                    color_continuous_scale = px.colors.sequential.Darkmint, 
                    scope ="world", 
                    animation_group ="Date_reported",
                    animation_frame = 'Date_reported',
                    labels={'Date_reported': 'Date', ' Cumulative_cases':'Total Cases', ' Country':'Country'},
                    hover_data=[' Cumulative_cases', 'Date_reported'],
                    title='Cumulative COVID-19 cases by date per country'
                    ) 
fig.show()

fig.write_html("/Users/Neha/Downloads/python/covid-19-viz/worldwide-timeseries/final-viz.html", include_plotlyjs='cdn')